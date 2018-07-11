"""
you can nest a list inside a dictionary any time you want more than one value
to be associated with a single key in a dictionary.
When we loop through the dictionary, the value associated with each person
would be a list of languages rather than a single language.
Inside the dictionary's for loop,
we use another for loop to run through the list of languages associated with each person
"""
#value associated with each name is now a list
favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    }
#use variable name languages to hold each value from the dictionary, bc that each value will be a list
for name, languages in favorite_languages.items():
    print("\n"+name.title()+"'s favorite language are:")
    #run through each person's list of favorite languages
    for language in languages:
        print("\t"+language.title())
