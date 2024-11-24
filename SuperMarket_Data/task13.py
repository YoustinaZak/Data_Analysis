import pandas as pd
import numpy as np
#1
df = pd.read_csv("supermarket_Sales.csv")
Branches_Sum = df.groupby("Branch")["Gross income"].sum()
filt = Branches_Sum == Branches_Sum.max()
print("Branch achieves with highest income")
print(Branches_Sum[filt])
#2
Product = df.groupby(["Product line", "Gender"])["Gross income"].sum()
#filt2 = Product["Gender"] == "Female" u can't do this to a series
filt2 = Product.index.get_level_values("Gender")== "Male"
print("Product Line achieves the highest income for Males")
print(Product[filt2].idxmax())
#3
Sold_City = df.groupby("City")["Cost of goods sold"].sum()
print(Sold_City)
print("Sales done in each city")
#4
Payment_Sum = df.groupby("Payment")["Gross income"].sum()
filt4 = Payment_Sum == Payment_Sum.max()
print("Payment achieves with highest income")
print(Payment_Sum[filt4])
#5
Branch = df.groupby("Branch")["Customer stratification rating"].mean()
print("average Customer satisfaction rating per branch")
print(Branch)
#6
df["new_date"]=pd.to_datetime(df["Date"])
Month_City = df.groupby(df["new_date"].dt.month)["Cost of goods sold"].sum()
print(Month_City)
print("sales done in each month")
#7
filt = (df["new_date"].dt.day_name() == "Saturday" )|( df["new_date"].dt.day_name() == "Sunday")
weekends= df[filt]
total = df["Gross income"].sum()
print("percentage of income made in weekends")
print(weekends["Gross income"].sum()/total *100)
#8
df["new_time"]= pd.to_datetime(df["Time"])
hour =df.groupby(df["new_time"].dt.hour)["Cost of goods sold"].sum()
filt= hour== hour.max()
print("hour of the day with the highest number of sales")
print(hour[filt])
#9
Pay =df.groupby("Payment")["Customer stratification rating"].sum()
filt = Pay== Pay.max()
print("Payment method with the most customer satisfaction")
print(Pay[filt])