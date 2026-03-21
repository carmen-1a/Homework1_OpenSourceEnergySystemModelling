# Homework1_OpenSourceEnergySystemModelling
Homework 1 17.03.2026 TU WIEN
![Badge](https://img.shields.io/badge/test_badge)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Electricity Price Calculator

The code calculates the current grid fee for electricity in Kärnten on NE 7.

The main function asks the user for:

- the current month (1–12)
- the current hour (0–23)

Based on these two inputs, it checks whether the SNAP discount is active, which stans for Sommerniedrigarbeitspreis.
The discount is active only if:

- the month is between April and September
- the time is between 10:00 and 16:00

If SNAP is active, the grid fee is reduced by 20%. 
Otherwise, the normal grid fee is applied.

After the input, the program prints:

- the current grid fee in cent / kWh
- whether the SNAP discount is active or not

