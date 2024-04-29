#a -> @
#A -> 4
#B, b -> 8
#E, e -> 3
#I, i -> !
#L, l -> 1
#O, o -> 0
#S, s -> 5
#Create a function convert(text: str) -> str that accepts a string, 
#converts the string to leet speak using the conversion table above, and returns the converted string. 
#No other changes should be made to the string.
text = "lab"
def convert(text: str) -> str:
    leet_dict = {
        "a" : "@",
        "A" : "4",
        "B" : "8", 
        "b" : "8",
        "E" : "3", 
        "e" : "3",
        "I" : "!", 
        "i" : "!",
        "L" : "1",
        "l" : "1",
        "O" : "0", 
        "o" : "0",
        "S" : "5", 
        "s" : "5",
    }
    converted_text = ""   
    for char in text:
        if char in leet_dict:
            converted_char = leet_dict[char]
        else:
            converted_char = char
        converted_text += converted_char
    
    return converted_text

print(convert(text)) 
    
