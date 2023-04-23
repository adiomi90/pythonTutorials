def greet(first_name, last_name):
    print(f"Hi there {first_name} {last_name}")
    print("Welcome onboard")


greet("Molecular", "Particles")
greet("John", "Smith")

# returns a value
def greet2(name):
    return f"Hi {name}"

message = greet2("Tikils90")
file = open("message1.txt","w")
file.write(message)
  