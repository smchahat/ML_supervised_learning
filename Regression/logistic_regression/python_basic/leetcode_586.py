#thiss is a SQL query 

select customer_number from (
select count(order_number) as c , customer_number from Orders group by customer_number order by c desc limit 1) t1;


SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(order_number) DESC
LIMIT 1;
