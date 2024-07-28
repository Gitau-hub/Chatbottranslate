from googletrans import Translator

def chatbot():
    translator = Translator()
    print("Hi! I am a simple chatbot that can translate text. Type 'bye' to exit.")
    print("Enter the text you want to translate, followed by the language code (e.g., 'Hello -> es').")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        try:
            text, lang = user_input.split(' -> ')
            translation = translator.translate(text, dest=lang)
            print(f"Bot: {translation.text}")
        except ValueError:
            print("Bot: Please enter the text in the correct format: 'text -> language_code'.")
        except Exception as e:
            print(f"Bot: Sorry, an error occurred: {e}")

if __name__ == "__main__":
    chatbot()