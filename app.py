from datetime import datetime

print("AI Public Health Chatbot")

current_time = datetime.now()
print("Date and Time:", current_time)

print("Type 'exit' to quit")

symptoms = {
    "fever": "Possible Viral Fever. Drink plenty of water and take rest.",
    "cough": "Stay hydrated and consult a doctor if the cough persists.",
    "headache": "Take adequate rest and drink plenty of water.",
    "cold": "Take rest and drink warm fluids.",
    "stomach pain": "Eat light food and consult a doctor if pain continues.",
    "dengue": "High fever and joint pain. Seek medical attention.",
    "malaria": "Fever with chills and sweating. Consult a doctor.",
    "covid": "Fever, cough, and fatigue. Follow health guidelines.",
    "diabetes": "Monitor blood sugar levels and consult a doctor.",
    "asthma": "Avoid triggers and keep inhalers available.",
    "typhoid": "Persistent fever and weakness. Medical treatment required.",
    "cholera": "Severe diarrhea and dehydration. Seek immediate care.",
    "tuberculosis": "Persistent cough and weight loss. Consult a doctor.",
    "pneumonia": "Chest pain and breathing difficulty. Medical attention needed.",
    "allergy": "Avoid allergens and take prescribed medication.",
    "migraine": "Rest in a quiet room and stay hydrated.",
    "anemia": "Eat iron-rich foods and consult a doctor.",
    "jaundice": "Yellowing of skin and eyes. Medical consultation required.",
    "arthritis": "Joint pain and stiffness. Regular exercise may help.",
    "food poisoning": "Drink ORS and avoid oily foods.",
    "dehydration": "Increase water intake immediately.",
    "skin rash": "Keep skin clean and avoid irritants.",
    "vomiting": "Drink small amounts of water frequently.",
    "diarrhea": "Use ORS and stay hydrated.",
    "chest pain": "Seek immediate medical attention.",
    "back pain": "Take rest and maintain proper posture."
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
        print("\nBMI Calculator")

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")