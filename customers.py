# Author: Samhita Savaram
# Module 11 Lab (Unit 3): Customer Dictionary and Lookup

# Reflection Questions:
# 1. In Exercise 3 you saw the difference between .get() and bracket notation. 
# When in real work would you use each one, and what's your rule of thumb for choosing?
# In real work I would use .get when avoiding KeyErrors, and that would be my rule of thumb
# Whereas I would use bracket notation when the key exists.


# 2. Exercise 8 asked you to build a summary dictionary with a loop. 
# What does this pattern remind you of from Excel, and why might the Python version be more useful for large datasets?
# This pattern reminds me of tables in Excel. Python is better for dealing with larger sets of data than excel.
# Excel can handle a lot less than Python can.

print("Exercise 1: One Customer") #!!!

customer = {
    "name": "Samhita",
    "email": "ssavaram@usf.edu",
    "tier": "gold",
    "ytd_spend": 14000
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("Exercise 2: Update and Add") #!!!

customer["phone"] = "813-555-0142"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

print(customer.get("email", "email not found"))

print("Exercise 3: Safe Lookup") #!!!

#NEW VERSION
print(customer.get("email", "no email on file"))

# try:
#    print(customer["email"])
# except KeyError as error:
#    print(f"KeyError Caught: {error}")

print("Exercise 4: Iterate") #!!!

for key, value in customer.items():
    print(f"{key} : {value}")

for item in customer:
    print(item)

print("Exercise 5: Lookup Table") #!!!

tier_discount = {"bronze" : 0,
                 "silver" : 0.05,
                 "gold" : 0.10,
                 "platinum" : 0.15}
purchase = 200
discount_rate = tier_discount.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"tier: {customer["tier"]}") # platinum 
print(f"discount rate: {discount_rate * 100:.0f}%") # 15%
print(f"final price: {final_price:.2f}") # $170.00

print("Exercise 6: List of Dicts") #!!!

customers = [
    {"name": "Bobby", "tier": "silver", "ytd_spend": 3200},
    {"name": "Coraline", "tier": "gold", "ytd_spend": 8750},
    {"name": "Derulo", "tier": "platinum", "ytd_spend": 450},
]

for record in customers:
    rate = tier_discount.get(record["tier"], 0)
    discount = 300 * rate
    print(f"{record['name']} {record['tier']} ${discount:.2f} discount on $300 purchases")

print("Exercise 7: Nested Catalog") #!!!

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in catalog.items():
    if details["stock"] > 20:
        print(f"LOW STOCK!!!: {product} - only {details['stock']} left in stock")

print("Exercise 8: Sales by Region") #!!!

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    sales_by_region[region] = sales_by_region.get(region, 0) + sale["amount"]
print(sales_by_region) 

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]}")