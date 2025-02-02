from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action, Tracker
from typing import Any, Dict, List
from rasa_sdk import Action, Tracker

from actions.simulation_function import (
    simulate_price_reduction,
    simulate_digital_promotion_budget_increase,
    simulate_ab_test_discount_strategies,
    predict_next_month_sales,
    simulate_removing_low_performing_sku,
    simulate_competitor_launch,
    simulate_supply_chain_disruption,
    simulate_offline_to_ecommerce_shift,
    simulate_increase_trade_margins,
    simulate_new_competitor_impact
)
# Import your analytics functions
from actions.analytics_function import (
    get_sales_data_for_quarter,
    compare_sales,
    get_yoy_sales_growth,
    get_highest_growth_categories,
    get_top_skus_by_revenue,
    get_average_sales_per_store,
    compare_brands_in_region,
    get_roi_data_for_promotions,
    identify_highest_roi_promotion,
    get_incremental_sales_by_promotion,
    get_retention_data_for_promotions,
    identify_highest_retention_promotion,
    calculate_promotion_cannibalization,
    get_sales_data_for_campaign
)

# ------------------ Actions from rules.yml ------------------

class ActionCompareSales(Action):
    def name(self) -> str:
        return "action_compare_sales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Example: compare Q1 vs Q2 sales; modify as needed.
        q1_sales = get_sales_data_for_quarter("Q1")
        q2_sales = get_sales_data_for_quarter("Q2")
        comparison = compare_sales(q1_sales, q2_sales)
        dispatcher.utter_message(text=f"Sales comparison between Q1 and Q2: {comparison}")
        return []


class ActionGetYoySalesGrowth(Action):
    def name(self) -> str:
        return "action_get_yoy_sales_growth"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        yoy_growth = get_yoy_sales_growth()
        dispatcher.utter_message(text=f"Year-over-Year sales growth: {yoy_growth}")
        return []


class ActionGetHighestGrowthCategories(Action):
    def name(self) -> str:
        return "action_get_highest_growth_categories"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        yoy_growth = get_yoy_sales_growth()
        highest_growth = get_highest_growth_categories(yoy_growth)
        dispatcher.utter_message(text=f"Highest growth categories: {highest_growth}")
        return []


class ActionGetTopSkusByRevenue(Action):
    def name(self) -> str:
        return "action_get_top_skus_by_revenue"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        top_skus = get_top_skus_by_revenue()
        dispatcher.utter_message(text=f"Top SKUs by revenue: {top_skus}")
        return []


class ActionGetAverageSalesPerStore(Action):
    def name(self) -> str:
        return "action_get_average_sales_per_store"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        avg_sales = get_average_sales_per_store()
        dispatcher.utter_message(text=f"Average sales per store: {avg_sales}")
        return []


class ActionCompareBrandsInRegion(Action):
    def name(self) -> str:
        return "action_compare_brands_in_region"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Example uses the "South" region; adjust as needed.
        comparison = compare_brands_in_region("South")
        dispatcher.utter_message(text=f"Brand comparison in South region: {comparison}")
        return []


class ActionGetROIDataForPromotions(Action):
    def name(self) -> str:
        return "action_get_roi_data_for_promotions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        roi_data = get_roi_data_for_promotions()
        dispatcher.utter_message(text=f"ROI data for promotions: {roi_data}")
        return []


class ActionIdentifyHighestROIPromotion(Action):
    def name(self) -> str:
        return "action_identify_highest_roi_promotion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        roi_data = get_roi_data_for_promotions()
        highest_roi = identify_highest_roi_promotion(roi_data)
        dispatcher.utter_message(text=f"Highest ROI promotion: {highest_roi}")
        return []


class ActionGetIncrementalSalesByPromotion(Action):
    def name(self) -> str:
        return "action_get_incremental_sales_by_promotion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        incremental_sales = get_incremental_sales_by_promotion()
        dispatcher.utter_message(text=f"Incremental sales by promotion: {incremental_sales}")
        return []


class ActionGetRetentionDataForPromotions(Action):
    def name(self) -> str:
        return "action_get_retention_data_for_promotions"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        retention_data = get_retention_data_for_promotions()
        dispatcher.utter_message(text=f"Retention data for promotions: {retention_data}")
        return []


class ActionIdentifyHighestRetentionPromotion(Action):
    def name(self) -> str:
        return "action_identify_highest_retention_promotion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        retention_data = get_retention_data_for_promotions()
        highest_retention = identify_highest_retention_promotion(retention_data)
        dispatcher.utter_message(text=f"Highest retention promotion: {highest_retention}")
        return []


