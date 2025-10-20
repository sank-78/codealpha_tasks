 #TASK 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 320
}

print("Available Stocks and Prices:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")


portfolio = {}

n = int(input("\nEnter the number of different stocks you own: "))

for i in range(n):
    stock_name = input(f"\nEnter stock {i+1} name: ").upper()
    if stock_name not in stock_prices:
        print("❌ Stock not found in the price list! Skipping...")
        continue
    quantity = int(input(f"Enter quantity of {stock_name}: "))
    portfolio[stock_name] = quantity

total_investment = 0
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
    total_investment += value

print(f"\n Total Investment Value: ${total_investment}")

save_choice = input("\nDo you want to save your portfolio summary to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("=========================\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("✅ Portfolio summary saved to 'portfolio_summary.txt'")
else:
    print(" File not saved. Program ended.")
