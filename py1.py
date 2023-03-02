MIN_NUM = 1
MAX_NUM = 999

number = int(input(f"Add number from {MIN_NUM} to {MAX_NUM} "))
if number < 10:
    result = number ** 2
elif number >=10 and number < 100:
    a = number // 10
    b = number % 10
    result = a * b
else:
    a = number // 100
    b = (number % 100) // 10
    c = number % 10 
    
    result = c * 100 + b * 10 + a
print(result)

