string_input=input ("enter a string")
char_input=input("enter a char")
count=0
for char in string_input:
    if char==char_input:
        count+=1
print(f"the char {char_input} shows {count} times")
