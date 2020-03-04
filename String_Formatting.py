There are two ways of doing it:-
  
user_input = input("Enter your Name: ")
message = f"Hello {user_input}"
print(message)

        OR,
user_input = input("Enter your Name: ")
message = "Hello %s" %user_input
print(message)
  
