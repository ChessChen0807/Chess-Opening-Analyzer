import json

from openai import OpenAI

# Read private key from JSON file
with open('openai_key.json', 'r') as file:
    config_data = json.load(file)
    private_key = config_data.get('private_key', None)

# Check if the private key was successfully retrieved
if private_key is not None:
    print(f"Private Key found in the JSON file.")
else:
    print("Private Key not found in the JSON file.")

# Initialize OpenAI client with the retrieved private key
client = OpenAI(
    # This is the default and can be omitted
    api_key=private_key,
)


def get_opening_advice(opening_name):
    # Construct a prompt for GPT-3 to generate advice for a given chess opening
    instruction_prompt = f'Act as a chess master. Please provide some tips/suggestions for the {opening_name}'

    # Make a request to the GPT-3 API for completion based on the prompt
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": instruction_prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Extract and return the generated advice from the GPT-3 response
    result = chat_completion.choices[0].message.content
    return result

if __name__ == '__main__':
    advice = get_opening_advice('Slav Defense: Exchange Variation')
    print(advice)
