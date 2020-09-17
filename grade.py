#grade

grade=[]                                #creates an empty list
while True:                             #infinite loop for the grade program.
    
    print("1-> Enter grade:\n")
    print("2-> List grades:\n")
    print("3-> clear all grades:\n")
    print("4-> Delete grade:\n")
    print("5-> Update grade:\n")
    print("6-> Calculate average grade:\n")
    print("7-> Exit programme:\n")
    choice=input("Enter choice:\n")        #user inputs choice of what to do from the above print statemnts
    
    #conditions for the iput of choice
    if not( len(choice)==1 and choice.isnumeric() and int(choice)<8):
        print("input is invalid. Enter a valid choice")
    
    
    if int(choice)==7:                #break the infinite loop if choice equal 7
        break
    if int (choice)==1:               #start another sub loop if choice eqaul 1
        while True:
            grades=input("Enter grades of different subjects and press 'e' to exit:\n")
           
            if grades=='e':
                break               #break loop if grades eqaul e
            grades=float(grades)    #convert the string to float data type
            grade.append(grades)    #add the grades to the list grade
        print(grade,"\n")                #print the list
        
    if int(choice)==2:
        print(grade)
        print("\n")                   #space for readability
        
    if int(choice)==3:
        grade.clear()                             #clear all elemets in the list
        print("\n")
        
    if int(choice)==4:
        e_list=enumerate(grade)                    #enumerate the list
        for i,grades in e_list:                    #for loop to iterate index and grade
            print("index:",i,"grades:",grades)     #print index with corresponding grade
            print("\n")
            
        index= int(input("Enter index of grade to delete:"))
        grade.pop(index)                           #delete grade with specified index
        print("grade=",grade)
        print("\n")
    
    if int(choice)==5:
        e_list=enumerate(grade)
        for i,grades in e_list:
            print("index:",i,"grades:",grades)
            
        new_grade=float(input("Enter grade to update to:"))
        index_1=int(input("Enter the index of the grade:"))
        grade[index_1]=new_grade                    #update the grade to a new grade with specified index
        print(grade)
        print("\n")
        
    if int(choice)==6:
        sum1=0
        for element in grade:                       #for loop for getting each element from the list-grade
            sum1=sum1+ element                      #sum all elements
        avg=sum1/len(grade)                         #function to calculate average
        print("The average of the grade is:", avg)  #prints average
        
       
        
