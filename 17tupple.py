# tupple are imutable in python
marks = (95,98,97,95,91,95,18,97) # paranthesis are optional for the tupple we can create  tupple without  paranthesis

#marks[0] = 99  # show error because tupple's element can not be changed 
print(marks.count(95))

print(marks.index(97)) 

marks.__add__(30)

person = "Ishita","himanshu "  # this is also a tupple

person[0] = "Ishi" # shows error because person is a tupple