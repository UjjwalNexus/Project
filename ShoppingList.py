Shopping_List=[]
print("Enter \'a\' to add item in list    ,     \'r\' to remove an item from the list   ,    \'v\' to view the Current List and  \'s\' to stop ")
c = ""


while True:
    c= input("Enter Your Choice :")
    if c== "a" or c== "A":
        add = input ("Enter The Item you want to add : ")
        Shopping_List.append(add)

    elif c== "r" or c== "R":
        rem=  input ("Enter The Item you want to remove : ")
        Shopping_List.remove(rem)

    elif c== "v" or c=="V":
        print(Shopping_List)
        
    elif c== "s" or c== "S":
        break

print("Your final Shopping list is :")
print(Shopping_List)
    

    
