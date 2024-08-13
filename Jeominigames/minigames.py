from secret import *
from openai import AzureOpenAI

ENDPOINT = AZURE_OPENAI_ENDPOINT
KEY = AZURE_OPENAI_API_KEY
MODEL = "gpt-35-turbo"

openai_client = AzureOpenAI(
    api_key=KEY,
    azure_endpoint=ENDPOINT,
    api_version="2024-05-01-preview"
)

def generate_question(category, level):
    prompt = f"Generate a {level} level Jeopardy question and answer for the category {category}. The question should be more difficult with higher levels."
    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a highly skilled teacher that creates Jeopardy questions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150
    )
    ai_response = response.choices[0].message.content
    question, answer = ai_response.split("Answer:")
    return question.strip(), answer.strip()

def play_jeopardy():
    score = 0
    print("Welcome to Jeopardy Chatbot!")

    while True:
        # Allow the user to choose a category
        category = input("\nEnter a category you want to play: ").strip()

        # Loop through levels of difficulty
        for level in [100, 200, 300, 400, 500]:
            question, answer = generate_question(category, level)
            print(f"\nLevel {level} Question: {question}")
            user_answer = input("Your answer: ").strip()
            
            if user_answer.lower() == answer.lower():
                print("Correct!")
                score += level
            else:
                print(f"Wrong. The correct answer was: {answer}")
            
            play_next = input("\nDo you want to continue to the next level? (yes/no): ").strip().lower()
            if play_next != 'yes':
                break

        # Ask if the user wants to continue with a new category
        play_again = input("\nDo you want to play a new category? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print(f"Your final score: {score}")

# Start the game
play_jeopardy()
