# 🔐 File Encryptor (Python)

A simple Python tool to **encrypt and decrypt text files** using either:

- **Fernet encryption** (secure, modern, symmetric encryption)
- **Caesar cipher** (basic, educational shift cipher)

This project demonstrates file handling, user input, and encryption techniques in Python.

---

## 📌 Features
- Encrypt any text file and save the encrypted output.
- Decrypt encrypted files back to their original form.
- Choose between **Fernet** (secure) or **Caesar cipher** (simple).
- Automatically generates and stores a Fernet key (`secret.key`).
- Works via command-line prompts.

---

## ⚙️ Requirements
- Python 3.7+
- [cryptography](https://pypi.org/project/cryptography/) library

Install dependencies:
```bash
pip install cryptography