from scipy.optimize import minimize_scalar

def find_optimal_price(cost, max_demand, demand_slope, price_range):
    
    def profit(x):
        return (x - cost) * (max_demand - demand_slope * x)
    
    def negative_profit(x):
        return -profit(x)
    
    result = minimize_scalar(negative_profit, bounds=price_range, method='bounded')
    
    optimal_price = result.x
    max_profit = profit(optimal_price)
    
    print(f"Оптимальна ціна: {optimal_price:.2f} грн")
    print(f"Максимальний прибуток: {max_profit:.2f} грн")
    
    
    analytical_price = 1650
    analytical_profit = 578000
    print(f"\nПорівняння:")
    print(f"Аналітична ціна:  {analytical_price} грн")
    print(f"Чисельна ціна:    {optimal_price:.2f} грн")
    print(f"Збігаються: {abs(analytical_price - optimal_price) < 0.01}")

find_optimal_price(cost=800, max_demand=2000, demand_slope=0.8, price_range=(800, 2500))
