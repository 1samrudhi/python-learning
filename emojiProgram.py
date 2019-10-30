message = input("Enter message :)")
words = message.split()

emojis = {
    ":)": "\U0001F600",
    ":D": "\U0001F603"
}
output=""
for word in words :
    output += emojis.get(word,word) + " "
print(output)
