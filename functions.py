import requests

def handle_chatbot_response(question, user):
    try:
        url = 'https://fastapi-backend-z89h.onrender.com/gemini'
        payload = {
            "question": question,
            "user": user,
            "system_instruction": "You are a helpful assistant."
        }

        response = requests.post(url, json=payload)
        print(response)
        print(type(response))

        if response.status_code == 200 and 'success' in response.json():
            return response.json()['response']
        else:
            return f"Sorry, I'm unable to answer that question. reason:{response.text}"
    except Exception as e:
        return f"An error occurred: {str(e)}"


# print(handle_chatbot_response("What is the capital of France?", "John"))