a = 200+2
print(a)
50 - 5*6
8 / 5  # division always returns a floating point number
17 / 3  # classic division returns a float
17 % 3  # the % operator returns the remainder of the division
5 * 3 + 2  # floored quotient * divisor + remainder
5 ** 2  # 5 squared
2 ** 7  # 2 to the power of 7
word = 'Python'
word[0]  # character in position 0

word[5]  # character in position 5
word[-1]  # last character

word[-2]  # second-last character

word[-6]
word[0:2]  # characters from position 0 (included) to 2 (excluded)

word[2:5]  # characters from position 2 (included) to 5 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)

word[4:]   # characters from position 4 (included) to the end

word[-2:]  # characters from the second-last (included) to the end
word[:2] + word[2:]

word[:4] + word[4:]
'J' + word[1:]
'Jython'
word[:2] + 'py'
'Pypy'

s = 'supercalifragilisticexpialidocious'
len(s)
34

# Lists

squares = [1, 4, 9, 16, 25]
squares
[1, 4, 9, 16, 25]
squares[0]  # indexing returns the item
1
squares[-1]
25
squares[-3:]  # slicing returns a new list
[9, 16, 25]

squares[:]
[1, 4, 9, 16, 25]
squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
64
cubes[3] = 64  # replace the wrong value
cubes
[1, 8, 27, 64, 125]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters