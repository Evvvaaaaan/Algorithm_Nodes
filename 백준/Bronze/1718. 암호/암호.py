plain_text = input() 
key = input()         

result = ''

for i in range(len(plain_text)):
    if plain_text[i] == ' ':
        result += ' '
    else:
        p_val = ord(plain_text[i]) - 97
       
        k_val = ord(key[i % len(key)]) - 97
        
        cipher_val = (p_val - k_val - 1) % 26
        
        result += chr(cipher_val + 97)

print(result)