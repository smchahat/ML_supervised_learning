#LogisticRegression

import pandas as pd
from sklearn.linear_model import LogisticRegression
from scipy.io import arff

#loading data file
data, meta =arff.loadarff(r"C:\Users\chaha\Documents\ML\data\supervised_learning\diabetes\dataset_37_diabetes.arff")
input_data = pd.DataFrame(data)

#seperating target and input data
actual_result = input_data['class'].str.decode('UTF_8')
i_data = input_data.drop(columns = ['class'])
i_data.head()

#passing values to model
obj = LogisticRegression(max_iter =500)
obj.fit(i_data.values, actual_result)

#predicting output class
obj.predict([[1.0, 150, 63, 25, 75, 73.2, .725, 34]])