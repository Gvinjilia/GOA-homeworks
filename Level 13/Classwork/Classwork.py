#1) შექმენით სია, რომელსაც შეინახავთ ცვლადში სახელად friends. მაგ სიაში უნდა 
#შეინახოთ მინიმუმ 5 მეგობრის სახელი. პირველ რიგში გამოიტანეთ თქვენი საუკეთესო 
#მეგობრის სახელი 
#ინდექსების დახმარებით. დაბეჭდეთ სია. შეცვლაეთ მე-3 ინდექსზე მყოფი სახელი ახალით 
#და დაბეჭდეთ სია. საბოლოოდ დაბეჭდეთ მთლიანი სიის სიგრძე
friends=["Salome","Mariami","Anastasia","Barbare","Nana"]
friends[3]="lizi"
print(friends)
print(len(friends))
#2)შექმენით მანქანების სია, სადაც გამოიყენებთ ერთ-ერთ ფუნქციას, რომ სიაში დაამატოთ 
#ახალი მანქანა. 
#ეხლით არ უნდა ჩაწეროთ(ამისათვის დაგჭირდებათ ფუნქცია)!!!
cars=["BMW","Toyota","Mercedes"]
cars.append("BMW")
print(cars)
#3) შექმენით რიცხვების სია სადაც გექნებათ მინიმუმ ხუთი რიცხვი. შეცვლაეთ ამ სიის 
#პირველი ელემენტი და გაუტოლეთ ის 50-ს. შემდეგ კი 
#გამოიტანეთ სიიდან პირველი და ბოლო რიცხვის ჯამი
numbers=[1,2,3,4,5,6,7]

numbers[0] = 50

print(numbers[0] + numbers[4])