from mini_parking_functions import *

mini_parking_dashboard = """
1. Park car
2. Remove car
3. Display slots
"""
parking_lot = []
print(len(parking_lot))
prompt = 1
index = 0
count = 0
while prompt != 0:
	print(mini_parking_dashboard)
	prompt = input("Enter your choice: ")
	match prompt:
		case "1":
			car_name = input("Enter name of your car: ")
			parked_car =  enter_parking_lot(car_name,parking_lot)
			print(car_name,parked_car)
			print(parking_lot)
		case "2":
			car_name = input("Enter name of your car: ")
			slot_number = int(input("Enter slot number: "))
			removed_car = leave_parking_lot(slot_number - 1,parking_lot)
			print(car_name,removed_car)
			print(parking_lot)
		case "3":
			print(parking_lot)
		case _:
			print("Invalid input")
	index += 1
	

	#print(parking_lot)
	


