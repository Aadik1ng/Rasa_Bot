# analytics_functions.py

import pandas as pd
import datetime

class Analytics:
    def __init__(self):
        """
        Constructor: Load the CSV file and perform any necessary preprocessing.
        This constructor is executed every time an Analytics object is created.
        """
        DATA_FILE = r"data\NRM_DataSet_Training.xlsx - All_Data.csv"  # Ensure the file path is correct.
        self.df = pd.read_csv(DATA_FILE)  # Using default comma separator.
        # Convert the 'Last_Purchase_Date' column to datetime objects.
        self.df['Last_Purchase_Date'] = pd.to_datetime(self.df['Last_Purchase_Date'], format='%m/%d/%Y')

    #############################################
    # Method 1: get_sales_data_for_quarter
    #############################################
    def get_sales_data_for_quarter(self, quarter):
        """
        Calculate total sales revenue for a given quarter (assumes year 2024).
        Returns a numeric value.
        """
        if quarter == "Q1":
            start = datetime.datetime(2024, 1, 1)
            end = datetime.datetime(2024, 3, 31)
        elif quarter == "Q2":
            start = datetime.datetime(2024, 4, 1)
            end = datetime.datetime(2024, 6, 30)
        elif quarter == "Q3":
            start = datetime.datetime(2024, 7, 1)
            end = datetime.datetime(2024, 9, 30)
        elif quarter == "Q4":
            start = datetime.datetime(2024, 10, 1)
            end = datetime.datetime(2024, 12, 31)
        else:
            return 0

        quarter_df = self.df[(self.df['Last_Purchase_Date'] >= start) & (self.df['Last_Purchase_Date'] <= end)]
        total_sales = quarter_df['Sales_Revenue'].sum()
        return total_sales

    #############################################
    # Method 2: compare_sales
    #############################################
    def compare_sales(self, base_sales, compared_sales):
        """
        Compare two sales figures and return the percentage change.
        Returns a float value representing the percentage change.
        If base_sales is 0, returns None.
        """
        if base_sales == 0:
            return None
        percentage_change = ((compared_sales - base_sales) / base_sales) * 100
        return percentage_change

    #############################################
    # Method 3: get_yoy_sales_growth
    #############################################
    def get_yoy_sales_growth(self):
        """
        Simulate YoY (Year-over-Year) growth by assuming last year's sales were 10% lower.
        Returns a dictionary.
        """
        current_year_sales = self.df['Sales_Revenue'].sum()
        previous_year_sales = current_year_sales * 0.9  # Assume previous year was 10% lower.
        yoy_growth = ((current_year_sales - previous_year_sales) / previous_year_sales) * 100
        return {"Total_YoY_Growth": yoy_growth}

    #############################################
    # Method 4: get_highest_growth_categories
    #############################################
    def get_highest_growth_categories(self, yoy_growth):
        """
        Identify categories with the highest YoY growth.
        Groups data by Region and returns the region with the maximum percentage change.
        Returns a dictionary with region and its growth percentage.
        """
        region_sales = self.df.groupby("Region")["Sales_Revenue"].sum().sort_values()
        region_growth = region_sales.pct_change().dropna() * 100
        if not region_growth.empty:
            highest_region = region_growth.idxmax()
            highest_growth = region_growth.max()
            return {"Region": highest_region, "Growth": highest_growth}
        else:
            return {}

    #############################################
    # Method 5: get_top_skus_by_revenue
    #############################################
    def get_top_skus_by_revenue(self):
        """
        Identify the top SKUs that cumulatively contribute to 80% of total revenue.
        Returns a list of SKU identifiers.
        """
        sku_revenue = self.df.groupby("Product_ID")["Sales_Revenue"].sum().sort_values(ascending=False)
        total_revenue = sku_revenue.sum()
        cumulative = 0
        top_skus = []
        for sku, revenue in sku_revenue.items():
            cumulative += revenue
            top_skus.append(sku)
            if cumulative / total_revenue >= 0.8:
                break
        return top_skus

    #############################################
    # Method 6: get_average_sales_per_store
    #############################################
    def get_average_sales_per_store(self):
        """
        Calculate average sales per store.
        Here, each unique value in the 'Channel' column is treated as a store.
        Returns a numeric value.
        """
        channel_sales = self.df.groupby("Channel")["Sales_Revenue"].sum()
        avg_sales = channel_sales.mean()
        return avg_sales

    #############################################
    # Method 7: compare_brands_in_region
    #############################################
    def compare_brands_in_region(self, region):
        """
        Compare sales performance between two simulated brands in the specified region.
        Simulates brand assignment based on the numeric part of Product_ID.
        Returns a dictionary mapping each brand to its total Sales_Revenue.
        """
        def assign_brand(product_id):
            num = int(product_id[1:])  # Remove the leading "P" and convert to int.
            return "Brand A" if num % 2 == 0 else "Brand B"

        self.df['Brand'] = self.df['Product_ID'].apply(assign_brand)
        region_df = self.df[self.df['Region'] == region]
        brand_sales = region_df.groupby("Brand")["Sales_Revenue"].sum()
        return brand_sales.to_dict()

    #############################################
    # Method 8: get_roi_data_for_promotions
    #############################################
    def get_roi_data_for_promotions(self):
        """
        Simulate ROI calculation for promotions.
        ROI is calculated as: Gross_Profit / (Discount (%) * Sales_Units) if Discount exists, else 0.
        Returns a dictionary mapping Product_ID to its ROI.
        """
        self.df['ROI'] = self.df.apply(
            lambda row: (row['Gross_Profit'] / (row['Discount (%)'] * row['Sales_Units']))
            if row['Discount (%)'] > 0 and row['Sales_Units'] > 0 else 0,
            axis=1
        )
        roi_data = self.df[['Product_ID', 'ROI']]
        return roi_data.set_index('Product_ID')['ROI'].to_dict()

    #############################################
    # Method 9: identify_highest_roi_promotion
    #############################################
    def identify_highest_roi_promotion(self, roi_data):
        """
        Identify the promotion (by Product_ID) with the highest ROI.
        Returns a tuple: (Product_ID, ROI) or None if no data is available.
        """
        if not roi_data:
            return None
        highest = max(roi_data, key=roi_data.get)
        return (highest, roi_data[highest])

    #############################################
    # Method 10: get_incremental_sales_by_promotion
    #############################################
    def get_incremental_sales_by_promotion(self):
        """
        Simulate a breakdown of incremental sales driven by promotions.
        - Discount-driven incremental sales = Sales_Units * (Discount (%) / 100)
        - Bundling-driven incremental sales = Sales_Units - (Sales_Units * (Discount (%) / 100))
        Returns a dictionary with keys 'Discount' and 'Bundling'.
        """
        self.df['Discount_Increment'] = self.df['Sales_Units'] * (self.df['Discount (%)'] / 100)
        self.df['Bundling_Increment'] = self.df['Sales_Units'] - self.df['Discount_Increment']
        total_discount = self.df['Discount_Increment'].sum()
        total_bundling = self.df['Bundling_Increment'].sum()
        return {"Discount": total_discount, "Bundling": total_bundling}

    #############################################
    # Method 11: get_retention_data_for_promotions
    #############################################
    def get_retention_data_for_promotions(self):
        """
        Simulate retention data based on Purchase_Frequency.
        Mapping:
          - "Weekly" → 4
          - "Bi-weekly" → 2
          - "Monthly" → 1
        Returns a dictionary mapping Product_ID to its retention score.
        """
        frequency_map = {"Weekly": 4, "Bi-weekly": 2, "Monthly": 1}
        self.df['Retention_Score'] = self.df['Purchase_Frequency'].map(frequency_map)
        retention = self.df.groupby("Product_ID")['Retention_Score'].mean().to_dict()
        return retention

    #############################################
    # Method 12: identify_highest_retention_promotion
    #############################################
    def identify_highest_retention_promotion(self, retention_data):
        """
        Identify the promotion (by Product_ID) that led to the highest customer retention.
        Returns a tuple: (Product_ID, retention score) or None if no data is available.
        """
        if not retention_data:
            return None
        highest = max(retention_data, key=retention_data.get)
        return (highest, retention_data[highest])

    #############################################
    # Method 13: calculate_promotion_cannibalization
    #############################################
    def calculate_promotion_cannibalization(self):
        """
        Calculate the percentage of promotions leading to cannibalization.
        Defined as: (Total Returns_Units for promotional products / Total Sales_Units for promotional products) * 100,
        where a product is promotional if Discount (%) > 0.
        Returns a float value representing the percentage.
        """
        promo_df = self.df[self.df['Discount (%)'] > 0]
        total_sales_units = promo_df['Sales_Units'].sum()
        if total_sales_units == 0:
            return 0
        cannibalization = (promo_df['Returns_Units'].sum() / total_sales_units) * 100
        return cannibalization

    #############################################
    # Method 14: get_sales_data_for_campaign
    #############################################
    def get_sales_data_for_campaign(self, campaign_name):
        """
        Simulate the sales performance before, during, and after a campaign.
        For example, for the Diwali campaign assume the campaign date is January 3, 2024.
        Returns a dictionary with keys 'Before', 'During', and 'After'.
        """
        if campaign_name.lower() == "diwali":
            campaign_date = datetime.datetime(2024, 1, 3)
        else:
            return {}
        
        before = self.df[self.df['Last_Purchase_Date'] < campaign_date]['Sales_Revenue'].sum()
        during = self.df[self.df['Last_Purchase_Date'] == campaign_date]['Sales_Revenue'].sum()
        after = self.df[self.df['Last_Purchase_Date'] > campaign_date]['Sales_Revenue'].sum()
        return {"Before": before, "During": during, "After": after}


