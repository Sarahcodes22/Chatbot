# Rule-Based Chatbot

A simple command-line chatbot built in Python as part of my AI internship at **DecodeLabs**. It replies to predefined user inputs using `if-elif-else` logic inside a continuous loop.

## Features

- Handles greetings (hi, hello, hey, salam, good morning, good evening)
- Handles exit commands (bye, exit, quit, goodbye)
- Uses `if-elif-else` logic to choose a response
- Runs in a continuous loop until the user exits
- Answers basic questions about itself, AI, chatbots, machine learning and Python
- Tells the current time and date
- Cleans user input (lowercase, no punctuation) so "Hello!!" and "hello" work the same
- Falls back to a helpful message when it doesn't understand

## How It Works

1. The program prints a welcome banner and enters a `while True` loop.
2. It reads the user's message with `input()`.
3. `get_response()` cleans the text and checks it against a chain of `if-elif-else` rules.
4. The matching reply is printed. If the user typed an exit command, the loop breaks and the program ends.

This is a **rule-based system**: it has no learning or training, only predefined condition → response pairs. Rule-based chatbots are the foundation for more advanced conversational AI.

## Requirements

- Python 3.6 or higher
- No external libraries needed

## How to Run

```bash
git clone https://github.com/YOUR-USERNAME/rule-based-chatbot.git
cd rule-based-chatbot
python chatbot.py
```

On some systems, use `python3 chatbot.py` instead.

## Sample Conversation

```
==================================================
  DecoBot - Simple Rule-Based Chatbot
  Type 'bye', 'exit' or 'quit' to leave.
==================================================
You: hi
DecoBot: Hello! How can I help you today?
You: what is your name?
DecoBot: I'm DecoBot, a simple rule-based chatbot.
You: what is AI?
DecoBot: AI (Artificial Intelligence) is the ability of machines to perform tasks that normally need human intelligence, like learning, reasoning and understanding language.
You: thanks
DecoBot: You're welcome!
You: bye
DecoBot: Goodbye! Have a great day!
```

## Project Structure

```
rule-based-chatbot/
├── chatbot.py   # chatbot source code
└── README.md    # project documentation
```

## Skills Practiced

- Control flow and decision-making logic (`if-elif-else`)
- Loops and user input handling
- String processing and functions
- Basic AI concepts (rule-based systems)

## Future Improvements

- Add more topics and responses
- Store rules in a dictionary or JSON file
- Add fuzzy matching for typos
- Upgrade to an NLP-based chatbot (TF-IDF or similar)
- Build a simple GUI or web interface

## Author

Sarah Moazzam
AI Intern at DecodeLabs
[LinkedIn](www.linkedin.com/in/sarah-moazzam-04a953406) · [GitHub](https://github.com/Sarahcodes22)
