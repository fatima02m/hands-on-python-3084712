greet = "Hello World"

# contcatenating the strings
extened_grt = "Hello World, " + "this is a long string"

name = "John"

# interpolating the string, adding 'name' to it
# intrupution = f"Hello {name}"

intrupution = f"{greet} whats up"

greet_format = "Hello {} howru"

# formatting
formatted = greet_format.format(name)

print(formatted)

#print(formatted.upper())
#print(formatted.lower())
#print(formatted.replace("John", "Paul"))
