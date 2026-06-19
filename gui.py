import tkinter as tk

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

window = tk.Tk()
window.title("Symptom Checker")
window.geometry("500x300")
window.configure(bg="lightblue")

label = tk.Label(
    window,
    text="Enter your symptom:",
    font=("Arial", 14),
    bg="lightblue"
)
label.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(window, text="Check", command=check_symptom)
button.pack(pady=10)

result = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    bg="lightblue",
    wraplength=450
)
result.pack(pady=20)

window.mainloop()