class ActionCalculatePromotionCannibalization(Action):
    def name(self) -> str:
        return "action_calculate_promotion_cannibalization"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        cannibalization = calculate_promotion_cannibalization()
        dispatcher.utter_message(text=f"Promotion cannibalization: {cannibalization}%")
        return []


class ActionGetSalesDataForCampaign(Action):
    def name(self) -> str:
        return "action_get_sales_data_for_campaign"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Example: using "Campaign" as the campaign name; modify as needed.
        campaign_data = get_sales_data_for_campaign("Campaign")
        dispatcher.utter_message(text=f"Sales data for campaign: {campaign_data}")
        return []

# ------------------ Actions from stories.yml ------------------

class ActionYoyGrowth(Action):
    def name(self) -> str:
        return "action_yoy_growth"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        yoy_growth = get_yoy_sales_growth()
        dispatcher.utter_message(text=f"YoY growth details: {yoy_growth}")
        return []


class ActionTopSkus(Action):
    def name(self) -> str:
        return "action_top_skus"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        top_skus = get_top_skus_by_revenue()
        dispatcher.utter_message(text=f"Top SKUs: {top_skus}")
        return []


class ActionAvgSales(Action):
    def name(self) -> str:
        return "action_avg_sales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        avg_sales = get_average_sales_per_store()
        dispatcher.utter_message(text=f"Average sales per store: {avg_sales}")
        return []


class ActionCompareBrands(Action):
    def name(self) -> str:
        return "action_compare_brands"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Example: using the "South" region.
        comparison = compare_brands_in_region("South")
        dispatcher.utter_message(text=f"Brand comparison: {comparison}")
        return []


class ActionIncrementalSales(Action):
    def name(self) -> str:
        return "action_incremental_sales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        incremental_sales = get_incremental_sales_by_promotion()
        dispatcher.utter_message(text=f"Incremental sales: {incremental_sales}")
        return []


class ActionRetention(Action):
    def name(self) -> str:
        return "action_retention"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        retention_data = get_retention_data_for_promotions()
        highest_retention = identify_highest_retention_promotion(retention_data)
        dispatcher.utter_message(text=f"Retention promotion details: {highest_retention}")
        return []


class ActionCannibalization(Action):
    def name(self) -> str:
        return "action_cannibalization"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        cannibalization = calculate_promotion_cannibalization()
        dispatcher.utter_message(text=f"Cannibalization percentage: {cannibalization}%")
        return []


class ActionCampaignSales(Action):
    def name(self) -> str:
        return "action_campaign_sales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Example: using "Campaign" as the campaign name; modify as needed.
        campaign_sales = get_sales_data_for_campaign("Campaign")
        dispatcher.utter_message(text=f"Campaign sales data: {campaign_sales}")
        return []


class UtterSimulationNotAvailable(Action):
    def name(self) -> str:
        return "utter_simulation_not_available"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        dispatcher.utter_message(text="Simulation is not available at the moment.")
        return []


# ------------------ Existing Actions from your provided snippet ------------------

class ActionTotalSalesComparisonQ4(Action):
    def name(self) -> str:
        return "action_total_sales_comparison_q4"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        q4_sales = get_sales_data_for_quarter("Q4")
        q3_sales = get_sales_data_for_quarter("Q3")
        comparison = compare_sales(q4_sales, q3_sales)
        dispatcher.utter_message(text=f"Total sales comparison between Q4 and Q3: {comparison}")
        return []


class ActionHighestSalesGrowthYoY(Action):
    def name(self) -> str:
        return "action_highest_sales_growth_yoy"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        yoy_growth = get_yoy_sales_growth()
        highest_growth = get_highest_growth_categories(yoy_growth)
        dispatcher.utter_message(text=f"Product categories with the highest YoY growth: {highest_growth}")
        return []


class ActionTopSkus80PercentRevenue(Action):
    def name(self) -> str:
        return "action_top_skus_80_percent_revenue"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        top_skus = get_top_skus_by_revenue()
        dispatcher.utter_message(text=f"Top 5 SKUs contributing to 80% of revenue: {top_skus}")
        return []


class ActionAverageSalesPerStore(Action):
    def name(self) -> str:
        return "action_average_sales_per_store"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        avg_sales = get_average_sales_per_store()
        dispatcher.utter_message(text=f"Average sales per store for our top-performing products: {avg_sales}")
        return []


