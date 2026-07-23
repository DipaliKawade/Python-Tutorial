print("----- Electricity Bill Calculation -----")

# Variables
units = 250
cost_per_unit = 8

# Calculate Bill
total_bill = units * cost_per_unit
gst = total_bill * 0.18
final_bill = total_bill + gst

print("Units Consumed =", units)
print("Cost per Unit =", cost_per_unit)
print("Total Bill =", total_bill)
print("GST (18%) =", gst)
print("Final Bill =", final_bill)