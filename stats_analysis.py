import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the bat dataset
bat_df = pd.read_csv("dataset1.csv")

# Confirm column names (already done previously)
print(bat_df.columns)

# Now plot hesitation time (avoidance/vigilance) by month
sns.boxplot(data=bat_df, x='month', y='bat_landing_to_food')
plt.title('Bat Hesitation Time by Month')
plt.xlabel('Month')
plt.ylabel('Seconds from Landing to Food')
plt.show()











