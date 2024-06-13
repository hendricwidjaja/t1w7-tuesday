# Leetcode Challenge #796 - Rotate String

# Grab input for "s" string
s = input("What should 's' equal? ")

# Grab input for "goal" string
goal = input("What should 'goal' equal? ")

# Initialise shift count and create a variable to account for amount of characters in s
shift_count = 0
s_count = len(s)
# LOOP for len of characters and compare to variable called shift_count
while shift_count < s_count:
    if s == goal:
        print(s)
    else:
        character_shift = 


# IF s equals goal, print result
# If not, "shift" s string by moving 1st index to last index
# Stop loop once len of characters i