# 🔐 Caesar Cipher (Encryption & Decryption in Python)

A **console-based Caesar Cipher program** implemented in Python that allows users to **encrypt and decrypt messages** using a shift-based substitution technique.

The Caesar Cipher is one of the **earliest and simplest encryption algorithms**, where each letter in a message is shifted by a fixed number of positions in the alphabet.


## 📌 What is Caesar Cipher?

The **Caesar Cipher** is a **substitution cipher** where:

* Each letter in the plaintext is replaced by another letter
* The replacement is done by shifting characters forward or backward by a fixed number (called the **shift key**)

### Example

```
Plain Text : HELLO
Shift Key : 3
Encrypted : KHOOR
```


## 🚀 Features

* Supports **encryption and decryption**
* Works with both **uppercase and lowercase letters**
* Preserves non-alphabetic characters (spaces, numbers, symbols)
* User-friendly command-line interface
* Continuous execution until the user chooses to exit


## 🧠 How the Program Works

1. User selects:

   * `encrypt` → to encrypt a message
   * `decrypt` → to decrypt a message
2. User enters:

   * The message
   * The shift key (integer)
3. Each character is:

   * Shifted forward for encryption
   * Shifted backward for decryption
4. The program displays the final transformed text


## 📂 Project Structure

```
caesar-cipher/
│
├── main.py        # Encryption & Decryption logic
└── CaeserCipher.md      # Project documentation
```


## 🛠️ Requirements

* Python **3.7 or more**
* No external libraries required


## ▶️ How to Run the Program

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/caesar-cipher.git
   ```

2. Navigate to the project directory:

   ```bash
   cd caesar-cipher
   ```

3. Run the program:

   ```bash
   python main.py
   ```


## 💻 Sample Interaction

```
Type 'encrypt' for encryption, type 'decrypt' for decryption:
encrypt
Type your message:
Hello World
Enter shift key:
3
Here's the text after encryption Khoor Zruog
```


## 🔑 Encryption & Decryption Logic

* **Encryption Formula**:

  ```
  Encrypted Character = (Original Position + Shift Key) % 26
  ```

* **Decryption Formula**:

  ```
  Original Character = (Encrypted Position - Shift Key) % 26
  ```


## 🏛️ Where is Caesar Cipher Used?

### 🔍 Historical Use

* Used by **Julius Caesar** to protect military communications
* One of the earliest known encryption techniques

### 🧪 Educational Field

* Teaching **cryptography fundamentals**
* Understanding:

  * Substitution ciphers
  * Encryption vs decryption
  * Key-based security concepts

### 💻 Computer Science & Cybersecurity

* Demonstrating:

  * Weak vs strong encryption
  * Brute-force attack concepts
* Used in **introductory security courses**

### 🧠 Modern Relevance

⚠️ **Not secure for real-world applications**, but still valuable for:

* Learning encryption logic
* Building foundations for advanced algorithms like:

  * AES
  * RSA
  * SHA hashing


## 🔧 Possible Enhancements (Future Scope)

* Fix wrap-around for uppercase letters correctly
* Add brute-force decryption mode
* Support custom alphabets
* Convert into GUI or web app
* Combine with other classical ciphers
