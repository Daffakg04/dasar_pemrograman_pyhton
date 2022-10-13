a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!" 

a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!'] 

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

#dataerror
#age = 36
#txt = "My name is John, I am " + age
#print(txt)
#yang benar
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 

txt = "Hello\nWorld!"
print(txt) 
txt = 'It\'s alright.'
print(txt) 
txt = "This will insert one \\ (backslash)."
print(txt) 
txt = "Hello\rWorld!"
print(txt) 
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