# ------------------------------------------------------------------------------
# Global functions that instantiate the Analytics class so that each call
# executes the constructor (i.e. reloads the CSV data).
# ------------------------------------------------------------------------------

def get_sales_data_for_quarter(quarter):
    return Analytics().get_sales_data_for_quarter(quarter)
     

def compare_sales(sales_q1, sales_q2):
    return Analytics().compare_sales(sales_q1, sales_q2)

def get_yoy_sales_growth():
    return Analytics().get_yoy_sales_growth()

def get_highest_growth_categories(yoy_growth):
    return Analytics().get_highest_growth_categories(yoy_growth)

def get_top_skus_by_revenue():
    return Analytics().get_top_skus_by_revenue()

def get_average_sales_per_store():
    return Analytics().get_average_sales_per_store()

def compare_brands_in_region(region):
    return Analytics().compare_brands_in_region(region)

def get_roi_data_for_promotions():
    return Analytics().get_roi_data_for_promotions()

def identify_highest_roi_promotion(roi_data):
    return Analytics().identify_highest_roi_promotion(roi_data)

def get_incremental_sales_by_promotion():
    return Analytics().get_incremental_sales_by_promotion()

def get_retention_data_for_promotions():
    return Analytics().get_retention_data_for_promotions()

def identify_highest_retention_promotion(retention_data):
    return Analytics().identify_highest_retention_promotion(retention_data)

