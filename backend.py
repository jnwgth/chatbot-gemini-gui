import google.generativeai as genai
 
API_KEY = 'your_api_key'
PROJECT_ID = 'your_project_id'
 
# Back-End

class ChatBot:
    # Model Configuration
    model_config = {
        "temperature": 0.5,  # 1.0
        "top_p": 0.99,
        "top_k": 0,
        "max_output_tokens": 4096,
    }

    def __init__(self, api_key, project_id):
        self.api_key = api_key
        genai.configure(api_key=self.api_key)
        self.project_id = PROJECT_ID
        self.user_input = "test"
        self.model = genai.GenerativeModel('gemini-1.5-flash',
                                    generation_config=self.model_config)
        self.chat = self.model.start_chat(history=[])
 
    def get_response(self, user_input):
        response = self.chat.send_message(user_input)
        print(response.text)
        return response.text
 
if __name__ == "__main__":
    chatbot = ChatBot(api_key=API_KEY, project_id=PROJECT_ID)
    response = chatbot.get_response(user_input="write a random joke")
    print(response)
