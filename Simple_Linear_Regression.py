import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

x = 0
y = 0
def fifi(brown):
    dataset = pd.read_csv(brown)
    global x
    x = dataset.iloc[:,:-1].values
    global y
    y = dataset.iloc[:,-1].values

print('enter the file name my dude')
brown = str(input())
fifi(brown)
print(x)
print(y)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.2,random_state=0)

print(x_train)

print(x_test)

print(y_train)

print(y_test)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

print(y_pred)

print(y_test)


plt.scatter(x_train,y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience(Training Set)')
plt.xlabel('Years of Experiance')
plt.ylabel('Years of Experiance')
plt.show()

plt.scatter(x_test,y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience(Test Set)')
plt.xlabel('Years of Experiance')
plt.ylabel('Years of Experiance')
plt.show()
print('enter the value you want to predict')
prepro = float(input())
na = [[prepro]]
print('The Salary is')
xr = regressor.predict(na)
print(xr[0])

xn=regressor.coef_
yn=regressor.intercept_

print('the coefficient is')
print(xn[0])
print('the intercept is')
print(yn)
print('the equation is ' + str(xn[0]) +'X '+ '+' +str(yn) )