import tkinter as tk

# Function
def check_symptom():
    symptom = entry.get().lower()

    symptoms = {
        "fever": "🟢 Drink plenty of fluids and take rest.",
        "cough": "🔵 Stay hydrated and consult a doctor if the cough continues.",
        "headache": "🟣 Take rest and avoid stress.",
        "cold": "🟢 Take rest and drink warm fluids.",
        "stomach pain": "🟠 Eat light food and consult a doctor if pain continues.",
        "dengue": "🔴 High fever, joint pain and weakness. Seek medical attention.",
        "malaria": "🟠 Fever with chills and sweating. Consult a doctor.",
        "covid": "🟡 Fever, cough and fatigue. Follow health guidelines.",
        "typhoid": "🔴 Persistent fever and weakness. Medical treatment required.",
        "cholera": "🔴 Severe diarrhea and dehydration. Seek immediate care.",
        "tuberculosis": "🔴 Persistent cough and weight loss. Consult a doctor.",
        "pneumonia": "🔴 Chest pain and breathing difficulty. Seek medical care.",
        "asthma": "🟠 Breathing difficulty and wheezing. Avoid triggers.",
        "diabetes": "🟡 Monitor blood sugar levels and consult a doctor.",
        "allergy": "🟢 Avoid allergens and take prescribed medication.",
        "migraine": "🟣 Rest in a quiet room and stay hydrated.",
        "anemia": "🟠 Eat iron-rich foods and consult a doctor.",
        "jaundice": "🟡 Yellowing of skin and eyes. Medical consultation required.",
        "arthritis": "🟢 Joint pain and stiffness. Regular exercise may help.",
        "food poisoning": "🟠 Drink ORS and avoid oily foods.",
        "dehydration": "🟡 Increase water intake immediately.",
        "skin rash": "🟢 Keep skin clean and avoid irritants.",
        "vomiting": "🟠 Drink small amounts of water frequently.",
        "diarrhea": "🟠 Use ORS and stay hydrated.",
        "chest pain": "🔴 Seek immediate medical attention.",
        "back pain": "🟢 Take rest and maintain proper posture.",
        "ear pain": "🟠 Avoid inserting objects into the ear and consult a doctor.",
        "eye pain": "🟠 Avoid rubbing the eyes and seek medical advice.",
        "sore throat": "🟢 Drink warm fluids and get adequate rest.",
        "high blood pressure": "🟡 Reduce salt intake and consult a doctor.",
        "low blood pressure": "🟡 Drink fluids and seek medical advice.",
        "obesity": "🟢 Maintain a healthy diet and exercise regularly.",
        "constipation": "🟢 Eat fiber-rich foods and drink more water.",
        "acidity": "🟠 Avoid spicy foods and eat smaller meals.",
        "stress": "🟢 Practice relaxation techniques and get enough sleep.",
        "anxiety": "🟢 Exercise regularly and seek support if needed.",
        "insomnia": "🟢 Maintain a regular sleep schedule.",
        "heart disease": "🔴 Follow medical advice and maintain a healthy lifestyle.",
        "kidney stones": "🟠 Drink plenty of water and consult a doctor.",
        "liver disease": "🔴 Avoid alcohol and seek medical care.",
        "bronchitis": "🟠 Rest well and stay hydrated.",
        "sinusitis": "🟢 Use steam inhalation and consult a doctor if needed."
    }

    if symptom in symptoms:
        result.config(text=symptoms[symptom], fg="green")
    else:
        result.config(
            text="❌ Symptom not found. Please consult a healthcare professional.",
            fg="red"
        )

# Clear function
def clear_all():
    entry.delete(0, tk.END)
    result.config(text="", fg="black")

# Main Window
root = tk.Tk()
root.title("AI Symptom Checker")
root.geometry("700x500")
root.configure(bg="#DFF6FF")

# Title
title = tk.Label(
    root,
    text="🩺 AI Symptom Checker",
    font=("Arial", 24, "bold"),
    bg="#DFF6FF",
    fg="#003366"
)
title.pack(pady=20)

# Label
label = tk.Label(
    root,
    text="Enter your symptom:",
    font=("Arial", 16, "bold"),
    bg="#DFF6FF"
)
label.pack()

# Entry Box
entry = tk.Entry(
    root,
    font=("Arial", 15),
    width=25,
    justify="center"
)
entry.pack(pady=15)

# Check Button
check_btn = tk.Button(
    root,
    text="Check Symptom",
    font=("Arial", 14, "bold"),
    bg="#007BFF",
    fg="white",
    width=15,
    height=1,
    command=check_symptom
)
check_btn.pack(pady=10)

# Clear Button
clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 14, "bold"),
    bg="red",
    fg="white",
    width=15,
    height=1,
    command=clear_all
)
clear_btn.pack()

# Result Box
result = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="white",
    width=50,
    height=6,
    wraplength=500,
    relief="solid",
    bd=3
)
result.pack(pady=30)

# Footer
footer = tk.Label(
    root,
    text="Developed by Abinash 🚀",
    font=("Arial", 10),
    bg="#DFF6FF",
    fg="gray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()