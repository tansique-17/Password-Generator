import random
import string
import customtkinter as ctk
import tkinter as tk
import pyperclip  # for clipboard functionality
import tkinter.messagebox as messagebox

# Function to generate the password
def generate_password():
    # Get the length from the input box
    try:
        length = int(length_entry.get())
    except ValueError:
        result_textbox.delete(0, ctk.END)
        result_textbox.insert(0, "Invalid Length!")
        return
    
    # Get options from the checkboxes
    include_lower = lowercase_var.get()
    include_upper = uppercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()

    # Define character sets based on user preferences
    characters = ""
    if include_lower:
        characters += string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    
    # Check if at least one set is selected
    if not characters:
        result_textbox.delete(0, ctk.END)
        result_textbox.insert(0, "Please select at least one character set!")
        return

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))

    # Display the password in the result textbox
    result_textbox.delete(0, ctk.END)
    result_textbox.insert(0, password)

# Function to copy the generated password to clipboard
def copy_to_clipboard():
    password = result_textbox.get()
    pyperclip.copy(password)

# Function to show "About" message
def show_about():
    messagebox.showinfo("About", "Password Generator v1.0\nCreated with customtkinter")

# Function to handle the exit functionality
def exit_program():
    root.quit()

# Create the main window
root = ctk.CTk()

# Set the window title and size
root.title("Password Generator")
root.geometry("400x350")

# Set the background color for the main window
root.configure(bg='black')

# Create a frame to center all elements
frame = ctk.CTkFrame(root, fg_color="black", bg_color="black")
frame.pack(expand=True)

# Create a label for the password length input
length_label = ctk.CTkLabel(frame, text="Enter password length:", text_color="white", bg_color="black")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

# Create a text entry box for the password length
length_entry = ctk.CTkEntry(frame, width=100, fg_color="black", text_color="white", border_color="white")
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create checkboxes for character set options
lowercase_var = ctk.BooleanVar(value=True)
uppercase_var = ctk.BooleanVar(value=True)
digits_var = ctk.BooleanVar(value=True)
special_var = ctk.BooleanVar(value=True)

lowercase_checkbox = ctk.CTkCheckBox(frame, text="Include Lowercase", variable=lowercase_var, fg_color="gray", hover_color="blue", text_color="white", border_color="blue", checkmark_color="blue")
lowercase_checkbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="w")

uppercase_checkbox = ctk.CTkCheckBox(frame, text="Include Uppercase", variable=uppercase_var, fg_color="gray", hover_color="blue", text_color="white", border_color="blue", checkmark_color="blue")
uppercase_checkbox.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky="w")

digits_checkbox = ctk.CTkCheckBox(frame, text="Include Digits", variable=digits_var, fg_color="gray", hover_color="blue", text_color="white", border_color="blue", checkmark_color="blue")
digits_checkbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

special_checkbox = ctk.CTkCheckBox(frame, text="Include Special Characters", variable=special_var, fg_color="gray", hover_color="blue", text_color="white", border_color="blue", checkmark_color="blue")
special_checkbox.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Create a button to generate the password
generate_button = ctk.CTkButton(frame, text="Generate Password", command=generate_password, fg_color="blue", text_color="white", hover_color="darkblue")
generate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Create a text box to display the generated password
result_textbox = ctk.CTkEntry(frame, width=350, height=20, fg_color="black", text_color="white", border_color="white")
result_textbox.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create a button to copy the password to the clipboard
copy_button = ctk.CTkButton(frame, text="Copy to Clipboard", command=copy_to_clipboard, fg_color="blue", text_color="white", hover_color="darkblue")
copy_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Bind the Enter key to trigger password generation
root.bind('<Return>', lambda event: generate_password())

# Create a custom menu bar using tkinter
menu_bar = tk.Menu(root, bg="black", fg="white")

# Add "About" option directly in the menu bar
menu_bar.add_command(label="About", command=show_about)

# Add "Exit" option directly in the menu bar
menu_bar.add_command(label="Exit", command=exit_program)

# Configure the window to use the menu bar
root.config(menu=menu_bar)

# Start the Tkinter event loop
root.mainloop()
