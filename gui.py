import tkinter as tk

# Function
def check_symptom():
    symptom = entry.get().lower()

    if symptom == "fever":
        result.config(
            text="🟢 Drink plenty of fluids and take rest.",
            fg="green"
        )

    elif symptom == "cough":
        result.config(
            text="🔵 Stay hydrated and consult a doctor if the cough continues.",
            fg="blue"
        )

    elif symptom == "headache":
        result.config(
            text="🟣 Take rest and avoid stress.",
            fg="purple"
        )

    elif symptom == "cold":
        result.config(
            text="🟢 Drink warm water and get enough sleep.",
            fg="green"
        )

    else:
        result.config(
            text="🔴 Symptom not found. Please consult a doctor.",
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