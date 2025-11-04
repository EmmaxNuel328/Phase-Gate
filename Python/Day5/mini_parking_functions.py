def is_empty():
	return 0


def is_occupied():
	return 1



def enter_parking_lot(car_name,parking_lot):
	if len(parking_lot) > 20:
		return "No space"
	parking_lot.insert(0,car_name)
	return "Parked successfully"
	


def leave_parking_lot(slot_number,parking_lot):
	if parking_lot == []:
		raise ValueError
	parking_lot.pop(slot_number)
	return "Removed successfully"

