
def emojie_converter(message):  #defining the system of code of converter                                                   

    words = message.split(" ")   #splliting eaxh word to use it in FOR loop
    emojis = {       #dictionary
        ':)':"😀",
        ':(': '😭'
    }

    output = ''
    for word in words:                  #go through each word one by one in words
        output += emojis.get(word , word) + " "   #keep adding message in output,If in dic then change if not retuen as it is
    return output   #use RETURN to use the output again


message = input ("> ")    
result = emojie_converter(message)    #we could also write print(emojie_converter(message))
print(result)

#we wrote the whole emoji converter thing to use to again anytime! made it a reusable function 