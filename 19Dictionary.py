marks = {"english":95 , "chemistry":99 }

print(marks["chemistry"])
marks["english"] = 92;
print(marks)

marks["physics"] = 99;
print(marks)

# 1. Add new element
marks["math"] = 100
print("After adding math:", marks)

# 2. Remove an element
marks.pop("chemistry")   # removes the key "chemistry"
print("After removing chemistry:", marks)

# 3. Find size of dictionary
print("Size of dictionary:", len(marks))