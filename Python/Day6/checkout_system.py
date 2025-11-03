from checkout_functions import *
print("WELCOME TO MAXL CHECKOUT SYSTEM")
product_name = "c"
sub_total = 0
invo = ""
while product_name != "DONE":
	product_name = input("Enter name of product or type 'DONE' to end: ").upper()
	if product_name == "DONE":
		continue
	product_price = int(input("Enter price of product: "))
	sub_total += product_price
	vat_amount = calculate_vat(sub_total)
	grand_total = add_vat_with_subtotal(sub_total,vat_amount)

	invoice = f"""
	{product_name} : 	N{product_price}
	"""
	invo += invoice
	vat_info = f"""
	VAT(7.5%)      : N{vat_amount}
	Total Amount   : N{grand_total}
	"""
print("\t","________INVOICE_________")
print(invo)
print(vat_info)

payment = int(input("Enter amount you want to pay: "))
balance = give_balance(payment,grand_total)

payment_receipt = f"""
___________PAYMENT RECEIPT_______
{invo}
Total Paid : N{payment}
Grand Total :N{grand_total}
Balance   :N{balance}



"""
print(payment_receipt)

	
	
