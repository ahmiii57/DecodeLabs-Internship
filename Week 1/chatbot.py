"""
Project: Rule-Based AI Chatbot
--------------------------------
A simple chatbot that uses if-else (rule-based) logic to respond to
predefined user inputs. It runs continuously in a loop, handles common
greetings, casual questions, and exit commands.

Key Concepts Demonstrated:
- Control flow (if / elif / else)
- Decision-making logic
- Basic AI concept: pattern matching on user input (rule-based, no ML)

Author: (Your Name)
"""


def get_bot_response(user_input):
    """
    Takes the user's input as a string, normalizes it, and returns
    a predefined response based on simple if-else rule matching.

    Parameters:
        user_input (str): The raw text typed by the user.

    Returns:
        str: The chatbot's response.
    """
    # Normalize input: remove extra spaces and convert to lowercase
    # so that "Hello", "HELLO", and "hello" are all treated the same.
    text = user_input.strip().lower()

    # ---------- Greetings ----------
    if text in ("hi", "hello", "hey", "hii", "helo"):
        return "Hello! How can I help you today?"

    # ---------- How are you ----------
    elif text in ("how are you", "how are you?"):
        return "I'm just a program, but I'm running perfectly! How about you?"

    # ---------- Name questions ----------
    elif text in ("what is your name", "what's your name", "who are you"):
        return "I'm a simple rule-based chatbot created for a Python project."

    # ---------- Thanks ----------
    elif text in ("thanks", "thank you", "thanx"):
        return "You're welcome!"

    # ---------- Help ----------
    elif text in ("help", "what can you do"):
        return ("I can greet you, chat a little, and respond to a few "
                "basic questions. Type 'bye' or 'exit' anytime to quit.")

    # ---------- Exit commands ----------
    elif text in ("bye", "exit", "quit", "goodbye"):
        return "EXIT"  # special marker handled in main loop

    # ---------- Fallback for unrecognized input ----------
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def run_chatbot():
    """
    Runs the chatbot in a continuous loop, taking user input from the
    console and printing the bot's response, until an exit command
    is entered.
    """
    print("=" * 50)
    print(" Rule-Based Chatbot ")
    print(" Type 'help' to see options, or 'bye'/'exit' to quit. ")
    print("=" * 50)

    # Continuous loop: keeps the conversation going until user exits
    while True:
        user_input = input("You: ")

        response = get_bot_response(user_input)

        # If the response is our special "EXIT" marker, end the loop
        if response == "EXIT":
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot:", response)


# Entry point of the program
if __name__ == "__main__":
    run_chatbot()
