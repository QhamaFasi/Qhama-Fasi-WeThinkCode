# faces.py

def convert(text):
    # Replace emoticons with emojis
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt the user for input
    user_input = input("Enter your message: ")
    # Convert emoticons to emojis
    result = convert(user_input)
    # Print the result
    print(result)

# Call the main function
if __name__ == "__main__":
    main()
    