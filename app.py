# Abstraction
class MessageSender:
    def __init__(self, sender):
        self.sender = sender

    def send_message(self, message):
        pass

# Implementations
class EmailSender:
    def send_email(self, message):
        print(f"Sending email: {message}")

class SMSSender:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

class ChatAppSender:
    def send_chat_message(self, message):
        print(f"Sending chat message: {message}")

# Refined Abstractions
class TextMessage(MessageSender):
    def send_message(self, message):
        self.sender.send_email(message)

class ImageMessage(MessageSender):
    def send_message(self, message):
        self.sender.send_sms(message)

class VideoMessage(MessageSender):
    def send_message(self, message):
        self.sender.send_chat_message(message)

# Usage
if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()
    chat_app_sender = ChatAppSender()

    text_message = TextMessage(email_sender)
    text_message.send_message("Hello, this is a text message")

    image_message = ImageMessage(sms_sender)
    image_message.send_message("Hello, this is an image message")

    video_message = VideoMessage(chat_app_sender)
    video_message.send_message("Hello, this is a video message")
