import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data
data = pd.read_csv("company_sales_data.csv")

months = data["month_number"]

# Exercise 1:
# Line plot of Total Profit
plt.figure()
plt.plot(months, data["total_profit"], marker="o")

plt.title("Total Profit Over Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)

plt.show()

# Exercise 2:
# Subplot for Bathing Soap & Facewash
plt.figure()

# Subplot 1: Bathing Soap
plt.subplot(2, 1, 1)
plt.plot(months, data["bathingsoap"], marker="o")
plt.title("Bathing Soap Sales")
plt.ylabel("Units Sold")
plt.grid(True)

# Subplot 2: Facewash
plt.subplot(2, 1, 2)
plt.plot(months, data["facewash"], marker="o")
plt.title("Facewash Sales")
plt.xlabel("Month Number")
plt.ylabel("Units Sold")
plt.grid(True)

plt.tight_layout()
plt.show()
