# solution.py: Determine the source of M&M candies using Maximum Likelihood Estimation (MLE)

import math

# Observed data (example): Frequency of each color in the sample
observed = {'Red': 50, 'Orange': 100, 'Yellow': 30, 'Green': 40, 'Blue': 120, 'Brown': 60}

# Factory distributions
cleveland = {'Red': 0.131, 'Orange': 0.205, 'Yellow': 0.135, 'Green': 0.198, 'Blue': 0.207, 'Brown': 0.124}
hackettstown = {'Red': 0.125, 'Orange': 0.25, 'Yellow': 0.125, 'Green': 0.125, 'Blue': 0.25, 'Brown': 0.125}

# Calculate log-likelihood for a given distribution
def log_likelihood(observed, distribution):
    return sum(observed[color] * math.log(distribution[color]) for color in observed)

# Compute log-likelihoods for both factories
log_likelihood_cleveland = log_likelihood(observed, cleveland)
log_likelihood_hackettstown = log_likelihood(observed, hackettstown)

# Determine the source
if log_likelihood_cleveland > log_likelihood_hackettstown:
    print("Candies are more likely from Cleveland.")
else:
    print("Candies are more likely from Hackettstown.")
