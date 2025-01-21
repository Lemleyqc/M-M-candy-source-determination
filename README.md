# M&M Candy Source Determination

This repository contains the solution to determine the source of M&M candies based on observed color distributions. The candies are manufactured in two plants (Cleveland and Hackettstown), and their color distributions differ. The goal is to identify the most likely source using statistical methods.

---

## Repository Structure

1. **README.md** (this file): Provides an overview of the solution and repository structure.
2. **solution.py**: Python implementation of the Maximum Likelihood Estimation (MLE) method for source determination.
3. **explanation.md**: Detailed explanation of the problem, methodology, and solution process.
4. **bonus.md**: Analysis of the flaws in using Chi-Square testing for this problem and suggestions for improvement.

---

## Problem Description

M&M candies are manufactured at two plants in the US, with the following color distributions:
- **Cleveland**: Red=0.131, Orange=0.205, Yellow=0.135, Green=0.198, Blue=0.207, Brown=0.124
- **Hackettstown**: Red=0.125, Orange=0.25, Yellow=0.125, Green=0.125, Blue=0.25, Brown=0.125

The task is to determine the likely source of a batch of candies based on observed color frequencies.

---

## Methodology

We use **Maximum Likelihood Estimation (MLE)** to compare the likelihood of the observed data under both distributions. The factory with the higher likelihood is identified as the most probable source.

Additionally, we analyze why the Chi-Square testing methodology might be flawed for this task.

---

## Instructions

1. **Run the Code**: Use the `solution.py` script to input observed data and compute the source.
2. **Understand the Process**: Refer to `explanation.md` for step-by-step methodology and mathematical background.
3. **Explore Bonus Analysis**: Check `bonus.md` for insights into the limitations of alternative methods.

---

## Example Output
When running `solution.py` with the observed data:
```python
observed = {'Red': 50, 'Orange': 100, 'Yellow': 30, 'Green': 40, 'Blue': 120, 'Brown': 60}
```
The output is:
```
Candies are more likely from Hackettstown.
```
This demonstrates that the observed data aligns more closely with the Hackettstown distribution.

---

