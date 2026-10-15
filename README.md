# Password Manager

<p align="center">
  <img src="logo.png" alt="Password Manager shield and key logo" width="120">
  <br>
  A small desktop password manager built with Python and Tkinter.
</p>

## Features

- Generates passwords with letters, numbers, and symbols
- Copies generated passwords to the clipboard
- Validates and confirms details before saving
- Saves website, username, and password to `password.txt`
- Clears the form after a successful save

## What I learned

Tkinter widgets and grid layouts · Button commands · List comprehensions ·
`choice()`, `randint()`, and `shuffle()` · Clipboard handling · Input validation ·
Message boxes · Reading entry fields · Appending data to files

## Run locally

```bash
git clone https://github.com/onebuildatatime/simple-password-manager.git
cd simple-password-manager
python3 -m pip install -r requirements.txt
python3 main.py
```

> **Note:** This learning project stores credentials as plain text. Use test
> data only; a real password manager should encrypt its stored data.
Credit: This is a practice implementation of the Password Manager project taught by Dr. Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp** course on Udemy.


## License

Released under the [MIT License](LICENSE).
