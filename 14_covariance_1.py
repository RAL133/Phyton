#
# Covariance for Python program
#
import statistics, math

def my_covariance(input_x, input_y):
    cov = 0 
    print(f'input X :{X} ',f'input Y :{Y}')
    Count = len(X)
    avgX = statistics.mean(X)
    avgY = statistics.mean(Y)
    print(f'Mean X: {avgX}',f'Mean Y :{avgY}')
    sum = 0
    for Q in range (len(X)):
        cov += (X[Q]-avgX)*(Y[Q]-avgY)
    cov = cov/Count
    return cov

# 1. Input
X = [10,20,30]
Y = [12,21,33]

# 2. Process
answer = my_covariance(X, Y)
answer = round(answer, 2)

# 3. Output
print(f'Answer: {answer}')
