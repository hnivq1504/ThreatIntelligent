import requests

class Bot:
    def __init__(self,token,chatId):
        self.token = token
        self.chatId = chatId
    
    def send_message(self,message):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        data = {"chat_id": self.chatId, "text": message}
        response = requests.post(url, data=data)
        if not response.ok:
            print("Failed to send message:", response.text)

    def create_message(new_data):
        message = "New articles!!!\n\n"
        for article in new_data:
            message += f"{article['Title']} ({article['Link']})\n\n"
        return message
    
    def split_message(message):
        max_length = 4096
        if len(message) <= max_length:
            return [message]
        chunks = [message[i:i+max_length] for i in range(0, len(message), max_length)]
        return chunks
    