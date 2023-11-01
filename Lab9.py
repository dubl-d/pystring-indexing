##Lab 9


##return to main function
def repeat():
    mMenu = str(input("Would you like to return to the Main Menu: "))
    print("")
    if (mMenu.lower() != "n"):
        ini()

#Pt1
####################################
##i might leave the spaghetti
##but fOne and Two take params from from the string
##v is the vowels its just a string
##for loop is characters in b because b = a that is passed through
##cL is the constant letters uhh if char is in the vowel list
##the counter will go up by 1 and return it back
##the second function is literally the first just with cL uncommented
#a = str(input("Input something."))

def fOne(a):
    b = a
    c = 0
    v = "aeiouAEIOU"
    #cL = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for ch in b:
        if ch in v:
            c+=1
    return c

def fTwo(a):
    b = a
    c = 0
    cL = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for ch in b:
        if ch in cL:
            c+=1
    return c
#d = fOne(a)
#e = fTwo(a)
#print(f"Vowel Count is {d}, Const. Letter count is {e}")
##rewrite into iniF but isss done :D

#####################################
##Pt2
#####################################

def fThree(f):
    #f = str(input("Enter something: "))
    j = f.split()
    g = j[0]
    h = j[1:]
#print(f"{g}{h}")
##I have to say this is probably the most unique line of code I have done
##with a string...I don't know if it's because its spaghetti code or what
##but j takes the input string from f and splits it into a list of words
##g takes j and grabs the first letter of it
##h takes j and grabs the rest of the word
##i is a list that takes the rest of g and adds the first letter of g to the end
##then adds 'AY'
##THEN it adds another list that grabs an index.
##the index then grabs the rest of the word and adds the first letter to the end of it
##and then adds 'AY' BUT it's only doing this while indexing h
##this took me a couple of hours of trial and error, I didn't want to use
##a normal method I guess? would of been alot easier without it I assume
##I hope I explained this as best as I could
    i = [g[1:]+g[0]+'AY']+[_[1:]+_[0]+'AY' for _ in h]
    k = " ".join(i)
    print(f"{k}\n")
    repeat()
##wrap this into a ini function

def ini():
    option = int(input("""\tMAIN MENU
------------------------------------
Vowels & Constants: 1
Pig Latin Translator: 2
------------------------------------
Enter Option: """))
    if (option==1):
        a = str(input("Calculate Vowels & Constants\nEnter Some Words: "))
        d = fOne(a)
        e = fTwo(a)
        print(f"Vowel Count is {d}, Const. Letter count is {e}\n")
        repeat()
    elif (option==2):
        f = str(input("Pig Latin Translator\nEnter Some Words: "))
        l = fThree(f)
    else:
        print("Invalid Option or Not currently an option I guess?")
ini()
    
