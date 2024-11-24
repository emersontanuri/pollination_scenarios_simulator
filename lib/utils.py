from scipy.stats import norm
import numpy as np

def generate_positive_sample(mean, std, size=1):
  """Gera valores positivos de uma distribuição normal."""
  existing_samples = []
  samples_needed = size - len(existing_samples)
  
  while samples_needed > 0:
    new_samples = norm.rvs(mean, std, size=samples_needed)
    new_samples = np.where(new_samples > 0, new_samples, new_samples)

    existing_samples = np.append(existing_samples, new_samples)

    samples_needed = size - len(existing_samples)
    
  return existing_samples
