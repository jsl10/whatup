#using a while loop with lists and dictionaries
"""
a for loop is effective for looping through a list, but you shouldn't modify
a list inside a for loop ecause python will have trouble keeping track of the items in the list.
To modify a list as you work through it, use a while loop.
while loops with lists and dictionaries allows you to collect, store and organize
lots of input to examine and report on later.
"""

#while loop to pull users from the list of unconfirmed users as we verify and then add then to seperate list of confirmed user.

#start with users that need to be verified,
#and an empty list to hold confirmed users.

unconfirmed_users=['alice','brian','candance']
confirmed_users=[]

#verify each user until there are no more unconfirmed users
#move each verified user into the list of confirmed user
while unconfirmed_users:
    #remove unvertified users one at a time from the end of unconfirmed_users
    current_user=unconfirmed_users.pop()

    print("Verifying user: "+current_user.title())
    confirmed_users.append(current_user)

    #Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
