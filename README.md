# Automotive Diagnostic Assistant

A Python-based command-line tool that simulates OEM-style automotive diagnostic workflows. This project guides users through structured troubleshooting steps to identify potential vehicle faults and recommend next actions.

## 🚗 Overview

This tool is designed to replicate how dealership technicians and support specialists diagnose vehicle issues using step-by-step logic, similar to real-world repair manuals and diagnostic systems.

## ✨ Features

* Interactive command-line diagnostic assistant
* Decision-tree-based troubleshooting system
* Simulates real automotive diagnostic workflows
* Case logging system for tracking issues and resolutions
* Handles incomplete data and escalation scenarios

## 🛠️ Technologies Used

* Python
* JSON (for case logging and data storage)

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/automotive-diagnostic-assistant.git
   ```

2. Navigate into the folder:

   ```bash
   cd automotive-diagnostic-assistant
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## 🧪 Example Use Case

```
Select issue:
1. Car won't start

Does the engine crank? (y/n): n
Are dashboard lights dim or off? (y/n): y

=== DIAGNOSIS RESULT ===
Battery voltage may be below operating threshold. Recommend testing and replacement if necessary.
```

## 📂 Project Structure

* `main.py` → CLI interface and diagnostic engine
* `diagnostics.py` → Decision tree logic
* `cases.json` → Logged diagnostic cases

## 📈 Future Improvements

* Add support for OBD-II error codes
* Expand diagnostic scenarios (engine, transmission, sensors)
* Web-based interface for easier interaction
* Integration with real vehicle data sources

## 🎯 Purpose

This project was built to demonstrate structured problem-solving, diagnostic reasoning, and the ability to simulate real-world automotive support workflows.

