import statistics, math

def my_add(input):
    print(f'Input : {input}')
    Number = len(input)
    sum = 0
    Average = statistics.mean(input)
    print(f'Mean  : {Average}')
    for x in input:
        sum += (int(x) - Average)**2
    sum = sum / Number
    output = math.sqrt(sum)    
    return output
#1. Input
input = [10,20,30]

#2. Process
answer = my_add(input)

#3. Output
print(f'answer:{answer}')

#1. Input
input = [20,23,18]

#2. Process
answer = my_add(input)

#3. Output
print(f'answer:{answer}')