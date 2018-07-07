#checking whether a value is not in a list
banned_users=['andrew','carolina','david']
user='marie' # marie is not in the banned list

if user not in banned_users:
    print(user.title()+", you can post a response if you wish")
else:
    print(banned_users)
print('----')

#boolean expression = True or False
#boolean values are often used to keep track of certain conditions
game_active=True
can_edit=False

