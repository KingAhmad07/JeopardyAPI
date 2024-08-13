import json
from jeo import *

def aiPrompt(prompt):
    response = openai_client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a highly skilled teacher that wants to create jeopardry"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=4000
    )
    ai_response = response.choices[0].message.content
    return ai_response

def modifyPrompt(topic, levels, subtopics):
    # Start building the prompt with topic and dynamic level range
    prompt = (
        f"Generate Jeopardy-style questions for the topic '{topic}', "
        f"with questions ranging from level 100 to {levels}, increasing in difficulty. "
        f"Also, create {subtopics} different subtopics based on the main topic. Also by the way create your own unique subtopic title. Format the response as JSON like this:\n\n"
        "{\n"
    )

    # Loop through to create JSON structure for the specified number of subtopics
    for i in range(1, subtopics + 1):
        subtopic_placeholder = (
            f"'Subtopic{i}': {{\n"
        )
        prompt += subtopic_placeholder
        
        # Loop to create questions for each level from 100 to the specified levels
        for level in range(100, levels + 100, 100):
            question_placeholder = (
                f"  '{level}': {{'Question': 'Question{level}', 'Answer': 'Answer{level}'}},\n"
            )
            prompt += question_placeholder
            
        # Remove trailing comma from the last question and close the subtopic
        prompt = prompt.rstrip(',\n') + "\n  },\n"

    # Add a placeholder for the remaining subtopics and close the JSON
    prompt += "'... other subtopics ...\n"
    prompt += "}\n\n"
    prompt += "ONLY return the JSON data and nothing else."

    return prompt

def generateJeopardy(topic,levels = 500, subtopics = 5):
    prompt = modifyPrompt(topic, levels, subtopics)
    print(subtopics)
    
    ai_response = aiPrompt(prompt)
       #print(ai_response)

    # Attempt to parse the response as JSON
    try:
        json_data = json.loads(ai_response)
        return json_data
    except json.JSONDecodeError as e:
        print("Failed to parse JSON response:", e)
        return None



#print(generateJeopardy("us history"))

#print(generateJeopardy("ushistory",300,3))

