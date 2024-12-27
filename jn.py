import json

try:
  
    with open("sample.json", "r") as fj:
        contents = json.load(fj)
        print(contents)
except FileNotFoundError:
        print("json file not avialable")
        
def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
            if len(username) == 0:
                username = input("What is your name? ")
                with open(filename, 'w') as f:
                    json.dump(username, f)
                    print(f"We'll remember you when you come back, {username}!")
    except FileNotFoundError:
            return None
    else:
      
        with open('sample.json','w') as f:
            contents[ 'age' ] = '28'
            json.dump(contents, f, indent=4)
            print(contents)
        print(f"Welcome back, {username}!")
greet_user()
