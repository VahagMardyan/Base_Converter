# Base & IEEE-754 Converter

A lightweight, interactive web application built with **Streamlit** and **Python** for base conversions and IEEE-754 floating-point format analysis.

---

## Key Features

- **Base Converter:** Convert numbers between custom bases (ranging from **Base 2** to **Base 36**).
  - Supports both **Signed** and **Unsigned** integers.
  - Handles **Two's Complement** representation with configurable bit-widths (8, 16, 32, 64-bit).
  - Displays instant side-by-side conversions for Binary, Quaternary, Octal, Decimal, and Hexadecimal.
- **IEEE-754 Floating-Point Analysis:**
  - **Float → Binary:** Converts any decimal float to standard **32-bit (Single Precision)** and **64-bit (Double Precision)** IEEE-754 strings.
  - **Binary → Float:** Reconstructs float values directly from raw or space-separated binary bit sequences.
  - Breaks down IEEE-754 structures into **Sign**, **Exponent**, and **Mantissa** components.

---

## Project Structure

```text
├── base_converter.py    # Core numerical conversion logic & IEEE-754 processing
├── app.py          	 # Streamlit UI implementation
├── main.py				 # Command Line Interface
└── README.md      		 # Project documentation
```
