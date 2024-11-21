from scipy.stats import norm

def generate_positive_sample(mean, std):
    """Gera um valor positivo de uma distribuição normal."""
    sample = norm.rvs(mean, std)
    while sample <= 0:
        sample = norm.rvs(mean, std)
    return sample