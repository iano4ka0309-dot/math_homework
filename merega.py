
priors = [0.5, 0.3, 0.2]
conversions = [0.04, 0.02, 0.08]   
labels = ["Пошукова реклама", "Соцмережі", "Email-розсилка"]

def bayes_source(prior_probs, conversion_rates):
    weighted_probs = []
    for p, c in zip(prior_probs, conversion_rates):
        weighted_probs.append(p * c)
    return weighted_probs

weighted_probs = bayes_source(priors, conversions)

total_p_a = sum (weighted_probs)

result = list(map(lambda x: x / total_p_a, weighted_probs))

print(f"--- Загальна ймовірність покупки: {total_p_a:.1%} ---")
for name, prob in zip(labels, result):
    print(f"Ймовірність, що покупець прийшов через {name}: {prob:.2%}")






