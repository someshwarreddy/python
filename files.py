file = open('sample.txt')
print(file.read())
file.close()

# use with keyword opem file because python encounters exception handling to close file using close() method so use aviod that
with open("sample.txt") as file_object:
    documentt = file_object
    for line in documentt:
        '''prints the each word seprate line use rstrip() method combine words'''
      
        print(f"i am each line {line}")


with open("sample.txt", 'w') as file_object:
    document = file_object.write("hi am new file line")
    
with open("sample.txt" , 'a') as file_object:
    document = file_object.write("\ni am second new line")

with open("sample.txt" , "r") as file_object :
    document = file_object.read()
    print(document.rstrip())
import json

#  read 
jstring ='{"name":"somesh", "profession":"uidevloper and teaching"}'
jstringg ='{"name":"somesh", "profession":"uidevloper and teaching"}'
person = json.loads(jstring)
print(jstring)
print(type(person))

# write 

jstring ={"name":"somesh", "profession":"uidevloper and teaching"}

person = json.dumps(jstring)

print(person , type(person))


# open json file and write
data = {"name":"somesh", "profession":"uidevloper and teafgggdhing"}

with open("sample.json", "w") as json_file:
    json.dump(data, json_file)
    
with open("sample.json", "r") as json_file:
    readedData = json.load(json_file)
    print(readedData)
    

import os
import shutil



filename ="sample.txt"
    
try:
 with open(filename, encoding='utf-8') as f:
    contents = f.read()
except FileNotFoundError:
 print(f"Sorry, the file {filename} does not exist.")

else:
    # Count the approximate number of words in the file.
    words = contents.split() # creats the array of words split the words at space of from the selected string
    total_words = len(words)
    print(f"the {filename} have {total_words} words")
    
    
# multipul files   Failing Silently pass
def countwords(filename):
    try:
        with open(filename, encoding='utf-8') as f:
         contents = f.read()
    except FileNotFoundError:
        pass
        # print(f"Sorry, the file {filename} does not exist.")

    else:
    # Count the approximate number of words in the file.
        words = contents.split()
        total_words = len(words)
        print(f"the {filename} have {total_words} words")

filenamee = ['sample.txt', "one.txt"]       
for filnamee in filenamee:
    countwords(filnamee)
