def emogi_converter(message):
    words = message.split()
    emojis = {
        ":)": "\U0001F600",
        ":D": "\U0001F603"
    }
    output=""
    for word in words :
    output += emojis.get(word,word) + " "
    return output

message  = input("Enter message :)")
emogi_converter(message)



