def sum_nombres(nombres):
    total = sum(nombres)
    return total

if __name__ == "__main__":
    nombres = [2, 5, 7]
    result = sum_nombres(nombres)
    print(f"La somme est: {result}")# Function to greet the user and provide a fun fact about Cameroon
def greet_user():
    # Print the initial message
    print("Hey, this is a Cameroonian Code!")
    
    # Ask the user for their name
    name = input("What is your name? ")
    
    # Greet the user personally
    print(f"Hello, {name}! Welcome to the world of programming!")
    
    # Provide a fun fact about Cameroon
    print("Did you know that Cameroon is known as 'Africa in miniature' because of its diverse geography and culture?")

# Function to sum a list of numbers
def sum_nombres(nombres):
    total = sum(nombres)
    return total

if __name__ == "__main__":
    # Call the greet_user function
    greet_user()
    
    # Define a list of numbers
    nombres = [2, 5, 7]
    
    # Calculate the sum of the numbers
    result = sum_nombres(nombres)
    
    # Print the result
    print(f"La somme est: {result}")