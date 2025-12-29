# Discrete-Time Derivatives Pricing Framework (Python)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📌 Project Overview

This repository contains a collection of foundational quantitative finance models implemented in Python, specifically focusing on derivatives pricing under **discrete-time frameworks**.

The primary goal of this project is to demonstrate:
1.  **Strong understanding of No-Arbitrage Pricing Theory.**
2.  **Translation of financial mathematics** into clean, modular, and maintainable code.
3.  **Practical implementation** of dynamic programming and lattice methods (Binomial Trees).

This codebase is designed to be **interview-ready** for Quantitative Finance, Trading, and Research roles, showcasing explicit risk-neutral valuation logic without relying on "black-box" libraries.

---

## 📂 Repository Scope & Structure

The project implements a flexible **Binomial Tree pricing engine** covering Vanilla (American) and Path-dependent (Barrier) derivatives. Each module is written to be independent, transparent, and extendable.

```text
quant-finance-projects/
├── binomial_tree.py
│   └── Core binomial tree engine and backward induction logic.
│
├── binomial_asset_pricing_parameters.py
│   └── Construction of CRR (Cox-Ross-Rubinstein) parameters (u, d, p)
│       under the risk-neutral measure.
│
├── american_option.py
│   └── American option pricing model with optimal early exercise logic.
│
├── barrier_option_pricing.py
│   └── Barrier option pricing handling path-dependent payoff conditions.
│
└── README.md
## Author
Chanyapon Trongjaroenchai
