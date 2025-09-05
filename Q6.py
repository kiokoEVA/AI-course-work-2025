digit= []
for i in range(5):
    value= int(input(f"Enter any 5 values {i+1}: "))
    digit.append(value)

    #calculate the sum
    avg= sum(digit) / len(digit)
print(f"The average of the entered values is: {avg}")