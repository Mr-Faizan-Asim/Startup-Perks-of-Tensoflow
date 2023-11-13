# find the mean
def mean(values):
    return sum(values) / float(len(values))

# ya like aisa ha jasa direct or indirect proportional ha
def covariance(x,mean_x,y,mean_y):
    cover = 0.0
    for i in range(len(x)):
        cover += (x[i] - mean_x) * (y[i] - mean_y)
    return cover

def cofficients(x,y):
    x_mean,y_mean = mean(x),mean(y)
    b1 = covariance(x,x_mean,y,y_mean)
    b0 = y_mean - b1* x_mean
    return b0,b1

def simple_linear_regression(x, b0, b1):
    return b0 + b1 * x


x_train = [1,2,3,4,5]
y_train = [3,5,7,9,11]

b0, b1 = cofficients(x_train, y_train)

x_test = [6, 7, 8]
y_pred = [simple_linear_regression(x, b0, b1) for x in x_test]


print(f'Coefficients: b0={b0}, b1={b1}')

for i in range(len(x_test)):
    print(f'Input={x_test[i]}, Predicted Output={y_pred[i]}')
    

