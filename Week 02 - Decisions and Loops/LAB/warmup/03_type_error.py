# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: ")) #Added the int converter as relative operators cannot be used with strings

if value > limit:
    print("OVER")
else:
    print("OK")
