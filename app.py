from datetime import datetime

print("AI Public Health Chatbot")

current_time = datetime.now()
print("Date and Time:", current_time)

print("Type 'exit' to quit")

symptoms = {
    "fever": "Drink plenty of water and consult a doctor if symptoms persist.",
    "cough": "Stay hydrated and consult a doctor if the cough continues.",
    "headache": "Take adequate rest and drink plenty of water.",
    "cold": "Take rest and drink warm fluids.",
    "stomach pain": "Eat light food and consult a doctor if the pain continues."
}

while True:
    user_input = input("\nEnter your symptom: ").lower()

    if user_input == "exit":
        print("Thank you for using AI Public Health Chatbot.")
        break

    elif user_input in symptoms:
        print("Advice:", symptoms[user_input])

    else:
        print("Symptom not found. Please consult a healthcare professional.")