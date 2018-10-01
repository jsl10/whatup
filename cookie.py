name = "trader joe"
print(name.title())

fname = "george"
lname = "clooney"
fullname = fname + " "+lname

print("Oceans: " +fullname.title())

favLan='python'
print("Favorite: "+ favLan)

cookies = ['amond', 'peanut', 'pistachio']
for cookie in cookies:
    print(cookie.title())
    print(cookie.title()+" ice cream!")
    print(cookie.title()+" & cream") 
print("All fresh from the farm!")
    

num=input("Type number ")
num=(str(num))

for num in range(2,10):
    if num >= 10:
        print()
    else:
        print(num+1)
