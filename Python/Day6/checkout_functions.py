def calculate_vat(subtotal):
	vat = 0.075 * subtotal
	if subtotal < 0:
		raise ValueError 
	return vat

def add_vat_with_subtotal(subtotal,vat_amount):
	total_amount = subtotal + vat_amount
	if total_amount < 0:
		raise ValueError
	return total_amount


def give_balance(payment_amount,grand_total):
	balance = payment_amount - grand_total
	if payment_amount < grand_total:
		raise ValueError
	return balance
