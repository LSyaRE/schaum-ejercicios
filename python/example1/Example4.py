
from NumbersArray import NumbersArray
# In this example 
#We can do a sum with more of 2 values using arrays.
example3 = NumbersArray()
example3.setNumbers(5)
numbers= example3.getNumbers()

#We can use while loop here too but I prefer use more for loop in this case 
for i in range(len(numbers)-1):
    if i == 0:
        sum = numbers[i]
    sum += numbers[i+1]

print(sum)