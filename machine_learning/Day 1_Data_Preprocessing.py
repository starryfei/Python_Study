# -*- coding=utf-8 -*-'''
import numpy as np
import pandas as pd

dataset = pd.read_csv('../Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values
print(dataset)
print("Step 2: Importing dataset")
print("X")
print(X)
print("Y")
print(Y)
# Step 3: Handling the missing data
from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values='NaN', strategy="mean", axis=0)
# 使用数组X去“训练”一个Imputer类，然后用该类的对象去处理X[:, 1:3]的缺失值，
# 缺失值的处理方式是使用X中的均值（axis=0表示按列进行）代替X[:, 1:3]中的缺失值。
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
print("---------------------")
print("Step 3: Handling the missing data")
print("step2")
print("X")
print(X)
# Step 4: Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# Creating a dummy variable
onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)
print("---------------------")
print("Step 4: Encoding categorical data")
print("X")
print(X)
print("Y")
print(Y)

# Step 5: Splitting the datasets into training sets and Test sets
from sklearn.model_selection import train_test_split

# 函数用于将矩阵随机划分为训练子集和测试子集，并返回划分好的训练集测试集样本和训练集测试集标签。
# train_data：被划分的样本特征集
# train_target：被划分的样本标签
# test_size：如果是浮点数，在0-1之间，表示样本占比；如果是整数的话就是样本的数量
# random_state：是随机数的种子。
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
print("---------------------")
print("Step 5: Splitting the datasets into training sets and Test sets")
print("X_train")
print(X_train)
print("X_test")
print(X_test)
print("Y_train")
print(Y_train)
print("Y_test")
print(Y_test)
# Step 6: Feature Scaling
from sklearn.preprocessing import StandardScaler
# StandardScaler 去均值和方差归一化。且是针对每一个特征维度来做的，而不是针对样本。
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
print("---------------------")
print("Step 6: Feature Scaling")
print("X_train")
print(X_train)
print("X_test")
print(X_test)
