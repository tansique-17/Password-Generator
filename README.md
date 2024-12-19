# Password Generator Application

This is a simple password generator built using Python's `customtkinter` library for the GUI, with functionality to generate secure passwords with customizable options. The user can specify the length of the password and choose whether to include lowercase letters, uppercase letters, digits, and special characters in the password.

## Features

- **Password Generation**: Generates a random password based on the user's selected options (length and character sets).
- **Customizable Options**:
  - Includes options for generating lowercase letters, uppercase letters, digits, and special characters.
- **Clipboard Functionality**: The generated password can be copied to the clipboard with a button click.
- **User Interface**: A simple and clean interface with checkboxes for the user to select the character sets they want in the password.
- **About Section**: A menu option that shows information about the application.
- **Exit Functionality**: An exit option in the menu to close the application.

## Requirements

To run this application, make sure you have the following Python libraries installed:

- `customtkinter`: For the GUI framework.
- `pyperclip`: For copying the generated password to the clipboard.
- `tkinter`: Standard Python library for GUI development (used by `customtkinter`).
  
You can install the required libraries using pip:

```bash
pip install customtkinter pyperclip
```
---

## How to Use

1. **Enter Password Length**: In the "Enter password length" input field, specify the desired length for the password.  
2. **Select Character Sets**: Use the checkboxes to include or exclude different types of characters in the password.  
   - **Lowercase**: Include lowercase letters.  
   - **Uppercase**: Include uppercase letters.  
   - **Digits**: Include numeric digits.  
   - **Special Characters**: Include symbols and punctuation.  
3. **Generate Password**: Click the "Generate Password" button or press `Enter` to generate the password based on your inputs.  
4. **Copy to Clipboard**: Click the "Copy to Clipboard" button to copy the generated password to your clipboard for easy use.

   
---
## Menu Bar
**1. About: Displays information about the application (version and creator).
2. Exit: Closes the application.**
---

## Example Usage
1. Launch the application.
2. Set the password length to 12.
3. Select the checkboxes for lowercase, uppercase, digits, and special characters.
4. Click "Generate Password" to get a randomly generated password like A3f^b2Z!G9k7.
5. Copy it to the clipboard and use it as needed.
---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/tansique-17/Password-Generator/blob/main/LICENSE) file for details.
