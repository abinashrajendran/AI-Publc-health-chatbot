import tkinter as tk

def check_symptom():
symptom = entry.get().lower()

if symptom == "fever":
    result.config(text="Drink plenty of water and consult a doctor if symptoms persist.")
elif symptom == "cough":
    result.config(text="Stay hydrated and consult a doctor if the cough continues.")
elif symptom == "headache":
    result.config(text="Take adequate rest and drink plenty of water.")
else:
    result.config(text="Please consult a healthcare professional.")

window = tk.Tk()
window.title("AI Public Health Chatbot")
window.geometry("500x300")

label = tk.Label(window, text="Enter your symptom:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Check", command=check_symptom)
button.pack()

result = tk.Label(window, text="")
result.pack()

window.mainloop()