class ActionBrandComparisonSalesSouth(Action):
    def name(self) -> str:
        return "action_brand_comparison_sales_south"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        comparison = compare_brands_in_region("South")
        dispatcher.utter_message(text=f"Brand comparison in the South region: {comparison}")
        return []


class ActionHighestROIPromotionQtr(Action):
    def name(self) -> str:
        return "action_highest_roi_promotion_qtr"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        roi_data = get_roi_data_for_promotions()
        highest_roi = identify_highest_roi_promotion(roi_data)
        dispatcher.utter_message(text=f"The most effective promotion based on ROI is: {highest_roi}")
        return []


class ActionIncrementalSalesBreakdown(Action):
    def name(self) -> str:
        return "action_incremental_sales_breakdown"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        incremental_sales = get_incremental_sales_by_promotion()
        dispatcher.utter_message(text=f"Incremental sales breakdown (Discount vs. Bundling): {incremental_sales}")
        return []


class ActionHighestRetentionPromotion(Action):
    def name(self) -> str:
        return "action_highest_retention_promotion"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        retention_data = get_retention_data_for_promotions()
        highest_retention = identify_highest_retention_promotion(retention_data)
        dispatcher.utter_message(text=f"Promotions that led to the highest customer retention: {highest_retention}")
        return []


class ActionPromotionCannibalization(Action):
    def name(self) -> str:
        return "action_promotion_cannibalization"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        cannibalization = calculate_promotion_cannibalization()
        dispatcher.utter_message(text=f"The percentage of promotions leading to cannibalization: {cannibalization}%")
        return []


class ActionDiwaliCampaignPerformance(Action):
    def name(self) -> str:
        return "action_diwali_campaign_performance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        diwali_data = get_sales_data_for_campaign("Diwali")
        dispatcher.utter_message(text=f"Sales performance before, during, and after the Diwali campaign: {diwali_data}")
        return []


class ActionAskAvgSales(Action):
    def name(self) -> str:
        return "action_ask_avg_sales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        avg_sales = get_average_sales_per_store()
        dispatcher.utter_message(text=f"The average sales per store is: {avg_sales}")
        return []


class ActionAskBrandComparison(Action):
    def name(self) -> str:
        return "action_ask_brand_comparison"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        comparison = compare_brands_in_region("South")
        dispatcher.utter_message(text=f"Brand comparison result: {comparison}")
        return []


class ActionAskDiwaliPerformance(Action):
    def name(self) -> str:
        return "action_ask_diwali_performance"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        diwali_data = get_sales_data_for_campaign("Diwali")
        dispatcher.utter_message(text=f"Diwali campaign performance: {diwali_data}")
        return []


class ActionAskHighestGrowth(Action):
    def name(self) -> str:
        return "action_ask_highest_growth"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        yoy_growth = get_yoy_sales_growth()
        highest_growth = get_highest_growth_categories(yoy_growth)
        dispatcher.utter_message(text=f"Categories with the highest growth: {highest_growth}")
        return []


class ActionAskHighestRetention(Action):
    def name(self) -> str:
        return "action_ask_highest_retention"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        retention_data = get_retention_data_for_promotions()
        highest_retention = identify_highest_retention_promotion(retention_data)
        dispatcher.utter_message(text=f"Highest retention promotion: {highest_retention}")
        return []


class ActionAskHighestROI(Action):
    def name(self) -> str:
        return "action_ask_highest_roi"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        roi_data = get_roi_data_for_promotions()
        highest_roi = identify_highest_roi_promotion(roi_data)
        dispatcher.utter_message(text=f"Highest ROI promotion: {highest_roi}")
        return []


class ActionAskIncrementalSales(Action):
    def name(self) -> str:
        return "action_ask_incremental_sales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        incremental_sales = get_incremental_sales_by_promotion()
        dispatcher.utter_message(text=f"Incremental sales breakdown: {incremental_sales}")
        return []


class ActionAskPromotionCannibalization(Action):
    def name(self) -> str:
        return "action_ask_promotion_cannibalization"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        cannibalization = calculate_promotion_cannibalization()
        dispatcher.utter_message(text=f"Promotion cannibalization percentage: {cannibalization}%")
        return []


class ActionAskSalesComparison(Action):
    def name(self) -> str:
        return "action_ask_sales_comparison"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        q4_sales = get_sales_data_for_quarter("Q4")
        q3_sales = get_sales_data_for_quarter("Q3")
        comparison = compare_sales(q4_sales, q3_sales)
        dispatcher.utter_message(text=f"Sales comparison (Q4 vs. Q3): {comparison}")
        return []


