from jeo import *

categories = ["World History", "Science", "Literature", "Mathematics"]
jeopardy_data = {}

for category in categories:
    jeopardy_data[category] = {}
    for level in [100, 200, 300, 400, 500]:
        prompt = f"Generate a {level} level Jeopardy question and answer for the category {category}."
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
        jeopardy_data[category][str(level)] = {
            "Question": question.strip(),
            "Answer": answer.strip()
        }
def play_jeopardy(game_data):
    score = 0
    print("Welcome to Jeopardy!")
    while True:
        print("\nCategories:")
        for category in game_data:
            print(f"- {category}")
        
        selected_category = input("Choose a category: ").strip()
        if selected_category not in game_data:
            print("Invalid category. Try again.")
            continue
        
        print("\nLevels: 100, 200, 300, 400, 500")
        selected_level = input("Choose a level: ").strip()
        if selected_level not in game_data[selected_category]:
            print("Invalid level. Try again.")
            continue
        
        question_info = game_data[selected_category][selected_level]
        print(f"\nQuestion ({selected_level}): {question_info['Question']}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == question_info['Answer'].lower():
            print("Correct!")
            score += int(selected_level)
        else:
            print(f"Wrong. The correct answer was: {question_info['Answer']}")
        
        play_again = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

    print(f"Your final score: {score}")

# Start the game
play_jeopardy(jeopardy_data)
