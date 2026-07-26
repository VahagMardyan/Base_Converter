# Base & IEEE-754 Converter

A lightweight, interactive web and CLI application built with **Streamlit** and **Python** for base conversions and IEEE-754 floating-point format analysis.

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
├── alpha.py			 # Show Base 36 Character Mapping (A=10, B=11 ... Z=35)
├── app.py               # Streamlit UI implementation
├── main.py              # Command Line Interface
└── README.md            # Project documentation
```

---

## Requirements

* Python 3.10 or above
* Streamlit 1.59.2 or above (*Only required for the Web Interface*)

---

## Installation

1. Navigate to the project directory:

```bash
cd Converter
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

* **Windows (PowerShell/CMD):**

```cmd
.venv\Scripts\activate
```

* **Linux / macOS:**

```bash
source .venv/bin/activate
```

4. Install Streamlit (optional for Web UI):

```bash
pip install streamlit
```

---

Running the Application

* **CLI Interface:**

```bash
python main.py
```

* **Web Interface:**

```bash
streamlit run app.py
```

## Testing Web Application

Visit [this page ](https://baseconverter-vahagmardyan.streamlit.app/)to use this converter from any device.
