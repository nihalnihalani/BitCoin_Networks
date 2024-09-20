# BitCoin Networks
## Blockchain Transactional System

Welcome to **BitCoin Networks**, a project that implements a blockchain-based transactional system, enabling two full nodes (F1 and F2) and two clients (A and B) to transfer funds seamlessly while ensuring all transactions remain valid and secure.

### 🛠️ Features
- **Initial Balances:** 
  - Each client (A and B) starts with 1000 BC (BitCoin).
  - Each full node (F1 and F2) starts with 0 BC.
- **Transaction Process:** 
  - Clients can record transactions and send them to their respective full node.
- **Block Mining:** 
  - Full nodes mine blocks once they accumulate 4 transactions.
  - F1 mines odd-numbered blocks; F2 mines even-numbered blocks.
- **Blockchain Update:** 
  - After mining, the mined block is stored and shared between the full nodes.
  - Transactions are confirmed and sent to clients.
- **Balance Update:**
  - Clients append confirmed transactions and update their balances accordingly.

### 📋 Requirements
- Python 3.7+

### 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nihalnihalani/BitCoin_Networks

2. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙Usage

- **Start Full Node F1:**
   ```bash
   python full_node_f1.py
   ```

- **Start Full Node F2:**
   ```bash
   python full_node_f2.py
   ```

- **Start Client A:**
   ```bash
   python client_a.py
   ```

- **Start Client B:**
   ```bash
   python client_b.py
   ```

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss the changes you'd like to make.

Make sure to update tests where necessary.

## 📄 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
