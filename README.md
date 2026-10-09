
# Electricity Bill Calculator Using Python

## 📌 About the Project
The Electricity Bill Calculator is a simple Python program that calculates the electricity bill based on the connection type and the number of units consumed. It supports both **Non Commercial** and **Commercial** connections using different rate slabs.

## 🚀 Features
- Accepts connection type as input.
- Calculates bills based on electricity consumption.
- Supports Non Commercial and Commercial connections.
- Applies different rates based on unit consumption.
- Displays the total bill in Indian Rupees (₹).

## 🛠️ Technologies Used
  Programming Language: Python 3
  Concepts: Variables, user input, conditional statements, arithmetic operations, and nested if-else.

## ⚙️ Electricity Rate Slabs

### Non Commercial Connection

| Units Consumed | Rate Applied |
|---|---:|
| Up to 200 | ₹0 |
| 201–500 | ₹4 per unit on units above 200 |
| 501–2000 | ₹8 per unit on total units |
| Above 2000 | ₹10 per unit on total units |

### Commercial Connection

| Units Consumed | Rate per Unit |
|---|---:|
| Up to 500 | ₹6 |
| 501–1000 | ₹9 |
| 1001–5000 | ₹12 |
| Above 5000 | ₹15 |


## ▶️ How to Run
1. Install Python 3.
2. Save the program as `electricity_bill.py`.
3. Open a terminal in the file's directory.
4. Run the command:
   "python electricity_bill.py"
5. Enter the connection type and units consumed on separate lines.

## 🧪 Sample Input

Non Commercial Connection
300


## Sample Output

total_bill:₹ 400


## 📚 Concepts Learned
- Python input and type conversion
- Nested conditional statements
- Comparison operators
- Arithmetic calculations
- Implementing rule-based billing logic

## 🔮 Future Improvements
- Validate connection types and unit inputs.
- Handle negative units and invalid entries.
- Add support for additional connection types.
- Improve the billing logic with configurable tariff slabs.

## 👩‍💻 Author
Deepa Ramesh

## 📄 License
This project is intended for educational and learning purposes.
