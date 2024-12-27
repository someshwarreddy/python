#python interpreats everything as string
enterValue = input("enter something:")
print(f"you entered \n{enterValue}")

# enterValue = int(enterValue)
# enterValue > 10

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
# while message != 'quit':
    #  message = input(prompt)
    #  print(message)
    
active = True
while active:
    message = input(prompt)
 
    if message == 'quit':
        # active = False
        break
    else:
        print(message)