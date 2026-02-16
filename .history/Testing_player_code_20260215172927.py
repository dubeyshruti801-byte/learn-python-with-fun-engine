#questionlevel1.py — Player Code
#Q1
print("shruti")

#Q2
print(["Deepak", "Priya", "Dimple"])

#Q3
print(["Apple", "Banana", "Mango", "Orange", "Grapes"])

#Q4
print(["January", "February", "March", "April", "May", "June", "July",
       "August", "September", "October", "November", "December"])

#Q5
print(["Monday", "Tuesday", "Wednesday", "Thursday", 
       "Friday", "Saturday", "Sunday"])


'''✔ requires_print = True
✔ no input
✔ no collection requirement
✔ no variables
✔ no loop'''

'''questionlevel2.py — Player Code
Q1

(require input, 1 variable, print)'''
a = input()
print(a)
'''✔ requires_input
✔ min_variables = 1'''

#Q2(require list, variable name 'num', no loop required)
num = []

num.append(input())
num.append(input())
num.append(input())
num.append(input())
num.append(input())
num.append(input())
num.append(input())
num.append(input())
num.append(input())
num.append(input())

print(num)
'''✔ requires_collection = list
✔ variable name = num
✔ no loop (since requires_loop = False)
✔ matches expected output format'''

#Q3(variable name 'even')

even = []

even.append(input())
even.append(input())
even.append(input())
even.append(input())
even.append(input())

print(even)

#Q4(variable name 'odd')

odd = []

odd.append(input())
odd.append(input())
odd.append(input())
odd.append(input())
odd.append(input())

print(odd)

#Q5(variable name 'week')

week = []

week.append(input())
week.append(input())
week.append(input())
week.append(input())
week.append(input())
week.append(input())
week.append(input())

print(week)


'''✔ requires_input
✔ requires_collection = list
✔ no loop
✔ min_variables = 1'''

'''✅ questionlevel3.py — Player Code

All require:

2 variables

operation

print

Q1 – Addition'''
a = int(input())
b = int(input())

result = a + b

print(result)

#Q2 – Subtraction
a = int(input())
b = int(input())

result = a - b

print(result)

#Q3 – Multiplication
a = int(input())
b = int(input())

result = a * b

print(result)

#Q4 – Division
a = int(input())
b = int(input())

result = a / b

print(int(result))


#(Ensures output = "2" not "2.0")

#Q5 – Modulus
a = int(input())
b = int(input())

result = a % b

print(result)


'''✔ requires_operation = True
✔ correct operation_type
✔ min_variables = 2'''

'''✅ questionlevel4.py — Player Code

These are stricter.

Q1 – Even Numbers

Must use:

list

for loop

condition

modulus

variable flow

min 2 variables'''
numbers = []
result = []

for _ in range(5):
    value = int(input())
    numbers.append(value)

for n in numbers:
    if n % 2 == 0:
        result.append(str(n))

print(result)
'''✔ for loop
✔ modulus
✔ condition
✔ list
✔ variable_flow'''
#Q2 – Odd Numbers
numbers = []
result = []

for _ in range(5):
    value = int(input())
    numbers.append(value)

for n in numbers:
    if n % 2 != 0:
        result.append(str(n))

print(result)

'''Q3 – Grade System

Must use:

dict

for loop

comparison

condition

variable flow'''
students = {}
grades = []

for _ in range(5):
    name = input()
    marks = int(input())
    students[name] = marks

for name in students:
    score = students[name]

    if score >= 80:
        grades.append("A")
    elif score >= 70:
        grades.append("B")
    elif score >= 60:
        grades.append("C")
    else:
        grades.append("D")

print(grades)
'''✔ dict
✔ for loop
✔ comparison
✔ condition
✔ variable_flow'''

#Q4 – Unique Values (Set)

# loop required.
'''NOT ALLOWED unique_values = set()

for _ in range(10):
    unique_values.add(int(input()))

print(unique_values)'''

numbers = []

for _ in range(10):
    numbers.append(int(input()))

unique_values = set(numbers)

print(unique_values)




'''✔ requires_collection = set
✔ variable_flow
✔ no loop'''

#Q5 – Tuple
day = input()
month = input()
year = input()

bob = (day, month, year)

print(bob)


'''✔ tuple
✔ variable_flow
✔ no loop
✔ no condition'''

#level5- FINAL LEVEL
'''✅ QUESTION 1

Second Largest Number

🔹 Approach 1 (Manual Tracking – Strong Schema Friendly)

✔ list
✔ loop
✔ condition
✔ function
✔ return
✔ variable flow
✔ ≥2 variables'''
nums = list(map(int, input().split()))

def second_largest(numbers):
    largest = float('-inf')
    second = float('-inf')

    for n in numbers:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n

    return second

result = second_largest(nums)
print(result)
'''🔹 Approach 2 (Sort Logic Without Built-in sort())

✔ loop
✔ condition
✔ manual logic'''
nums = list(map(int, input().split()))

def second_largest(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers[-2]

result = second_largest(nums)
print(result)
'''✅ QUESTION 2

Word Frequency Dictionary

🔹 Approach 1 (Classic Dictionary Counting)'''
sentence = input()
words = sentence.split()

def word_frequency(word_list):
    freq = {}

    for word in word_list:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

result = word_frequency(words)
print(result)
#Approach 2 (Using get() Method – Cleaner Logic)
sentence = input()

def word_frequency(text):
    words = text.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1

    return freq

result = word_frequency(sentence)
print(result)
'''✅ QUESTION 3

Student Grade

🔹 Approach 1 (if-elif Ladder)'''
marks = int(input())

def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 75:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 40:
        return 'C'
    else:
        return 'F'

result = get_grade(marks)
print(result)
#🔹 Approach 2 (Using Range Logic Clearly)
marks = int(input())

def get_grade(score):
    grade = 'F'

    if score >= 85:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'F'

    return grade

result = get_grade(marks)
print(result)
'''✔ Condition
✔ Function
✔ Return
✔ Variable flow'''

'''✅ QUESTION 4

Menu Driven Contact Manager

Schema requires:

✔ dictionary
✔ while loop
✔ condition
✔ state-based
✔ variable flow

🔹 Best Structured Version'''
contacts = {}

while True:
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input()

    if choice == "1":
        name = input()
        number = input()
        contacts[name] = number
        print("Contact Added")

    elif choice == "2":
        for name in contacts:
            print(name, contacts[name])

    elif choice == "3":
        name = input()
        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Not Found")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
'''✔ State maintained
✔ Dictionary used
✔ While loop
✔ Conditions
✔ Variable flow'''


#non split ..100% compatible version of final level of your engine 
#