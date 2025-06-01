#pattern_drawing.py

#Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern:"))

#Initialize row counter
row = 0

#Loop through rows using while loop
while row < size:
    #Loop through columns using for loop
    for col in range(size):
        print("*",end="")
        print() #move to the next line after each row
        row += 1
