import random                   #import of the random module
number = random.randint(1,100)  #random integers in the range of 1 to 100 
import tkinter                  #import of built in GUI in python
window=tkinter.Tk()             #window for the GUI
window.title("Guessing Game")   #changing the default title of the window



def entry_button_check():            #user defined function for the check button

    for n in range(9):              # for loop used to limit the no of guess to 8 times
        
 
        user_guess=int(entry_1.get())     #get the integer of entry_1 value and assign it to variable user_guess
        
        if (user_guess)==number:          #first condition to check if the entry_1(user_guess) is same as the 
            
            msg="wow, you guessed correctly"  #statement to print
               
            

        elif user_guess>number:
            
             msg="Too high, try again.You guessed:"+ str(user_guess)
             
            
        elif user_guess<number:
            
            msg= "too low, try again.You guessed:" +str(user_guess)
     
        label_2["text"]=msg
        
        entry_1.delete(0,"end")
            

def clear():    #user defined function clear
    global number
    number = random.randint(1,100) #pick a random number
    label_2["text"]="Game reset!"
    entry_1.delete(0,"end")


#widgets used in the window
#labels

label_1=tkinter.Label(text="Welcome to Number Guessing Game.\n Guess a number between 1 and 100.",bg="pink",fg="black")
label_1.pack()

label_2=tkinter.Label(window,text="Enter your guess below",bg="DarkOrchid1",fg="black")
label_2.pack()


#entry widget

entry_1=tkinter.Entry(window,text="enter your guess")  #get input from a user
entry_1.pack()

#button widget

button_check=tkinter.Button(window,text="check",bg="violet",command=entry_button_check)
button_check.pack(side="top")

button_clear=tkinter.Button(window,text="clear",fg="red",bg="white", command=clear)
button_clear.pack(side="top")



window.configure(bg="DarkOrchid1")
tkinter.mainloop()

