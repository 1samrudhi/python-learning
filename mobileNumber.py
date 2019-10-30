mobile_number = input("Enter mobile number:")
joined = ''
split_array = list(mobile_number)

for digit in split_array:
    print(digit)
    if digit == '1':
        joined +="ONE "
    elif digit == '2':
        joined += "TWO "
    elif digit == '3':
        joined += "THREE "
    elif digit == '4':
        joined += "FOUR "
    elif digit == '5':
        joined += "FIVE "
    elif digit == '6':
        joined += "SIX "
    elif digit == '7':
        joined += "SEVEN "
    elif digit == '8':
        joined += "EIGHT "
    elif digit == '9':
        joined += "NINE "
    elif digit == '0':
        joined += "ZERO "
print(joined)

