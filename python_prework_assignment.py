#Question 1: 
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

def hello_name(user_name):
    print ("Hello, " + user_name.title() + "!")
hello_name ("David")



#Question 2: 
# #Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    
    for i in range (1, 100+1,2):
        if i %2 != 0:
            print ("\n", i,end="")

first_odds ()



#Question 3:
# Write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list (a_list):
    max = a_list [0]
    for a in a_list:
       if a > max:
           max=a
    return max
    
print ("\n",max_num_in_list([32,-5,0,14,26]))



#Question 4:
#Write a function to return if the given year is a leap year.

def is_leap_year (a_year):
    
    if (a_year%4 == 0 and a_year%100 != 0):
        print(a_year, "is a leap year.")
    elif (a_year%400 == 0):
        print(a_year, "is a leap year.")
    else :
        print(a_year, "is not a leap year.")

is_leap_year(2021)



#Question 5:
#Write a function to check to see if all numbers in list are consecutive numbers.


def is_consecutive (a_list):
    if len(a_list) < 1: 
        return False
    
    min_num_in_list = min(a_list)
    max_num_in_list = max(a_list)

    if max_num_in_list - min_num_in_list + 1 == len(a_list):
        for i in range (len(a_list)):
            if a_list [i] < 0:
                j = -a_list - min_num_in_list
            else:
                j = a_list [i] - min_num_in_list
                if a_list [j] > 0:
                    a_list [j] = -a_list[j]
                else:
                    return False
            return True
    return False

a_list = [9,5,7,6,8]
print (is_consecutive (a_list))


    

