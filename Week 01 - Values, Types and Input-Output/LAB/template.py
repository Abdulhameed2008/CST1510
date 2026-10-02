"""
RECORD CHECK  -  my version
===========================

Name  :
Lane  :  AI       (delete two)
Date  :

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

label = input("Enter Dataset Name: ")      # : replace with an input() call
first = float(input("Enter rows loaded: "))    # : replace with an input() call, converted
second = float(input("Enter Rows Expected: "))   # : replace with an input() call, converted
duplicates = float(input("Enter Number of Duplicates found if any: ")) 
# This is the extra line of my own that I decided to add because of the sheer number of duplicates that one finds when going through Data.


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = first - second   # because this shows the difference between rows loaded and rows expected
percent = (first/second) * 100      #second will be the denominator because rows expected will usually be higher than rows loaded.


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

r = "Rows loaded"
r2 = "Rows Expected"
d = "Difference"
p = "Percent" 
d2 = "Duplicates"

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here
print(f"{r:<20}:{first:>10.2f} \n{r2:<20}:{second:>10.2f} \n{d:<20}:{difference:>+10.2f} \n{p:<20}:{percent:>10.2f} % \n{d2:<20}:{duplicates:>10.2f} ")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
