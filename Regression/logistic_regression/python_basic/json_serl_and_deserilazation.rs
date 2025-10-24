use serde_json::Value; 
//find issue in this code 
//show the issue 
// propse a solution

 
fn main() {
 let json = r#" 
 { 
 "name": "Alice",
 "age": 30, 
 "is_student": true, 
 "grades": [85.5, 90.0, 78.0], 
 "address": { 
	"street": "123 Main St", 
	"city": "Wonderland" 
	} 
} "#; 

let parsed: Value = serde_json::from_str(json).unwrap();
println!("Parsed JSON: {:?}", parsed);

let mut writer = Vec::new();
write(&parsed, &mut writer);
println!("Serialized bytes: {:?}", writer);

let mut reader = &writer[..];
let deserialized: Value = read(&mut reader);
println!("Deserialized JSON: {:?}", deserialized);

}

fn write(json: &Value, writer: &mut Vec<u8>) {
	match json {
		Value::Null => writer.push(0x00),
		Value::Bool(value) => {
			writer.push(0x01);
			writer.push(if *value { 0x01 } else { 0x00 });
		}
		Value::Number(n) => {
			if let Some(i) = n.as_i64() {
				writer.push(0x02);
				writer.extend_from_slice(&i.to_be_bytes());
			}
			else if let Some(i) = n.as_u64() { 
				writer.push(0x02); 
				writer.extend_from_slice(&i.to_be_bytes());
			} 
			else if let Some(f) = n.as_f64() {
				writer.push(0x03); 
				writer.extend_from_slice(&f.to_be_bytes());
			} 
		} 
		Value::String(s) => {
			writer.push(0x04); 
			let len = s.len() as u16; 
			writer.extend_from_slice(&len.to_be_bytes()); 
			writer.extend_from_slice(s.as_bytes()); 
		}
		Value::Array(a) => { 
			writer.push(0x05); 
			let len = a.len() as u16; 
			writer.extend_from_slice(&len.to_be_bytes()); 
			for item in a { 
				write(item, writer); 
			} 
		}
		Value::Object(o) => { 
			writer.push(0x06); 
			let len = o.len() as u16; 
			writer.extend_from_slice(&len.to_le_bytes()); 
			for (key, value) in o { 
				let key_len = key.len() as u16;
				writer.extend_from_slice(&key_len.to_be_bytes()); 
				writer.extend_from_slice(key.as_bytes()); 
				write(value, writer); 
			} 
		} 
	} 
}

fn read(reader: &mut &[u8]) -> Value { 
	let type_byte = reader[0]; 
	*reader = &reader[1..]; 
	match type_byte { 
		0x00 => Value::Null, 
		0x01 => { 
			let value = reader[0] != 0; 
			*reader = &reader[1..]; 
			Value::Bool(value) 
		} 
		0x02 => { 
			let mut buf = [0; 8]; 
			buf.copy_from_slice(&reader[..8]); 
			*reader = &reader[8..]; 
			let i = i64::from_be_bytes(buf); 
			Value::Number(serde_json::Number::from(i)) 
		}
		0x03 => { 
			let mut buf = [0; 8]; 
			buf.copy_from_slice(&reader[..8]); 
			*reader = &reader[8..]; 
			let f = f64::from_be_bytes(buf); 
			Value::Number(serde_json::Number::from_f64(f).unwrap())
		}
		0x04 => { 
			let len = u16::from_be_bytes([reader[0], reader[1]]) as usize; 
			*reader = &reader[2..]; 
			let s = String::from_utf8(reader[..len].to_vec()).unwrap(); 
			*reader = &reader[len..]; 
			Value::String(s) 
		} 
		0x05 => { 
			let len = u16::from_be_bytes([reader[0], reader[1]]) as usize; 
			*reader = &reader[2..]; 
			let mut arr = Vec::with_capacity(len); 
			for _ in 0..len { 
				arr.push(read(reader));
			}
			Value::Array(arr) 
		}
		0x06 => { 
			let len = u16::from_le_bytes([reader[0], reader[1]]) as usize; 
			*reader = &reader[2..]; 
			let mut obj = serde_json::Map::new(); 
			for _ in 0..len { 
				let key_len = u16::from_be_bytes([reader[0], reader[1]]) as usize; 
				*reader = &reader[2..]; 
				let key = String::from_utf8(reader[..key_len].to_vec()).unwrap(); 
				*reader = &reader[key_len..]; 
				let value = read(reader); 
				obj.insert(key, value); 
			} 
			Value::Object(obj) 
		} 
		_ => panic!("Unknown type byte: {}",type_byte), 
	}
}

