a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

a = [1,2,3,4,5,6,7]
print("\n", a[0:1])
print("\n", a[1:3])
print("\n", a[3:8])
print("\n", a[2:5])
print("\n", a[-1])
print("\n", a[-1:1])
a[6] = "seven"
print(len(a))
a.append(8)
a.insert(7, "eight")
print("appended" , a)

for value in a:
    print(value)

# dictionaries    

b = {
    "name": "somesh",
    "city": "hyd"
}

print(b["name"])
print(b.keys())
for key in b:
    print(key)

#Lists Cannot Be Used as a Key but Tuples Can

    
