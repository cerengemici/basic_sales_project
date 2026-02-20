quantities = [2, 1, 3, 1, 2]
prices = [10,20,10,15,20]
total_revenue=0
for q, p in zip(quantities, prices):total_revenue +=q*p
print("toplam revenue:", total_revenue)