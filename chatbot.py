"""
Simple Rule-Based Chatbot
-------------------------
A beginner-friendly chatbot that replies to predefined user inputs
using if-elif-else logic inside a continuous loop.

Run:  python chatbot.py
Exit: type  bye / exit / quit
"""

import string

BOT_NAME = "DecoBot"


def clean_input(text):
    """Lowercase the text and remove punctuation so matching is easier."""
    text = text.lower().strip()
    return text.translate(str.maketrans("", "", string.punctuation))


def get_response(user_input):
    """
    Decide how to reply using if-elif-else logic.
    Returns (reply, should_exit).
    """
    text = clean_input(user_input)
    words = text.split()  # list of words, so "hi" won't match inside "which"

    # 0. Empty input
    if text == "":
        return "Please type something so I can help you.", False

    # 1. Exit commands
    elif text in ("bye", "exit", "quit", "goodbye", "see you") or "bye" in words:
        return "Goodbye! Have a great day!", True

    # 2. Greetings
    elif any(g in words for g in ("hi", "hello", "hey", "salam", "greetings")):
        return "Hello! How can I help you today?", False
    elif "good morning" in text:
        return "Good morning! Hope you have a productive day.", False
    elif "good evening" in text:
        return "Good evening! How can I help?", False

    # 3. Questions about the bot
    elif "your name" in text or "who are you" in text:
        return f"I'm {BOT_NAME}, a simple rule-based chatbot.", False
    elif "how are you" in text:
        return "I'm doing great, thanks for asking! How about you?", False
    elif "what can you do" in text or "help" in words:
        return (
            "I can greet you, answer a few basic questions, tell you the "
            "time or date, and chat a little. Try asking 'what is AI?'",
            False,
        )

    # 4. Basic knowledge questions
    elif "what is ai" in text or "artificial intelligence" in text:
        return (
            "AI (Artificial Intelligence) is the ability of machines to "
            "perform tasks that normally need human intelligence, like "
            "learning, reasoning and understanding language.",
            False,
        )
    elif "what is a chatbot" in text or "what is chatbot" in text:
        return (
            "A chatbot is a program that simulates conversation with users, "
            "using either fixed rules or machine learning.",
            False,
        )
    elif "rule based" in text or "rulebased" in text:
        return (
            "A rule-based chatbot follows predefined rules (like if-else "
            "conditions) to pick a reply. That's exactly what I am!",
            False,
        )
    elif "machine learning" in text:
        return (
            "Machine learning is a branch of AI where computers learn "
            "patterns from data instead of being explicitly programmed.",
            False,
        )
    elif "python" in words:
        return "Python is a popular, beginner-friendly language used a lot in AI.", False

    # 5. Time and date
    elif "time" in words:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}.", False
    elif "date" in words or "today" in words:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%A, %d %B %Y')}.", False

    # 6. Politeness
    elif "thanks" in words or "thank" in words:
        return "You're welcome!", False
    elif text in ("ok", "okay", "cool", "nice"):
        return "Glad to hear that!", False

    # 7. Fallback
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do.", False


def main():
    print("=" * 50)
    print(f"  {BOT_NAME} - Simple Rule-Based Chatbot")
    print("  Type 'bye', 'exit' or 'quit' to leave.")
    print("=" * 50)

    # Continuous loop: runs until the user says goodbye
    while True:
        user_input = input("You: ")
        reply, should_exit = get_response(user_input)
        print(f"{BOT_NAME}: {reply}")

        if should_exit:
            break


if __name__ == "__main__":
    main()