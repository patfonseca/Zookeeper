deposit = int(input())
interest_rate = 0.071
years = 0
while deposit < 700000:
    deposit = deposit * (1 + interest_rate)
    years += 1
print(years)