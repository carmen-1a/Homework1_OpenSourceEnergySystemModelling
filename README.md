
# Homework1_OpenSourceEnergySystemModelling
Homework 1 17.03.2026 TU WIEN

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

### (Simplified) Electricity Price Calculator

The code calculates the current grid fee for electricity in Carinthia on NE 7.

The main function controls the program flow and asks the user for:

- the current month (1–12)
- the current hour (0–23)

Based on these two inputs, it checks whether the SNAP discount is active, which stands for Sommerniedrigarbeitspreis.
The discount is active only if:

- the month is between April and September
- the time is between 10:00 and 16:00

If SNAP is active, the grid fee is reduced by 20%. 
Otherwise, the normal grid fee is applied.

The function "current_grid_fee" calculates the grid fee, the function "get_valid_number" checks the user input and repeatedly asks for a value within the allowed range.

After the input, the program prints:

- the current grid fee in cent / kWh
- whether the SNAP discount is active or not

### Information regarding the use of AI
AI tools such as ChatGPT and Claude were used in this project mainly to simplify and then debug an existing codebase (the Electricity Price Calculator), to develop code for test.yml, and to develop code for the testing file (test_el_price_calculator.py). They were also used to research and better understand the pushing process and the setup in VS Code. 
The workflow was as follows: existing code and development problems were described to the AI tools, which then provided suggestions for code simplification, debugging, and file generation. These suggestions were reviewed, adapted where necessary, and then integrated into the project.