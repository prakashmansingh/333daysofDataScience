#scale analysis for the small business products
import numpy as np 

#here we take 5 product sample 
sales_data = np.array([
    [5 ,8 ,6 ,7 ,9 ,5, 4 ],
    [2 ,3 ,4 ,2 ,1 ,3 ,5],
    [10 ,12 ,10 ,11 ,9 ,12 ,13],
    [1, 2, 1, 2, 3, 2, 1],
    [7, 6, 8, 9, 10, 7, 6]
])

#total sales of each product
total_sales_per_product = np.sum(sales_data , axis=1)

#weakly sales of product
total_weekly_sales = np.sum(sales_data)

 #best and worst sell in a weeek
best_selling_product = np.argmax(total_sales_per_product) + 1
worst_selling_product = np.argmin(total_sales_per_product) +1

print("total sales per product : ",total_sales_per_product)
print("total weekly sales per product :" , total_weekly_sales)
print(f"best selling product : product {best_selling_product}")
print(f"worst selling product : product{worst_selling_product}")
