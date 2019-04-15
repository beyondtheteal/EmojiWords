from letter_functions import * 

# 1. Take an input, a string, of what you want to write
# 2. Take an emoji for the content of those words
# 3. Take an emoji for the space :space: or :empty:
# Print that string with that emoji

# Print the letter T as emoji :egg:
# 5 px letters
height = 5 -1

# Change all the cryptic 0s and 1s below into the actual emoji requested
def collate(seq): 
    seq = seq.replace("0", ":space:")
    seq = seq.replace("1", ":shed:")
    return seq

def completePrint(word): 
    word.upper # make it all caps, just in case
    print(collateString(word))

# Print the text as a printer would, one complete line at a time from top to bottom
def collateString(word): 
    string = ""
    row = 0

    # Loop through 
    while row <= height:
        string += "\n" #Put a line break at the end of each line
        for c in word:
            func = caps_functions[c]
            string += collate(func(row))
            string += collate(kerning())

        row+=1
    
    return string

    # Try 1
    # printOut(func(1))
    # printOut(func(2))
    # printOut(func(3))
    # printOut(func(4))
    # printOut(func(5))


caps_functions = {
    ' ': load_space,
    'A': load_A,
    'B': load_B,
    'C': load_C,
    'D': load_D,
    'T': load_T }

completePrint("BAD CAT BAD")


    # Try 3
    # if row == 1:
    #     return """010"""
    # elif row == 2:
    #     return """101"""
    # elif row == 3: 
    #     return """111"""
    # elif row == 4: 
    #     return """101"""
    # elif row == 5: 
    #     return """101"""
    # else: 
    #     return """010\n101\n111\n101"""

    # Try 2
    # l = """010\n101\n111\n101"""
    # l = l.replace("0", ":space:")
    # l = l.replace("1", ":sweat:")
    # print(l)
    
    # Try 1
    # print(":space::sweat::space:")
    # print(":sweat::space::sweat:")
    # print(":sweat::sweat::sweat:")
    # print(":sweat::space::sweat:")