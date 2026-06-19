print("AI Public Health Chatbot")

user_input = input("Enter your symptom: ")

if user_input.lower() == "fever":
    print("Drink plenty of water and consult a doctor if symptoms persist.")

elif user_input.lower() == "cough":
    print("Stay hydrated and consult a doctor if the cough continues.")

elif user_input.lower() == "headache":
    print("Take adequate rest and drink plenty of water.")

else:
    print("Please consult a healthcare professional for advice.")