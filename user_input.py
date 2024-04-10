def main():
    # Ask the user for their name and store it in a variable called "name"
    name = input("Please enter your name: ")

    # Ask the user for their age and store it in a variable called "age"
    age = input("Please enter your age: ")

    # Ask the user for their location and store it in a variable called "location"
    location = input("Please enter your location: ")

    # Print out a personalized message using the user's name, age, and location
    print("Hello " + name + ", you are " + age + " years old and live in " + location + ".")

if __name__ == "__main__":
    main()
