# Transaction Summary

A Python solution that summarizes financial transactions by calculating the net balance for each user.

## Problem

Given a list of transaction records, where each record contains a username and a transaction amount, calculate the total net amount for every user.

Positive amounts represent money received, while negative amounts represent money spent.

### Example

```python
transactions = [
    ("ali", 120),
    ("sara", 200),
    ("ali", 80),
    ("hamza", 150),
    ("sara", 50),
    ("ali", -20),
]
```

The expected result is:

```python
{
    "ali": 180,
    "sara": 250,
    "hamza": 150
}
```

### Calculation

```text
Ali:   120 + 80 - 20 = 180
Sara:  200 + 50      = 250
Hamza: 150           = 150
```

## Approach

The solution uses a Python dictionary to store the accumulated balance for each user.

For every transaction:

1. Extract the username and amount.
2. Check whether the user already exists in the dictionary.
3. If the user does not exist, initialize their balance with the transaction amount.
4. If the user already exists, add the transaction amount to their existing balance.

This allows all transactions to be processed in a single pass.

## Project Structure

```text
.
├── main.py
├── README.md
└── LICENSE
```

## Requirements

* Python 3.x
* No external libraries are required.

The project uses only Python's standard library.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/mwchuchu/transaction_summary
```

### 2. Navigate to the project directory

```bash
cd transaction_summary
```

### 3. Run the program

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

No additional dependencies or virtual environment are required.

## Complexity

### Time Complexity

```text
O(n)
```

Each transaction is processed once.

### Space Complexity

```text
O(u)
```

where `u` is the number of unique users.

The dictionary stores one entry for each unique user.

## Edge Cases

The solution handles cases such as:

### Empty transactions

```python
[]
```

Output:

```python
{}
```

### Single transaction

```python
[("ali", 100)]
```

Output:

```python
{"ali": 100}
```

### Negative balance

```python
[("ali", -100)]
```

Output:

```python
{"ali": -100}
```

### Transactions that cancel each other

```python
[
    ("ali", 100),
    ("ali", -100)
]
```

Output:

```python
{"ali": 0}
```

## Key Concepts Practiced

* Python dictionaries
* Tuples
* Iteration
* Conditional logic
* Data aggregation
* Handling repeated records
* Time and space complexity
* Edge-case handling

## License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.
