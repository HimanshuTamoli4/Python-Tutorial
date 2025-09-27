# List are mutable in python

marks = [95,98,97,"maths"]
print(marks)
print(marks[0])
print(marks[-1])
print(marks[-2])

print(marks[0:2])
print(marks[1:3])


for i in marks:
    print(i)   

marks.append(99)   
marks.append(97)   

print(marks)

marks.insert(0,84)   
print(marks)

marks.insert(2,18)   
print(marks)

print(18 in marks)
print(4 in marks)

print(len(marks))

i =0
while i<len(marks):
    print(marks[i])
    i+=1

print(marks)
marks.remove(97)
print(marks)  
marks.remove(97)
print(marks)
marks.remove("maths")
print(marks)    

# Clear marks list
marks.clear() 
print(marks)  