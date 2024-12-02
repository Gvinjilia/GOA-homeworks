# word = "Hello World!"
# print(word.count("l"))
# count function.count
# example 1
# how to do a clone of count function 

# 1) შექმენით ცვლადი, სადაც შეინახავთ string-ს. დაბეჭდეთ მისი თითოეული სიმბოლო და გვერდით მიუწერეთ რიგით მერამდენეა ის.
# მგალითად: "Hello" >>> "H - 1", "e - 2"...
string = "Hello"
for i in range(len(string)):
    print(string[i], "-", i + 1)
# შექმენით manual_join ფუნქცია, რომელსაც გადაეცემა სთინგების სია და ერთი სთრინგი. ამ ფუნქციამ უნდა შეართოს ეს 
# სია და თითოეულ ელემენტს შორის ჩასვას გადმოცემული სთრინგი
# არ გამოიყენოთ .join() ფუნქცია
def manual_join(items):
    result = ""
    for i in range(len(items)):
        result += items[i]
        if i < len(items) - 1:
            result += " "
    return result
print(manual_join(["hello", "world", "python"]))

# 3) შექმენით manual_count ფუნქცია, რომელსაც გადაეცემა სთრინგი ნა სია და ელემენტი რომლის რაოდენობაც უნდა გაიგოთ. დააბრუნეთ მიღებული შედეგი.
def manuel_count (listn,symbol):
    count=0
    for i in listn:
        if symbol == i:
            count += i
    return count
# 4) შექმენით manual_replace ფუნქცია, რომელიც იქნება .replace() ფუნქციის კლონი. ამ ფუნქციამ სთრინგში არსებული sapce-ები უნდა შეცვალოს ტირეებად.
def custom_replace(string, old_string, new_string):
    result = ""
    i = 0
    while i < len(string):
        if string[i:i+len(old_string)] == old_string:
            result += new_string
            i += len(old_string)
        else:
            result += string[i]
            i += 1
    return result
# ფუნქციის გამოყენება და შედეგის დაბეჭდვა
print(custom_replace("hello world hello", "hello", "python"))
# არ გამოიყენოთ ჩაშენებული ფუნქციები და კომენტარებით ახსენით მე-4 დავალება

# 5) შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. 
# ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.
# გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step
# range ფუნქციის კლონი
def manual_range(start, end, step=1):
    final = start
    while final < end: # სანამ final ნაკლებია end ზე უნდა გავაგრძელოთ for loop ი
        print(final) # მანამდე სანამ final ნაკლებია end ზე უნდა დავპრინტოთ final რადგან დავიწყოთ გარკვეული რიცხვიდან ამ შემთხვევაში #1 თი დან
        final += step  # და ასევე უნდა ჩავამატოთ კიდევ ერთი რიცხვი ანუ არგუმნტი ამ სემტხვევაში step რადგან გავაგძელოთ რიცხვები მაქამდე სანამ არ დამთავრდება  იგი
print(manual_range(1, 10 ,1)) # ბოლოს manual_range გადავცემთ იმ 
#3 არგუმენტს რაც გვინდა რომ დავპრინტოთ start იდან end ამდე ამ შემთხვევაში manual_range ში გადაცემული არგუმენტებიდან გამომდინარე autput ში დაგვიპრინტავს
#შემდეგს 
1
3
5
7
9 # რადგან ჩვეენ მესამე არგუმენტად გვაქვს გადაცემული ის რიცხვი რომლის დროსაც უნდა გამოვტოვით ორ რით  1 + 2  = 3 
# 3 + 2 = 5
# 5 + 2 = 7
# 7 + 2 = 9