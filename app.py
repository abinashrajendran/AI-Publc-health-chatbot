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