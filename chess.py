#This programs gives the color of the position of a square on a chess board
#the program requires the user to enter the column and the row
column=int(input("column:")) #enter column
row=input('row:')            #enter row

#checks for postion in row a
if row=='a' and column%2==1:
    print('black')
elif row=='a' and column%2==0:
    print('this sqare is white ')
    
#checks for postion in row b
    
elif row=='b' and column%2==0:
    print(row,column, 'is black ')
elif row=='b' and column%2==1:
    print('The Square is white ')

#checks for position in row c

elif row=='c' and column%2==1:
    print(row,column, 'is black ')
elif row=='c' and column%2==0:
    print(row,column, 'is white ')

#checks for position in row d
elif row=='d' and column%2==1:
    print(row,column, 'is white ')
elif row=='d' and column%2==0:
    print(row,column, 'is black ')

#checks for position in row e

elif row=='e' and column%2==1:
    print(row,column, 'is black')
elif row=='e' and column%2==0:
    print(row,column, 'is white')

#checks for position in row f

elif row=='f' and column%2==1:
    print(row,column, 'is white')
elif row=='f' and column%2==0:
    print(row,column, 'is black')

#checks for position in row g
    
elif row=='g' and column%2==1:
    print(row,column, 'is black')
elif row=='g' and column%2==0:
    print(row,column, 'is white')

#checks for position in row h
    
elif row=='h' and column%2==1:
    print(row,column, 'is white')
elif row=='h' and column%2==0:
    print(row,column, 'is black')

    
else:
    print(row,column, ' is invalid')

