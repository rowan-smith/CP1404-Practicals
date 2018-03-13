print("Electricity Bill Estimator\n")
cents_per_kwh = int(input("Enter cents per kWh: "))
daily_kwh_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

cents_per_kwh = cents_per_kwh / 100
kwh_cost_per_day = cents_per_kwh * daily_kwh_use
estimated_bill = kwh_cost_per_day * billing_days

print("\nEstimiated bill: ${:.2f}".format(estimated_bill))
