import string

def encode(chars, number):

    i = chars[number] + "-za-" + chars[number-1]
    caps = input("both cases? (y/n)")
    if caps == ("y"):
        
        return "tr '[A-Za-z]' '[" + i.upper() + i +"]'"
            
    elif caps == ("n"): 
        return "tr '[a-z]' '[" + i + "]'"


lower = string.ascii_lowercase

usr_input = input("encode (e), or decode(d) ? ")
usr_int = int(input("how much? "))

if usr_input == "e":
    print(encode(lower,usr_int))

elif usr_input == "d":
    print(encode(lower,26-usr_int))