def calculate_promotion_cannibalization():
    return Analytics().calculate_promotion_cannibalization()

def get_sales_data_for_campaign(campaign_name):
    return Analytics().get_sales_data_for_campaign(campaign_name)


# ------------------------------------------------------------------------------
# Optional: Testing the module directly.
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    analytics = Analytics()  # Create an instance of Analytics

    # Example 1: Get sales data for a specific quarter
    sales_a = analytics.get_sales_data_for_quarter("Q3")
    sales_b = analytics.get_sales_data_for_quarter("Q1")
    print("Q3 Sales:", sales_a)
    print("Q1 Sales:", sales_b)

    # Example 2: Compare sales between two quarters
    comparison = analytics.compare_sales(sales_a, sales_b)
    print("Sales Comparison:", comparison)

    # Example 3: Get Year-over-Year (YoY) sales growth
    yoy_growth = analytics.get_yoy_sales_growth()
    print("YoY Growth:", yoy_growth)

    # Example 4: Get highest growth categories
    highest_growth_category = analytics.get_highest_growth_categories(yoy_growth)
    print("Highest Growth Category:", highest_growth_category)

    # Example 5: Get top SKUs contributing to 80% of revenue
    top_skus = analytics.get_top_skus_by_revenue()
    print("Top SKUs by Revenue:", top_skus)

    # Example 6: Get average sales per store
    avg_sales = analytics.get_average_sales_per_store()
    print("Average Sales per Store:", avg_sales)

    # Example 7: Compare sales between brands in a specific region
    brand_comparison = analytics.compare_brands_in_region("North")
    print("Brand Comparison in North Region:", brand_comparison)

    # Example 8: Get ROI data for promotions
    roi_data = analytics.get_roi_data_for_promotions()
    print("ROI Data for Promotions:", roi_data)

    # Example 9: Identify highest ROI promotion
    highest_roi = analytics.identify_highest_roi_promotion(roi_data)
    print("Highest ROI Promotion:", highest_roi)

    # Example 10: Get incremental sales from promotions
    incremental_sales = analytics.get_incremental_sales_by_promotion()
    print("Incremental Sales by Promotion:", incremental_sales)

    # Example 11: Get retention data for promotions
    retention_data = analytics.get_retention_data_for_promotions()
    print("Retention Data for Promotions:", retention_data)

    # Example 12: Identify highest retention promotion
    highest_retention = analytics.identify_highest_retention_promotion(retention_data)
    print("Highest Retention Promotion:", highest_retention)

    # Example 13: Calculate promotion cannibalization
    cannibalization = analytics.calculate_promotion_cannibalization()
    print("Promotion Cannibalization:", cannibalization)

    # Example 14: Get sales data for a specific campaign
    campaign_sales = analytics.get_sales_data_for_campaign("Diwali")
    print("Sales Data for Diwali Campaign:", campaign_sales)
