name = input("Enter your name: ")
surname = input("Enter your name: ")
message = ("hello %s %s") %(name,surname)
print(message)

       OR,
       
name = input("Enter your name: ")
surname = input("Enter your name: ")
message = f"hello {name} {surname}"
print(message)


       OR,
       
name = input("Enter your name: ")
experience_years = input("Enter years: ")
mesage = "Hi {}, you have {} years of experience".format(name, experience_years)
print(message)
