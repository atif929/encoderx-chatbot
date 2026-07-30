from backend.chatbot import get_response

history = []

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = get_response(question, history)

    print("\nAssistant:\n")

    print(answer)

    history.append(
        {
            "role": "user",
            "parts": [question]
        }
    )

    history.append(
        {
            "role": "model",
            "parts": [answer]
        }
    )