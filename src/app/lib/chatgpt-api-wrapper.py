import openai

# Set up your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

# Define a function to send a message to the ChatGPT API
def send_message(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
    )
    return response.choices[0].text.strip()

# Test the connection by sending a message
response = send_message("Hello, ChatGPT!")
print(response)
