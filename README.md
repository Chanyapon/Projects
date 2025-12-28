# American Option Pricing (Binomial Tree Model)

This project implements pricing for **American-style options**, which allow early exercise before maturity.

---

## Overview
The model uses a **Binomial Tree framework** to evaluate the option value at each node and determine the optimal early exercise strategy.
The pricing follows a risk-neutral valuation framework under discrete-time dynamics.

---

## Key Features
- Early exercise decision logic
- Risk-neutral valuation
- Backward induction through binomial tree

---

## Methods
- Cox–Ross–Rubinstein (CRR) Binomial Tree
- Dynamic programming

---

## Tech Stack
- Python
- NumPy

---

## Usage
1. Set option parameters (S, K, r, sigma, T)
2. Run the pricing script
3. The model outputs the American option price using backward induction

---

## Output
- American option price
- Comparison with European option pricing

---

## Author
Chanyapon Trongjaroenchai
