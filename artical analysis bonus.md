# Bonus: Analysis of Chi-Square Testing Flaws

## Problem Context
In the original problem, Chi-Square testing is suggested as a method to determine the source of M&M candies. However, this methodology has inherent flaws that make it less suitable for the given task.

---

## Limitations of Chi-Square Testing

### 1. **Independence Assumption**
Chi-Square testing assumes that all observations (i.e., the color of each candy) are independent. This assumption may not hold in the context of candy packaging:
- Candy colors in a single package might not be randomly distributed due to manufacturing or packaging processes.
- For example, certain batches might have slight color biases or correlations.

Violation of the independence assumption can lead to inaccurate Chi-Square test results.

---

### 2. **Small Sample Size Issue**
Chi-Square testing requires that the expected frequency for each category (color) is sufficiently large. The rule of thumb is that each expected frequency should be at least 5:
- If the sample size is small or if some colors have low probabilities, the expected frequencies may fall below this threshold.
- This can invalidate the test results or make them unreliable.

In contrast, MLE can handle smaller sample sizes more gracefully.

---

### 3. **Dynamic Distribution Changes**
The color distributions for Cleveland and Hackettstown are assumed to be constant. However, in reality:
- Manufacturing plants might adjust their color distributions over time.
- If the theoretical distributions used for Chi-Square testing are outdated, the results will be biased.

MLE can partially mitigate this issue by focusing on observed data likelihood rather than theoretical fit.

---

### 4. **Chi-Square Testing Focuses on Fit, Not Likelihood**
Chi-Square testing is designed to test whether observed data fits a theoretical distribution. It does not provide a direct way to compare two competing hypotheses (e.g., whether the candies come from Cleveland or Hackettstown).

In contrast, MLE explicitly compares the likelihood of the observed data under two different hypotheses, making it better suited for this task.

---

## Bonus Addition: Demonstration Output
To illustrate the practical issues with Chi-Square testing, consider running the `solution.py` script with observed data:

**Observed Data Example**:
```
{'Red': 50, 'Orange': 100, 'Yellow': 30, 'Green': 40, 'Blue': 120, 'Brown': 60}
```

### Output:
```
Candies are more likely from Hackettstown.
```
This aligns with the MLE result, where likelihood comparison directly addresses the problem.

---

## Conclusion
While Chi-Square testing is a useful statistical tool in many contexts, its assumptions and limitations make it less appropriate for determining the source of M&M candies in this problem. Maximum Likelihood Estimation (MLE) offers a more robust and direct approach to solving the problem.

For more details on the methodology, refer to the `explanation.md` file.
