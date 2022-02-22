          #Random Module 
# import random 
# random_int = random.randint(1, 50)     
# print(random_int)      
#The code that written above gives the random integer everytime we run the code.

# import random
# random_float = random.random()
# print(random_float)
#The code that written above gives the random floating number between [0 to 1) where 1 not included ofc everytime we run the code.
# Now if you want to expand the range from 0 to 1 to 0 to whatever number you want you just have to do this...
# import random 
# ran_float = random.random() * 5
# print(ran_float)
# so its range gonna be from 
# 0.000... - 4.9999...

#               Note:-
# You can import a file to the code. suppose you have a file other than "main.py" and u make another file suppose "Uza.py" then if u want to add "Uza.py" things in "main.py" U simply have to use (import) like, import Uza.py and then to print the stament if u want to print for example then type print(Uza.pi) if suppose u added pi = 3.24 there in Uza.py. 
# Example:-
# import Uza
# print(Uza.pi)

#A dice without any animation:-
# import random 
# Ran = random.randint(1, 6)
# print(f"Dice Facing:\n{Ran}")

  #Offset and Appending Items to Lists
                #List
# Suppose u wanna store lots of things in one variable only, like 1+1, 3+4, ..... alll in one variable then we can do it like this:-
# Varible = [list1, list2, list3, ...]
#Example:-
# Indian_Places = ["Bihar", "Assam" ,"up", "mp"]
# print(Indian_Places)
# and if u wanna check the order:-
# print(Indian_Places[0])
# line 37 used [] inside bracket knowns as index.
# now we wanna count from forward... we can use positive index inside [] like 0,9,7,5... but if we wanna count from the backward then we should use _ve Index inside [] like -1,-8,-4,...
# print(Indian_Places[-2])
# Now suppose you wanna add an item to the end of the list we can do it like:-
# Indian_Places.append("Uzalund")
# print(Indian_Places[-1])
# To add one than many items in the end of list we can write code like:-
# Indian_Places.extend(["Uzaland", "Hazelland", "RiriLand"])
# print(Indian_Places)

#IndexErrors and Working with Nested Lists
            #Nested list:-
# Suppose we have fruits and veggies in one group but we wanna seperarte it, we can do it like:-
# Fruits = ["apple", "guava", "Mango"]   
# Veggies = ["Potato", "Tomato", "Beans"]  
# T = [Fruits, Veggies]
# print(T)  

            #Quiz Example1
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# fruits[-1] = "Melons"
# fruits.append("Lemons")
# print(fruits)     
#adding (fruits[-1] = "Melons") to the list will replace the item that was first there to the one it was replaced with. means at positon of index [-1] there was "pears" before, but after writting fruits[-1] = "Melons" it will change to "Melons" and the output that we will get it "Melons" at the place of index [-1].

          #Quiz Example2
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]
 
# print(dirty_dozen[1][1])
# here, [1] will print (Vegetables), then again [1][1] will print thing in vegetable at index [1] place in vegetables there is "kale".

             #Example2(Bank)
             #Method1:-
# import random

# # Split string method
# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")

# #Write your code below this line 👇

# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")

#            #Method 2:-(Easy)

# import random

# names_string = input("Give me everybody's names, seperated by a comma. ")
# names = names_string.split(", ")
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is going to buy the meal today!")



              