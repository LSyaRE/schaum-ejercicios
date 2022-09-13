from NumbersArray import NumbersArray


example3 = NumbersArray()
example3.setNumbers(2)
numbers=example3.getNumbers()

for i in range(len(numbers)-1):
    if i == 0:   
        A= numbers[i]
    A = A * numbers[i+1]
    


print(A)