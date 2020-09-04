#Yingxuan Wang
#Palinadrome

Alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Digit='0123456789'

def Valid_Palindrome(str):
    #input validation
    if type(str)!=str:
        raise TypeError("Your input should be a string.")
    if str=="":
        return True
    
    new_str='' #store valid information
    count=0 #for judging if the string is a palindrome
    for element in str:
        #convert all the elements
        element=element.upper()
        #get rid of all non-letters and non-digits
        if element in Alphabet or element in Digit:
            new_str+=element
    #compare the first letter in the string with the last one and so forth
    for i in range(len(new_str)):
        if new_str[i] == new_str[-(i+1)]:
            #check condition
            count=0
        else:
            count+=1
            break
    if count==0:
        return True
    else:
        return False