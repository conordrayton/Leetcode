#reverse the given integer if its outside the range of integers than
#return 0




def reverse(x:int)->int:
    y=str(x) #convert integer to a string
    for i in y:
        if i[0]=='-':
            y=y.strip('-') #if index 0 is - then remove the negative
            z=y[::-1] # reverse the string
            y=int(z)*-1 # convert it back to an integer and make it negative again
        else:
            z=y[::-1] # reverse the string
            y=int(z) #convert back to integer
        if -2147483649 <= y <= 2147483647: # test that it falls in appropriate region
            return y
        else:
            return 0





poo=reverse(-12438575)
print(poo)