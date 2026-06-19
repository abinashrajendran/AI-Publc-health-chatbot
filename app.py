print("AI Public Health Chatbot")

while True:
user_input = input("Enter your symptom (or type exit to quit): ")

if user_input.lower() == "exit":
    print("Thank you for using AI Public Health Chatbot.")
    break

elif user_input.lower() == "fever":
    print("Drink plenty of water and consult a doctor if symptoms persist.")

elif user_input.lower() == "cough":
    print("Stay hydrated and consult a doctor if the cough continues.")

elif user_input.lower() == "headache":
    print("Take adequate rest and drink plenty of water.")

elif user_input.lower() == "cold":
    print("Take rest and drink warm fluids.")

elif user_input.lower() == "stomach pain":
    print("Eat light food and consult a doctor if the pain continues.")

else:
    print("Please consult a healthcare professional for advice.")