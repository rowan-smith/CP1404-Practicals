TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator 2.0\n")

tariff_choice = int(input("Which tarrif? 11 or 31: "))
daily_kwh_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

if tariff_choice == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31

kwh_cost_per_day = tariff * daily_kwh_use
estimated_bill = kwh_cost_per_day * billing_days

print("\nEstimiated bill: ${:.2f}".format(estimated_bill))
