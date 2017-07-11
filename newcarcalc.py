
def newcar():
	input("How much is a new car going to cost you per month? Please hit enter to start")
	p = int(input("Please enter total cost of car: "))
	r = float(input("Please enter interest rate as a whole number(example: 15.6% = 15.6): National average is around 4.5%):  "))
	t = int(input("These payments would last for how many months?: "))
	dp = int(input("Please enter the downpayment percentage as a whole number: example: 20% = 20: "))
	afterdp = p - (p * dp/100)
	downpay = p - afterdp
	downpay = round(downpay, 2)
	interest = afterdp * (r/100) * (t/12)
	interest = round(interest, 2) 
	monthly_payment_bt = (afterdp + interest)/t
	monthly_payment_bt = round(monthly_payment_bt, 2)
	monthly_payment = (monthly_payment_bt * .07) + monthly_payment_bt
	monthly_payment = round(monthly_payment, 2)
	t = round(t/12, 2)
	return("Your monthly payment would be $" + str(monthly_payment)  +  " for " + str(t) + " years, and a downpayment of $" +  str(downpay))



print(newcar())















# Car payment should not exceed 10% of your total gross income per month. 
# Try not to finance a car longer than 60 months



