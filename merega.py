priors = [0.5, 0.3, 0.2]
conversions = [0.04, 0.02, 0.08]
labels = ["Пошукова реклама", "Соцмережі", "Email-розсилка"]

def bayes_source(prior_probs, conversion_rates):
    weighted = [p * c for p, c in zip(prior_probs, conversion_rates)]
    total = sum(weighted)
    posterior = [w / total for w in weighted]
    return posterior

posterior = bayes_source(priors, conversions)
total_p_a = sum([p * c for p, c in zip(priors, conversions)])

print(f"--- Загальна ймовірність покупки: {total_p_a:.1%} ---")
for name, prob in zip(labels, posterior):
    print(f"Ймовірність, що покупець прийшов через {name}: {prob:.2%}")





