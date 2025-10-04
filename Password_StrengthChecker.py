#for getting user input password
password = input( "Enter your password: ").strip()
#for checking symbols are contain in password or not
symbols = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
#for counting password strength
points = 0

#for checking every strength condition of passwords
has_lower=False
has_upper=False
has_number=False
has_symbol=False

#for checking length of password and for checking conditions and adding points
if len(password)>4:
    if len(password)>=5 and len(password)<8:
        points+=1
    elif len(password)>=8 and len(password)<12:
        points+=2
    elif len(password)>=12 :
        points+=4
    for i in password:
        if not has_lower and i.islower():
            points += 1
            has_lower=True
        elif not has_upper and i.isupper():
            points +=1
            has_upper=True
        elif not has_number and i.isdigit():
            points+=1
            has_number=True
        elif not has_symbol and i in symbols:
            points+=1
            has_symbol=True
else :
    print("Password must contain 5 characters..")

#dictionary of common passwords
common_passwords = [
    "123456", "123456789", "qwerty", "password", "abc123",
    "111111", "123123", "letmein", "welcome", "admin",
    "monkey", "1234", "12345", "iloveyou", "football"
]

#for checking common password
if password.lower() in common_passwords:
    print("Your password is common password easy to intercept.")
else:
    points+=2


#condition checking strength according to points
if points == 10 :
    print("Very Strong Password")
elif points>=8 and points <10:
    print("Strong Password")
elif points>=5 and points <8:
    print("Good Password")
else :
    print("Weak Password")


