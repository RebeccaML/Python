# Challenge found here: http://www.pythonchallenge.com/pc/def/equality.html
# Read a file and look for a lowercase letter with three uppercase
# letters on either side.
# In progress... there might be a better way to do this

file = open("pc#3.txt")
file_string = file.read()
length = len(file_string) # Get the length of the string to use range
result = "" # Put matching letters in a string for readability

# Don't look at the first 3 or the last 3 chars because they can't be the answer
for i in range(3, length-2):
    if file_string[i].islower():
        if file_string[i-3: i].isupper() and file_string[i-4].islower():
            if file_string[i+1: i+4].isupper() and file_string[i+4].islower():
                result += file_string[i]
print(result)