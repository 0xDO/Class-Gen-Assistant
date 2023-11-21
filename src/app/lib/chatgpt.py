def get_chat_response(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"
    }
    data = {
        "prompt": prompt,
        "max_tokens": 100,
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["text"]

# Example usage
prompt = "What is the capital of France?"
response = get_chat_response(prompt)
print(response)