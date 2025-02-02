# simulation_function.py

import random
import datetime

# --------------------------
# A/B Testing and Forecasting Simulations
# --------------------------

def simulate_price_reduction(product: str, reduction_percent: float) -> str:
    """
    Simulate the impact on revenue when reducing the price of a product.
    
    Args:
        product: Name of the product.
        reduction_percent: The percentage reduction in price.
        
    Returns:
        A string describing the estimated revenue impact.
    """
    # Simulate revenue impact: a price reduction could boost volume but lower margin.
    # Here we simulate a net revenue change percentage.
    volume_increase = random.uniform(5, 15)  # percentage increase in volume
    margin_drop = reduction_percent * random.uniform(0.8, 1.2)  # effective margin loss
    net_impact = volume_increase - margin_drop  # simplistic net effect
    if net_impact >= 0:
        return (f"Simulating a {reduction_percent}% price reduction on {product} may increase revenue by "
                f"approximately {net_impact:.2f}% due to a volume boost of {volume_increase:.2f}% offsetting a margin drop of {margin_drop:.2f}%.")
    else:
        return (f"Simulating a {reduction_percent}% price reduction on {product} may decrease revenue by "
                f"approximately {abs(net_impact):.2f}% due to a significant margin drop despite a volume boost of {volume_increase:.2f}%.")


def simulate_digital_promotion_budget_increase(budget_increase: float) -> str:
    """
    Simulate the expected lift in sales when increasing the digital promotion budget.
    
    Args:
        budget_increase: The percentage increase in budget.
        
    Returns:
        A string with the forecasted sales lift.
    """
    # Assume a multiplier effect: each 1% extra budget can lift sales by 0.5% to 1.5%.
    lift_factor = random.uniform(0.5, 1.5)
    sales_lift = budget_increase * lift_factor
    return (f"Increasing the digital promotions budget by {budget_increase}% is expected to lift sales by approximately "
            f"{sales_lift:.2f}% based on current digital engagement trends.")


def simulate_ab_test_discount_strategies(strategy1: str, strategy2: str) -> str:
    """
    Simulate an A/B test comparing two discount strategies.
    
    Args:
        strategy1: Description of the first discount strategy.
        strategy2: Description of the second discount strategy.
        
    Returns:
        A string summarizing the projected sales impact difference.
    """
    # Simulate projected sales lift for each strategy
    lift_strategy1 = random.uniform(5, 15)
    lift_strategy2 = random.uniform(5, 15)
    
    # Compare the two lifts
    if lift_strategy1 > lift_strategy2:
        better_strategy = strategy1
        difference = lift_strategy1 - lift_strategy2
    else:
        better_strategy = strategy2
        difference = lift_strategy2 - lift_strategy1
        
    return (f"Simulated A/B Test Results:\n"
            f"- {strategy1}: Projected sales lift of {lift_strategy1:.2f}%\n"
            f"- {strategy2}: Projected sales lift of {lift_strategy2:.2f}%\n"
            f"Recommendation: {better_strategy} appears to be better by approximately {difference:.2f}%.")


def predict_next_month_sales(sku: str) -> str:
    """
    Predict next month's sales for a given SKU based on past 12 months' trends.
    
    Args:
        sku: The SKU for which to forecast sales.
        
    Returns:
        A string with the sales prediction.
    """
    # For demonstration, we simulate sales prediction with a base value and random trend factor.
    base_sales = random.randint(5000, 20000)
    trend_factor = random.uniform(0.95, 1.05)  # slight variation month-over-month
    predicted_sales = base_sales * trend_factor
    return (f"Based on the past 12 months' trends, the predicted sales for SKU {sku} next month are approximately "
            f"{predicted_sales:.0f} units.")


def simulate_removing_low_performing_sku(category: str) -> str:
    """
    Simulate the impact on total category sales when removing a low-performing SKU.
    
    Args:
        category: The product category being analyzed.
        
    Returns:
        A string summarizing the impact on category sales.
    """
    # Simulate an improvement in overall category performance after removing a low-performing SKU.
    improvement = random.uniform(2, 8)  # percentage improvement
    return (f"Removing the low-performing SKU from the {category} category could potentially improve total category sales by "
            f"around {improvement:.2f}% due to a reallocation of consumer focus towards higher-performing items.")


# --------------------------
# Market Disruptions & Supply Chain Simulations
# --------------------------

