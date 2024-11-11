#https://www.codewars.com/kata/523b4ff7adca849afe000035
def greet():
    return "hello world!"
#https://www.codewars.com/kata/50654ddff44f800200000004
def multiply(a, b):
    return (a*b)
final=multiply(2,2)
print(final)
#https://www.codewars.com/kata/55a2d7ebe362935a210000b2
def find_smallest_int(arr):
    smallest_int=[]
    for number in arr:
        if number < 0:
            smallest_int +=number
    return smallest_int  
#https://www.codewars.com/kata/5168bb5dfe9a00b126000018
def solution(string):
    return string[::-1]
#https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
#https://www.codewars.com/kata/546e2562b03326a88e000020
def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))
#შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა რიცხვი, ხოლო ამ ფუნქციამ უნდა დაბეჭდოს 1-დან გადმოცემულ რიცხვამდე ყველა რიცხვი
def greet (number):
    for i in range(1,number+1):
        print(i)
greet(4)

#შექმენით ფუნქცია, რომელსაც არგუმენტად გადაეცემა ორი რიცხვი, ხოლო ამ ფუნქციამ უნდა დააბრუნოს პირველი რიცხვი აყვანილი მე-2 რიცხვის ხარისხში
def greet(num1,num2):
    return num1**num2
final=greet(4,2)
print(final)