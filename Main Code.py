import random

file = open("Word List.txt","r+")
full_list = file.readlines()
grid7 = []
grid9 = []
grid12 = []
w_list7 = []   #Defining Variables needed in the entire game, and importing file
w_list9 = []
w_list12 = []

def orientation(z, word_list, word_length, r_column, r_row, length, current_rc, difficulty, used_words, used_rc, r_orientation, place_holder, endX):
    endY = True    #this is a function that can be used for any of the 4 rotations of words, left, right, up, or down.

    if r_orientation == 1:
        if ((word_length + r_column) >= length):
            endY = False
    elif r_orientation == 2:
        if ((r_column - word_length) < 0):   #because each different orientation needs to be checked if it fits a different way i use an
            endY = False                     #if statement with each different arrangment of code in it, i use this once more in this function
    elif r_orientation == 3:
        if ((word_length + r_row) >= length):
            endY = False
    elif r_orientation == 4:
        if ((r_row - word_length) < 0):
            endY = False
    if endY == True:
        for i in range(word_length):
            if r_orientation == 1:
                current_rc2 = [r_row,r_column + place_holder]
                current_rc.append(current_rc2)
            elif r_orientation == 2:
                current_rc2 = [r_row, r_column - place_holder] #This code creates a 2D list full of every coordinate of every letter in the current word. Different logic is needed
                current_rc.append(current_rc2)                  #for each orientation so it is repeated 4 times
            elif r_orientation == 3:
                current_rc2 = [r_row + place_holder, r_column]
                current_rc.append(current_rc2)
            elif r_orientation == 4:
                current_rc2 = [r_row - place_holder, r_column]
                current_rc.append(current_rc2)
            place_holder = place_holder + 1
        for i in used_rc:
            for x in current_rc:    #this checks every coordinate of every letter in the current word with every coordinate of every letter in every other word
                if x == i:
                    endX = 1
        if endX == 0:
            for i in range(word_length):
                if (r_orientation == 1) or (r_orientation == 2):
                    difficulty[r_row][int(current_rc[i][1])] = used_words[z][i]     #this adds the current word into the overall grid
                elif (r_orientation == 3) or (r_orientation == 4):                  #different logic is needed for up and down, and left and right so it is in an if statement like before
                    difficulty[int(current_rc[i][0])][r_column] = used_words[z][i]  #although only 2 if statements are needed
            for i in current_rc:
                used_rc.append(i)
            word_list.append(used_words[z]) #creates a list with all words then ended up getting used in the word search

def filler(difficulty):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y = -1
    for i in difficulty:
        y += 1              #this function fills every spot in the word search that hasnt been filled with a word with a random letter
        w = -1              #it used 4 letters, because two are the actual lists and two are number keeping track of which list it is
        for x in i:
            w += 1
            if x == " ":
                difficulty[y][w] = alphabet[random.randint(0, 25)]

def search_creator(length, difficulty, word_num, word_list):
    used_rc = []            #this fucntion is what creates the word search, it has two other functions embeded in it.
    used_words = []
    loop_length = 1 #variables needed throughout all functions
    z = -1

    for i in range(length):
        difficulty.append([])       #creates an emtpy square grid of any size
        for x in range(length):
            difficulty[i].append(" ")

    while loop_length == 1: #this is a while loop because i only want the loop to end after all words are fit into the word search
        z+=1                #and each time the loop runs there is no gaurentee a word will be added
        place_holder = 0
        current_rc = []
        r_word = random.randint(0, 42962)
        r_row = random.randint(0, length - 1)
        r_column = random.randint(0, length - 1)   #these are all the numbers that randomly generate the grid, so the word search isnt the same every time
        r_orientation = random.randint(1,4)
        used_words.append(full_list[r_word].strip("\n"))
        word_length = len(used_words[z])
        endX = 0
        orientation(z, word_list, word_length, r_column, r_row, length, current_rc, difficulty, used_words, used_rc, r_orientation, place_holder, endX)
        if len(word_list) >= word_num: #this checks if all words needed have been added, if they are the while loop ends.
            loop_length = 0
    filler(difficulty)

def search_printer(grid):
    print_list = []
    for i in grid:
        print_str = ""      #this function prints out the word search in a way that makes it look nice
        for x in i:                             #it essentialy takes the 2D list and turns it into a 1D list.
            print_str = print_str + x + "  "    #so every letter that would have been in a list within the bigger list
        print_list.append(print_str)            #gets added to a string with all the other letters that where in its list
                                                #and a space is added to make it look nice
    print("Here is your WordSearch: ")
    for i in print_list:
        print(i)

def gameplay(word_list, word_num):  #this function is where the actual game happens.
    print("Here are the list of words you will find in your WordSearch: ")
    for i in word_list:
        print(i)        #this prints out all words that can be found in the word search
    words_found = 0
    while words_found != word_num: #a while loop that wont end until all words are found
        word_correct = False
        word_guess = input("Guess A Word: ")
        for i in range(len(word_list)):
            if word_guess == word_list[i]:  #after the user guesses, this checks the users guess against all word options
                word_correct = True         #the if statement is outside of the forloop because if it wasnt, even if your answer is correct
        if word_correct == True:            #the try again will print everytime expect the one where your answer matches.
            words_found += 1
            word_list.remove(word_guess)
            print(str(words_found) + "/" + str(word_num) + "Words Found")
        else:
            print("Word Incorrect, Try Again!")
    print("YOU WON!")
    keep_going = input("Input 1 to Keep Playing, Or 2 To Quit: ")
    if int(keep_going) == 2:
        exit("Thanks For Playing!")

print("Welcome to Word Search.\nTo Play Just Enter Words You Think You See In The Grid.\nGet Them All And You Win!")
print("Remember to type in UpperCase.\nAlright, Have Fun!")
while 1 == 1: #here is the main for loop of the game
    user_diff = int(input("Enter 1 For Easy, 2 For Medium, 3 For Hard, and 4 to Exit: "))

    if user_diff == 1:
        search_creator(7, grid7, 7, w_list7)        #all the functions are called, with specific parameters for the difficulty
        search_printer(grid7)
        gameplay(w_list7, 7)
    elif user_diff == 2:
        search_creator(9, grid9, 10, w_list9)
        search_printer(grid9)
        gameplay(w_list9, 10)
    elif user_diff == 3:
        search_creator(12, grid12, 15, w_list12)
        search_printer(grid12)
        gameplay(w_list12, 15)
    else:
        exit("Thanks For Playing!")