class ActionAskTopSkus(Action):
    def name(self) -> str:
        return "action_ask_top_skus"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        top_skus = get_top_skus_by_revenue()
        dispatcher.utter_message(text=f"Top SKUs contributing to revenue: {top_skus}")
        return []


class ActionHighestROI(Action):
    def name(self) -> str:
        return "action_highest_roi"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        roi_data = get_roi_data_for_promotions()
        highest_roi = identify_highest_roi_promotion(roi_data)
        dispatcher.utter_message(text=f"Highest ROI promotion: {highest_roi}")
        return []
class ActionSimulatePriceReduction(Action):
    def name(self) -> str:
        return "action_simulate_price_reduction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        product = tracker.get_slot("product")
        reduction_percent = tracker.get_slot("reduction_percent")
        result = simulate_price_reduction(product, reduction_percent)
        dispatcher.utter_message(text=f"Simulated impact of {reduction_percent}% price reduction on {product}: {result}")
        return []


class ActionSimulateDigitalPromotionBudgetIncrease(Action):
    def name(self) -> str:
        return "action_simulate_digital_promotion_budget_increase"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        budget_increase = tracker.get_slot("budget_increase")
        result = simulate_digital_promotion_budget_increase(budget_increase)
        dispatcher.utter_message(text=f"Expected sales lift from {budget_increase}% budget increase: {result}")
        return []


class ActionSimulateABTestDiscountStrategies(Action):
    def name(self) -> str:
        return "action_simulate_ab_test_discount_strategies"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        strategy1 = tracker.get_slot("strategy1")
        strategy2 = tracker.get_slot("strategy2")
        result = simulate_ab_test_discount_strategies(strategy1, strategy2)
        dispatcher.utter_message(text=f"Projected sales impact: {result}")
        return []


class ActionPredictNextMonthSales(Action):
    def name(self) -> str:
        return "action_predict_next_month_sales"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        sku = tracker.get_slot("sku")
        result = predict_next_month_sales(sku)
        dispatcher.utter_message(text=f"Predicted sales for next month (SKU: {sku}): {result}")
        return []


class ActionSimulateRemovingLowPerformingSKU(Action):
    def name(self) -> str:
        return "action_simulate_removing_low_performing_sku"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        category = tracker.get_slot("category")
        result = simulate_removing_low_performing_sku(category)
        dispatcher.utter_message(text=f"Impact of removing low-performing SKU in {category}: {result}")
        return []


class ActionSimulateCompetitorLaunch(Action):
    def name(self) -> str:
        return "action_simulate_competitor_launch"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        competitor_price_difference = tracker.get_slot("competitor_price_difference")
        result = simulate_competitor_launch(competitor_price_difference)
        dispatcher.utter_message(text=f"Expected market impact due to competitor launch: {result}")
        return []


class ActionSimulateSupplyChainDisruption(Action):
    def name(self) -> str:
        return "action_simulate_supply_chain_disruption"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        days = tracker.get_slot("days")
        result = simulate_supply_chain_disruption(days)
        dispatcher.utter_message(text=f"Impact of {days}-day supply chain disruption: {result}")
        return []


class ActionSimulateOfflineToEcommerceShift(Action):
    def name(self) -> str:
        return "action_simulate_offline_to_ecommerce_shift"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        shift_percentage = tracker.get_slot("shift_percentage")
        result = simulate_offline_to_ecommerce_shift(shift_percentage)
        dispatcher.utter_message(text=f"Effect of shifting {shift_percentage}% offline sales to e-commerce: {result}")
        return []


class ActionSimulateIncreaseTradeMargins(Action):
    def name(self) -> str:
        return "action_simulate_increase_trade_margins"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        margin_increase = tracker.get_slot("margin_increase")
        result = simulate_increase_trade_margins(margin_increase)
        dispatcher.utter_message(text=f"Projected impact of {margin_increase}% increase in trade margins: {result}")
        return []


class ActionSimulateNewCompetitorImpact(Action):
    def name(self) -> str:
        return "action_simulate_new_competitor"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[str, Any]) -> List[Dict[str, Any]]:
        duration_months = tracker.get_slot("duration_months") or 6
        result = simulate_new_competitor_impact(duration_months)
        dispatcher.utter_message(text=f"Expected sales impact of new competitor over {duration_months} months: {result}")
        return []
