

##def fun(l1,l2):
##    l1.append('programming')
##    l2=l1
##    print('l1 inside function',l1)
##    print('l2 inside function',l2)
##
##l1=['Python']
##l2=['R']
##fun(l1,l2)
##
##print('l1 outside function',l1)
##print('l2 outside function',l2)
"""
##---------------------------------------------------------

###The parameter mylist is local to the function changeme.
###Changing mylist within the function does not affect mylist.
##
##def changeme(mylist):
##    mylist=50
##    print('value inside function',mylist)
##    return
##
##mylist=100;
##changeme(mylist);
##print('value outside function',mylist)

#---------------------------------------------------------
"""
#All parameters (arguments) in the Python language are passed by reference.
#It means if you change what a parameter refers to within
#a function, the change also reflects back in the calling function.
#Here, we are maintaining reference of the passed object and
# appending values in the same object.

##def changeme( mylist ):
##   "This changes a passed list into this function"
##   mylist.append([1,2,3,4]);
##   print ("Values inside the function: ", mylist)
##   return
##
### Now you can call changeme function
##mylist = [10,20,30];
##changeme( mylist );
##print ("Values outside the function: ", mylist)
##---------------------------------------------------------

##total = 0; # This is global variable.
### Function definition is here
##def sum( arg1, arg2 ):
##   # Add both the parameters and return them."
##   total = arg1 + arg2; # Here total is local variable.
##   print( "Inside the function local total : ", total)
##   return
##
### Now you can call sum function
##sum( 10, 20 );
##print ("Outside the function global total : ", total )
##--------------------------------------------------------------

##Keyword arguments must follow non-keyword(positional) arguments
##def printinfo( arg1, *arg2 ):
##   "This prints a variable passed arguments"
##   print ("Output is: ")
##   print(arg1)
##   
##   for var in arg2:
##      print (var)
##   return;
##
### Now you can call printinfo function
##printinfo( 10 )
##printinfo( 70, 60, 50 )
##------------------------------------------

##def fun_dep(*args):
##    sum=0
##    for i in args:
##        sum+=i
##    print('total deposit',sum)
##
##fun_dep(100,210,300)
##fun_dep(45,87,98,65,32,754)
##-------------------------------------

##def fun_dep(id,name,*m,**d):
##    print(id,name,m,d)
##
##dict1={'mob':'344'}
##dict2={'mob1':'588','mob2':'599'}
##
##fun_dep(100,'Suren',10,45,65,75,**dict1)
##fun_dep(101,'Minu',45,87,98,65,32,754,**dict2)

##-------------------------------------------------

##Keyword arguments are related to the function calls.
##When you use keyword arguments in a function call,
##the caller identifies the arguments by the parameter name.

##def printme( str ):
##   "This prints a passed string into this function"
##   print( str)
##   return;
##
### Now you can call printme function
##printme( str = "My string")
##-----------------------------------------------

##def printinfo( name, age ):
##   "This prints a passed info into this function"
##   print ("Name: ", name)
##   print ("Age ", age)
##   return
##
### Now you can call printinfo function
##printinfo( age=50, name="miki" )
#------------------------------------------------

##Always non-default(constants) arguments must follow default arguments
##def printinfo( name, age=35 ):
##   "This prints a passed info into this function"
##   print( "Name: ", name)
##   print ("Age ", age)
##   return;
##
### Now you can call printinfo function
##printinfo( age=50, name="miki" )
##printinfo( "miki" )
##----------------------------------------------
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)

