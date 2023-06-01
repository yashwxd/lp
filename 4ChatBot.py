# Define a dictionary of predefined responses
responses = {
    "hey": "Hello! How can I assist you today?",
    "hello": "Hello! How can I assist you today?",
    "hi": "Hello! How can I assist you today?",
    "how are you?": "I'm doing well, thank you! How about you?",
    "i am fine": "Great",
    "i need help": "Of course! I'm here to help. What do you need assistance with?",
    "pricing": "For pricing information, please visit our website or contact our sales team at sales@example.com.",
    "order status": "To check the status of your order, please provide your order number and we will assist you.",
    "product information": "Our products are designed to provide high quality and exceptional performance. Is there any specific product you would like information about?",
    "payment options": "We offer various payment options, including credit cards, PayPal, and bank transfers.",
    "shipping information": "Our standard shipping time is 3-5 business days. Express shipping options are also available.",
    "return policy": "Our return policy allows returns within 30 days of purchase. Please ensure the product is in its original condition and packaging.",
    "account registration": "To create an account, please visit our website and click on the 'Register' button.",
    "password reset": "To reset your password, please click on the 'Forgot password' link on the login page and follow the instructions.",
    "technical support": "For technical support, please contact our support team at support@example.com or call our helpline at +1-123-456-7890.",
    "discounts and promotions": "We frequently offer discounts and promotions. Please subscribe to our newsletter to stay updated.",
    "order cancellation": "To cancel your order, please contact our customer service as soon as possible with your order details.",
    "default": "I'm sorry, I didn't understand. Could you please rephrase?"
}

print("Welcome to DoorStep.com assistance!!!")

while True:
    user_input = input("You: ")

    if user_input in responses:
        print("ChatBOT(DoorStep.com): ", responses[user_input])
    elif user_input == 'exit':
        exit()
    else:
        print("ChatBOT(DoorStep.com): ", responses["default"])
