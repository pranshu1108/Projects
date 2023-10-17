#Take Password input from the user

strings = str(input())

#Criteria

Caps_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
Symbols = ['!', '@', '#', '$', '%', '^', '&', '*']


havingblank = 0
count = 0
index = 0
criteria_passed = 0
for i in strings:
    count += 1
if count > 8:
    criteria_passed += 1
else:
    print("Password Invalid : Length is not greater than 8 characters")
for j in strings:
    if j[0] in Caps_letters:
        criteria_passed += 1
        break
else:
    print("Password Invalid: No Uppercase character found")

while index < count:
    if (strings[index] == ' '):
        havingblank = 1
        break
    index += 1

if (havingblank == 0):
    criteria_passed += 1
else:
    print("Password Invalid : It contains a blank space")
for k in strings:
    if k in Numbers:
        criteria_passed += 1
        break
else:
    print("Password Invalid : Not alphanumberic")
for l in strings:
    if l in Symbols:
        criteria_passed += 1
        break
else:
    print("Password Invalid : No special character")

print(f"Total Criteria Passed:  {criteria_passed} /5")