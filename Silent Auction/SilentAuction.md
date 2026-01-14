# 🕊️ Silent Auction Program (Python)

A **console-based Silent Auction system** built using Python.
Multiple bidders can secretly place their bids, and once bidding ends, the program determines and announces the **highest bidder**.


## 🚀 Features

* Allows multiple bidders to participate
* Stores bidder names with their bid amounts
* Automatically finds the highest bid
* Clears the console between bidders to maintain **auction secrecy**
* Displays the final winner and bid amount



## 🧠 How It Works

1. The program asks each bidder for:

   * Name
   * Bid amount
2. After each bid, the user is asked if there are more bidders
3. If **yes**, the screen clears and the next bidder enters their bid
4. If **no**, the auction ends and:

   * All bids are displayed
   * The highest bidder is announced as the winner 🏆

---

## 📂 Project Structure

```
silent-auction/
│
├── SilentAuction.py        # Silent Auction program
└── README.md      # Project documentation
```

---

## 🛠️ Requirements

* Python **3.8 or more**
* Uses only built-in modules (`os`)


## ▶️ How to Run the Program

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/silent-auction.git
   ```

2. Navigate to the project directory:

   ```bash
   cd silent-auction
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## 💻 Sample Output

```
******Welcome to the Silent Auction Program******
What is your name?: Ram
Enter your bid: 2500
Are there more bidders? Type 'yes' or 'no': yes

What is your name?: Aman
Enter your bid: 3200
Are there more bidders? Type 'yes' or 'no': no

Here is a list of all the bidders: {'Ram': 2500, 'Aman': 3200}
The winner is Aman with the bid price of 3200
```

## 🔐 Silent Auction Logic

* Bidder data is stored in a dictionary:

  ```python
  { "Bidder Name": Bid Amount }
  ```
* The program loops through all bids to find the **maximum value**
* Console is cleared after each bidder to keep bids private
