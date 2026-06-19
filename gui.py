def check_symptom():
symptom = entry.get().lower()

symptoms = {
    "fever": "Drink plenty of water and consult a doctor if symptoms persist.",
    "cough": "Stay hydrated and consult a doctor if the cough continues.",
    "headache": "Take adequate rest and drink plenty of water.",
    "cold": "Take rest and drink warm fluids.",
    "stomach pain": "Eat light food and consult a doctor if the pain continues."
}

if symptom in symptoms:
    result.config(text=symptoms[symptom])
else:
    result.config(text="Please consult a healthcare professional.")