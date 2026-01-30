s = input()

newS = ''
for char in s:

    if char.isupper():

        new_char = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        newS += new_char
        

    elif char.islower():

        new_char = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        newS += new_char
        
    else:
        newS += char

print(newS)