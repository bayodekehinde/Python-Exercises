#project 2: Text based adventure game
import time               #time module
import random             #random module
print("Haunted House\n There are 3 rooms in a house, some of them have been invaded by zombies. ")
time.sleep(3)
print("There are also some children trapped in the house.")
time.sleep(3)
print("You have to save the children. The rooms where the children are trapped is not known, you have to find them.")

            
def choose_room():
    '''this functions allows the player to chooose a room to start the "horror" adventure.'''

    room_no=int(input("Enter room to search '1','2',or '3' to search for the children and kill the zombies"))
    if room_no==1:
        room_no_1()
    if room_no==2:
        room_no_2()
    if room_no==3:
        room_no_3()
    
def room_no_1():
    '''This function is for activities in room number 1. 
    It takes one input from the player and the input decides where the player goes next.'''
    
    print("You are in room 1 and there are no children in this room. There are zombies in the room,press 's' to shoot or 'l'to leave room")
    action=input()
    
    if action=='s':
        print("You just killed two zombies. Enter 's' to shoot")
        print("You can now move to room 2")
        wait()
        print("\n")      #prints an empty line
        room_no_2()
        
    if action=="1":
        room_no_2()

def wait():
    '''This functions has no argument. It allows the program to wait foe 3 secons before moving to the next line of code'''
    time.sleep(3)
            
def room_no_2():
    '''This function has no argument. It defines the activities in room number 2.It makes use of the random module to pick a number
    between 2 and 4, the random number picked moves the player to another room.'''
    print("You are currently in room 2. \nOh, there are two children in this room. The room is very big and filled with garbage")
    time.sleep(2)
    
    #decision_2 takes input from the user to leave or seach the room
    decision_2=input("Press 's to search the room or 'e' to leave the room")
    if decision_2=='s':
        print("The room has clothes strewn all over the floor and food splattered all over the place. There is a bed at the left side of the room \n There is also a ladder in the room and wardrobes")
        wait()
        print("The room has a ladder,Press 'c' to climb the ladder and seach the roof")
        wait()
        print("Press  'w' to search the wardrobe")
        
        #search_room takes input from user to search a particular part of the room, the ceiling or wardrobe.This is only posssible when the user decides to search room 2
        
        search_room=input()
        if search_room=='c':
            print("Climbing the ladder...")
            for i in range(5):
                print("I-I")
                time.sleep(1)
                
            wait()
            print("You are presently above the ceiling. ")
            decision_2_c=input("Enter '1' to turn left or '2 ' to turn right")
            find_children=random.randint(1,2)
            if decision_2_c==find_children:
                wait()
                print("You just found the children")
                wait()
                print("Going down the ladder")
                for i in range(5):
                    print("I-I")
                    time.sleep(1)
                    print("Pick another room to search")
                choose_room()
                
            else:
                print("You lost the children. They have just been taken by the zombies to another room")
                wait()
                print("The zombies are behind you...Run")
                print("back to where you started")
                room_no_2()
                
        if search_room=='w':
            print("There are no children here")
            print("Search somewhere else")
            wait()
            choose_room()
            
   #decision to leave room 2              
    if decision_2=='e':
        print("Leaving room 2...")
        new_room=random.randint(2,3) #get random number between 2 and 3
        print(new_room)              #print the random number
        new_room1(new_room)          #go to function new_room with the random number as its argument.


 #function for room 3       
def room_no_3():
    '''This function describes the activities in room 3. '''
    
    print("You are currently in room 3. \n This  room is the biggest of all. \nIt has five children hidden in different parts. you have to check the wardrobes, cupboards,under the chair.")
    wait()
    print("You have only 3 decisions to make. Start your search now")
    count=0                #initilize count variable for counting the number of chilfren saved
  
    for i in range(4):     #This program can only run 3 times
        if count==5:       #checks if the children saved is equal to five
            print("You found all five of the children. Congrats.")
            print("*****")
            break           #go out of the loop if all 5 children are saved
        if i==3:            #checks if the program has ran 3 times
            print("Oooops,sorry,You cant search this room more than three times\nGame over")
            print("  0 0")
            print("   - ")
            break           #breaks the loop if it has an 3 times
        
        search_corner=random.randint(1,4)     #picks a random number betweem 1 and 4 inclusive
        #user_entry get inputs from the user
        user_entry=input("You have to search randomly around the corners of the room for the children. \n Enter corner: \n 1,2,3, or 4")
        
        wait()
        
        if user_entry==search_corner:      #checks if the random number is equal to the input of the user
            #decision_3 takes inpt from the user to search room 3
            decision_3=input("You picked the right cornner to search.\n press 'w' to search the wardrobe\n press 'c' to search the cupboard \n press 'd' to search behind the drapes,\n press 't' to search the toilet")
            print("enter w,c ,d, t")
            if decision_3=='w':
                print(".You just searched the wardrobe.There no children here. You can search other parts")
                continue                    #continue to the next line of code
            
            elif decision_3=="c":
                print("You just found two of  children. ")
                count+=2                    #increase the number saved children by 2
                if count<5:                 #checks if number of saved children are less than 5 
                    print("search another part of the room")
                    print("press 'w' to search the wardrobe \n \npress 'd' to search behind the drapes,\n press 't' to search the toilet")

            elif decision_3=="d":
                print("There are three zombies under the drape.")
                print("     They just bit you.\n You are dying...")
                time.sleep(5)
                print("Game Over")
                break
            elif  decision_3=="t":
                print("You just found three chidren.")
                count+=3                 #increase the number saved children by 3
                if count<5:
                    print("Search another part of the room for more children")
        else:
            print("You picked the wrong corner")
            choose_room() #calls choose_room() function to start again
            

def new_room1(new_room):
    '''This fuction takes one argument . The function calls other functions'''
    if new_room==3:
        room_no_3()
    elif new_room==1:
        room_no_1()
    elif new_room==2:
        print("You are still in room 2")
        room_no_2()
        
        
        
    
            
start_game=input('press "s" to start the game')          #start the game

if start_game=="s":
    choose_room()                                       #call the choose_room function to chooose a room

    
