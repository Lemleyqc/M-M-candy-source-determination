# Explanation: Determining the Source of M&M Candies

## Problem Description
M&M candies are produced at two different plants in the US, with different color distributions:
- **Cleveland**: Red=0.131, Orange=0.205, Yellow=0.135, Green=0.198, Blue=0.207, Brown=0.124
- **Hackettstown**: Red=0.125, Orange=0.25, Yellow=0.125, Green=0.125, Blue=0.25, Brown=0.125

The goal is to determine the likely source of a batch of candies using statistical testing based on observed color frequencies.

---

## Methodology: Maximum Likelihood Estimation (MLE)
### Why MLE?
MLE is chosen because it directly estimates which factory is more likely to have produced the candies based on observed data. Unlike Chi-Square testing, MLE focuses on maximizing the probability of the observed data given the theoretical distributions.

### Steps:
1. **Observed Data**:
   Collect the observed frequencies for each color in a sample of candies.

2. **Theoretical Distributions**:
   Use the color distributions provided for Cleveland and Hackettstown factories as theoretical models.

3. **Likelihood Calculation**:
   Compute the likelihood of the observed data for each factory:
   \[
   P = \prod_{i=1}^{n} p_i^{O_i}
   \]
   - \(p_i\): Probability of color \(i\) from the factory distribution.
   - \(O_i\): Observed frequency of color \(i\).

4. **Log-Likelihood**:
   To simplify computation and avoid numerical underflow, compute the log-likelihood:
   \[
   \log P = \sum_{i=1}^n O_i \cdot \log(p_i)
   \]

5. **Comparison**:
   Compare the log-likelihoods for Cleveland and Hackettstown. The factory with the higher log-likelihood is the most probable source.

---

## Example Calculation
- **Observed Data**: {'Red': 50, 'Orange': 100, 'Yellow': 30, 'Green': 40, 'Blue': 120, 'Brown': 60}
- **Cleveland Distribution**: {'Red': 0.131, 'Orange': 0.205, 'Yellow': 0.135, 'Green': 0.198, 'Blue': 0.207, 'Brown': 0.124}
- **Hackettstown Distribution**: {'Red': 0.125, 'Orange': 0.25, 'Yellow': 0.125, 'Green': 0.125, 'Blue': 0.25, 'Brown': 0.125}

Using the Python implementation in `solution.py`, the log-likelihoods are computed, and the source is determined based on the higher value.

### **Output of the Code**:
```
Candies are more likely from Hackettstown.
```

---

## Advantages of MLE
1. **Directly Addresses the Problem**:
   Focuses on probability estimation rather than distributional fit.

2. **Numerical Stability**:
   Log-likelihood avoids numerical issues with small probabilities.

3. **Scalability**:
   Easily extended to more complex models or additional variables.

---

## Conclusion
MLE is a robust and reliable method for determining the source of M&M candies, providing clear and interpretable results without the limitations of alternative methods like Chi-Square testing.
