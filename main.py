#So this is how you put python codes and run!
# First we are going to make a password contained in a variable!


x="hello"
#hello is my password.

y=raw_input("What is your Username:")
#raw_inout is basically prompting a user to answer a question.

if y=="Sooraj" or y=="Sooraj":
    print("Hello Sooraj!")
    d=raw_input("What is your password Sooraj:")
    if d==x:
        print ("Welcome back Sooraj!!")
    else:
        while not d==x:
            print("Help!! I am being Hacked!!")
            d=raw_input("What is your password Sooraj:")
            if d==x:
                print ("Welcome back Sooraj!!")

else:
    while not y=="Sooraj" and (not y=="Sooraj"):
        print "I dont know you!"
        y=raw_input("What is your Username:")


if y=="Sooraj" or y=="Sooraj":
    print("Hello Sooraj!")
    d=raw_input("What is your password Sooraj:")
    if d==x:
        print ("Welcome back Sooraj!!")
    else:
        while not d==x:
            print("Help!! I am being Hacked!!")
            d=raw_input("What is your password Sooraj:")
            if d==x:
                print ("Welcome back Sooraj!!")


#So this is the code to make an authentication system.

#and means that both the conditions should be true!

                #Now lets run it.