def simulate_competitor_launch(competitor_price_difference: float) -> str:
    """
    Simulate the impact on sales when a competitor launches a similar product at a lower price.
    
    Args:
        competitor_price_difference: The percentage lower the competitor's price is compared to ours.
        
    Returns:
        A string summarizing the estimated impact on sales.
    """
    # A larger price gap may lead to a higher loss in market share.
    market_share_loss = competitor_price_difference * random.uniform(0.5, 1.5)
    return (f"A competitor launching a similar product at {competitor_price_difference}% lower price may result in a loss "
            f"of approximately {market_share_loss:.2f}% in market share, potentially impacting our sales significantly.")


def simulate_supply_chain_disruption(days: int) -> str:
    """
    Simulate the impact of a supply chain disruption on stock levels and revenue.
    
    Args:
        days: Duration of the disruption in days.
        
    Returns:
        A string detailing the estimated drop in stock levels and revenue.
    """
    # Assume longer disruptions cause more severe impact.
    stock_drop = random.uniform(10, 30) * days / 30  # percentage drop
    revenue_drop = random.uniform(5, 20) * days / 30  # percentage drop
    return (f"A {days}-day supply chain disruption is estimated to decrease stock levels by approximately {stock_drop:.2f}% "
            f"and revenue by around {revenue_drop:.2f}%.")


def simulate_offline_to_ecommerce_shift(shift_percentage: float) -> str:
    """
    Simulate the effect on overall sales when shifting a percentage of the offline sales budget to e-commerce.
    
    Args:
        shift_percentage: The percentage of the offline budget reallocated.
        
    Returns:
        A string describing the expected change in overall sales.
    """
    # Simulate improved e-commerce efficiency and potential cannibalization of offline sales.
    ecommerce_boost = shift_percentage * random.uniform(1.0, 2.0)
    offline_loss = shift_percentage * random.uniform(0.8, 1.5)
    net_impact = ecommerce_boost - offline_loss
    if net_impact >= 0:
        return (f"Shifting {shift_percentage}% of the offline budget to e-commerce is projected to improve overall sales by "
                f"approximately {net_impact:.2f}% due to enhanced digital channel performance.")
    else:
        return (f"Shifting {shift_percentage}% of the offline budget to e-commerce might result in a net decline of overall sales by "
                f"around {abs(net_impact):.2f}% if offline losses outweigh digital gains.")


def simulate_increase_trade_margins(margin_increase: float) -> str:
    """
    Simulate the impact of increasing trade margins for top distributors.
    
    Args:
        margin_increase: The percentage increase in trade margins.
        
    Returns:
        A string summarizing the expected effect on profitability or sales.
    """
    # Assume a margin increase can lead to improved distributor performance.
    performance_gain = margin_increase * random.uniform(0.8, 1.2)
    return (f"Increasing trade margins by {margin_increase}% for our top distributors is expected to improve their performance, "
            f"potentially increasing overall profitability by around {performance_gain:.2f}%.")


def simulate_new_competitor_impact(duration_months: int = 6) -> str:
    """
    Simulate how a new competitor entering the market would affect sales over a given period.
    
    Args:
        duration_months: The number of months over which to simulate the impact.
        
    Returns:
        A string describing the projected sales impact over the period.
    """
    # Assume the competitor gradually gains market share over time.
    monthly_impact = random.uniform(1, 3)  # percentage loss per month
    total_impact = monthly_impact * duration_months
    return (f"A new competitor entering the market could erode our sales by approximately {monthly_impact:.2f}% per month, "
            f"leading to an overall decline of about {total_impact:.2f}% over {duration_months} months.")

# --------------------------
# Example usage (for testing purposes)
# --------------------------
if __name__ == "__main__":
    # A/B Testing and Forecasting Examples
    print(simulate_price_reduction("Product X", 10))
    print(simulate_digital_promotion_budget_increase(20))
    print(simulate_ab_test_discount_strategies("Flat 10% off", "Buy 1 Get 1"))
    print(predict_next_month_sales("BEST_SELLER_001"))
    print(simulate_removing_low_performing_sku("Electronics"))
    
    # Market Disruptions & Supply Chain Examples
    print(simulate_competitor_launch(15))
    print(simulate_supply_chain_disruption(30))
    print(simulate_offline_to_ecommerce_shift(10))
    print(simulate_increase_trade_margins(5))
    print(simulate_new_competitor_impact(6))
