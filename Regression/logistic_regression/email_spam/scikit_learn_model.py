from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix

import pandas as pd

file_path = r"C:\Users\chaha\OneDrive\Documents\ML\data\supervised_learning\spam_email\emails.csv"

df = pd.read_csv(file_path)
y = df["spam"]

vectorizer = CountVectorizer()
#convert string to numbers
X = vectorizer.fit_transform(df["text"])

model = LogisticRegression()
#split data into train and test
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state = 42)

model.fit(train_X, train_y)


predict_y = model.predict(test_X)
#check accuracy score
result = accuracy_score( predict_y, test_y)

#confusion_matrix
matrix = confusion_matrix(predict_y, test_y)
#[[1060   14]
# [   3  355]]

#test on String input
text = "WINNER!! You have won a $1000 cash prize. Call now to claim."
vsct_out = vectorizer.transform([text])
out = model.predict(vsct_out)

print("out is : ", out)
