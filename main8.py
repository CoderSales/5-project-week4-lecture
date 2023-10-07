"""
4 test cases needed:
1. #
2. 1
3. done
4. <anything else>

This program takes user input, as string
and prints some message based on the input
entering done, makes the while loop end
and finally the program prints:
Done!
"""

while True:
    line = input('enter some text > ')
    if line == '#':
        continue
    if line == '1' :
        print("you entered 1")
        continue
    if line == 'done':
        break
    print("hello world")
print("Done!")