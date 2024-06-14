from openai import OpenAI
import os

# Set OpenAI API key
client = OpenAI(api_key = "sk-proj-bOm7O7srn4PgKb64mXGgT3BlbkFJFHLllGphoytvxqWGuy6L")

#
#
#Can's use openai as it is paid, but this is a general template that would work and can be expanded
#Further if need be.
#New plan is to use surfing and text to speech that are free, implementing timers
#and features manually with some generated text and websites that can be surfed easier

def get_response(prompt):
    completion = client.chat.completions.create(
                            model="gpt-4",
                            messages=[
                                {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
                                {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
                            ]
                            )
    try:
        response = completion.choices[0].message
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to the OpenAI CLI. Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = get_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
