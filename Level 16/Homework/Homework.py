#შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე დიდი რიცხვი
numbers = [1, 4, 2, 77, 9, 3, 2]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number

print("Max_Number:", max_number)
#შექმენით რიცხვების სია და დაბეჭდეს სიის თითოეული რიცხვის ფაქტორიალი
import math
numbers = [4, 3, 6, 5, 44, 7, 8, 9]
for num in numbers:
    factorial = math.factorial(num)
    print(f"{num} factorial is: {factorial}")
#შექმენით სია სადაც გექნებათ რიცხვები. for loop-ის გამოყენებით იპოვეთ ამ სიაში ყველაზე პატარა რიცხვი
numbers=[2,9,8,6,5,3,5]
min_numbers=numbers[0]
for number in numbers:
    if number<min_numbers:
        min_number=number
print("Min_Numbers:",min_numbers)
#შექმენით რიცხვების სია სადაც გექნებათ დადებითი და უარყოფითი რიცხვები, შემდეგ შექმენით ახალი სია სადაც გექნებათ 
#მხოლოდ უარყოფითი რიცხვები და დაბეჭდეთ ის(გამოიყენეთ while).
numbers = [10, -5, 3, -2, -8, 7, -1, 6]
negative_numbers = []
index = 0

while index < len(numbers):
    if numbers[index] < 0:
        negative_numbers.append(numbers[index])
    index += 1

print("Negative_Numbers:", negative_numbers)

#შექმენით რიცხვების სია და დაპრინტეთ სიის თითოეული ელემენტი უკუღმა(გამოიყენეთ range() ფუქნცია ან შექმენით ცვლადი)
numbers = [1, 2, 3, 4, 5, 6, 7]
for i in range(len(numbers) - 1, -1, -1):
    print(numbers[i])
#შექმენით სიმბოლოების სია, სადაც იქნება დუბლიკატები. შექმენით ახალი სია სადაც ყველა სიმბოლო მხოლოდ ერთხელ გვხვდება
simboloebi=[1,1,3,3,4,5,6,7,8,9]
simboloebi=[1,9,5,3,29,10]
#შექმენით ცლვადი სადაც შეინახავთ string-ს, შემდეგ შექმენით ახალი ცვლადი სადაც შეინახავთ ამ სტრინგს შემოტრიალებულად და დაბეჭდეთ ის
str="Nino"
str2="oniN"
print(str2)
#დაწერეთ პროგრამა, რომელიც მომხამრებელს შემოატანინებს რიცხვს და აბრუნებს სიას, სადაც იქნება გამდოცემული რიცხვის ყველა გამყოფი
print(input("Enter a number:"))
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)
print("number devisiors are:", divisors)
#შექმენით პროგრამა, რომელიც მომხარებელს შემოატანინებს წელს და დაპრინტავს რომელი საუკუნეა ის
year = int(input("Enter a year: "))
century = (year - 1) // 100 + 1
print(f"{year} year is {century} century")