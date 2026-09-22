import pandas as pd
import matplotlib.pyplot as plt

# Load data - Legal Subscription Saver by Sakshi Pradhan
df = pd.read_csv('subscription_data.csv')

# Remove Total row for chart
df_chart = df[df['App'] != 'Total']

# Calculate savings
total_paid = df_chart['Paid_Cost_INR'].sum()
total_saving = df_chart['Saving'].sum()
yearly_saving = total_saving * 12

print(f"=== Sakshi Pradhan - Legal Free Tools Hub ===")
print(f"Total Paid Cost: ₹{total_paid} per month")
print(f"Total After Free Legal Tools: ₹0")
print(f"You Save: ₹{total_saving} per month")
print(f"Yearly Saving: ₹{yearly_saving} per year!")

# RED-GREEN Chart - Sakshi's signature logic
plt.figure(figsize=(12,6))
colors = ['#D32F2F' if cost > 500 else '#FF9800' if cost > 200 else '#388E3C' for cost in df_chart['Paid_Cost_INR']]
bars = plt.bar(df_chart['App'], df_chart['Paid_Cost_INR'], color=colors, edgecolor='black')

plt.title('Project 3: Subscription Cost Analysis - RED=Expensive Paid, GREEN=Free Legal (Sakshi Pradhan)', fontsize=12, fontweight='bold')
plt.ylabel('Cost INR per Month', fontsize=11)
plt.xlabel('Apps', fontsize=11)
plt.xticks(rotation=20, ha='right')
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 20,
             f'₹{int(height)}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('cost_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('cost_comparison_tableau.png', dpi=300, bbox_inches='tight')
print("
Charts saved: cost_comparison.png")
plt.show()

# Show Free Alternatives
print("
--- LEGAL FREE ALTERNATIVES HUB ---")
print(df_chart[['App','Free_Legal_Alternative','Saving']].to_string(index=False))

# Category wise
print("
--- Category Wise Spend ---")
category = df_chart.groupby('Category')[['Paid_Cost_INR','Saving']].sum()
print(category)
