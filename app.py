print("AI Public Health Chatbot")
print("Available symptoms: fever, cough, headache, cold, stomach pain")
print("Type 'exit' to quit")

while True:
user_input = input("\nEnter your symptom: ")

if user_input.lower() == "exit":
    print("Thank you for using AI Public Health Chatbot.")
    break

elif user_input.lower() == "fever":
    print("Possible cause: Infection")
    print("Advice: Drink plenty of water and consult a doctor if symptoms persist.")

elif user_input.lower() == "cough":
    print("Possible cause: Common cold or throat irritation")
    print("Advice: Stay hydrated and consult a doctor if the cough continues.")

elif user_input.lower() == "headache":
    print("Possible cause: Stress or dehydration")
    print("Advice: Take adequate rest and drink plenty of water.")

elif user_input.lower() == "cold":
    print("Possible cause: Viral infection")
    print("Advice: Take rest and drink warm fluids.")

elif user_input.lower() == "stomach pain":
    print("Possible cause: Indigestion")
    print("Advice: Eat light food and consult a doctor if the pain continues.")

else:
    print("Symptom not found. Please consult a healthcare professional.")