def create_greeting(first_name, last_name):
    greeting = f"Hello, {first_name} {last_name}! Welcome to the community!"
    return greeting

# Example 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(create_greeting(first_name, last_name))


