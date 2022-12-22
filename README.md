# BitCoin_Networks
# Blockchain Transactional System
This is a project that implements a blockchain transactional system. It allows two full nodes (F1 and F2) and two clients (A and B) to connect to each other and transfer funds. It also keeps track of the funds stored in each account and makes sure that all transactions are valid. 

## Features
* Initial balance of each client account is 1000 BC (bitcoin) and the initial balance of each full node account is 0 BC (bitcoin). 
* Each client can record a transaction with either of its accounts and sends it to its full node. 
* The full nodes can mine a block with the transactions when there are 4 transactions in the list of temporary transactions. 
* F1 mines the odd blocks and F2 mines the even blocks. 
* Once mined, the miner full node stores the block in its blockchain and sends the mined block to the other full node. 
* The corresponding transactions are sent to the clients. 
* When a client receives the confirmed transactions, it appends it to the its list of confirmed transactions and update its balance. 

## Requirements
* Python 3.7 


## Installation
Clone the repository 
```
git clone https://github.com/username/repository.git
```

Install the requirements 
```
pip install -r requirements.txt
```

## Usage
Start the full node F1
```
python full_node_f1.py
```

Start the full node F2
```
python full_node_f2.py
```

Start the client A 
```
python client_a.py
```

Start the client B 
```
python client_b.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
