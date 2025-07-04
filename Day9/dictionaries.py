programming_dictionary = {
        "Bug": "In computer technology, a bug is a coding error in a computer program",
        "Function": "A piece of code that can be called over again and again"
    }

result = programming_dictionary["Bug"]
print(result)

programming_dictionary["Loop"] = "The action of doing again and again finitely"

print(programming_dictionary)

empty_dictionary = {}
print(empty_dictionary)

# Loop through dictionaries

for thing in programming_dictionary:

   print(thing + ": " +programming_dictionary[thing])