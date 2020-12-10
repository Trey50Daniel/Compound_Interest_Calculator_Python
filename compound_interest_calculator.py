initial_investment = int(input("Initial Investment: "))
apy = float(input("APY: "))
time_of_investment = int(input("Time invested(in years): "))

years = 0
investment_total = initial_investment
while years < time_of_investment:
    investment_total = investment_total + (investment_total * (apy / 100))
    years += 1
print(round(investment_total, 2))
