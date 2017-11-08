secret = int("8")

guess = int(raw_input("Enter the value for guess: "))
print guess

if guess == secret:
    print "CONGRATULATIONS. YOU'VE WON !!!"

else:
    print "Please try again."
