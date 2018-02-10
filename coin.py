#196, 245, 191, 207, 137, 252, 152, 239, 170, 45, 1, 36, 48, 139, 97, 164, 229,
 #89, 89, 50, 152, 143, 149, 164, 155, 136, 12, 72, 197, 26, 55, 242

 #200-256 animal, 22 numbers
 #

 class CoinGen:

 	def __init__(self, hashfn):

 		self.item = which_item(hashfin[10])

 	def which_item(n):

 		# 101-220 animal
	 	# 1-100 coin
	 	#221-256 item

 		if (n <= 100):
 			return Coin()
 		elif (n <= 220):
 			return CoinCreature()
 		else:
 			return CoinItem()


class CoinCreature:

	def __init__(self, hashfn):

	 	self.animal_type =  animal_type(hashfn[11])
	 	self.eye = eye_type(hashfn[12])
	 	self.color_1 = color_picker(hashfn[13])
	 	self.color_2 = color_picker(hashfn[14])
	 	self.color_3 = color_picker(hashfn[15])

	def animal_type(n):

		if(n <= 75):
			return "bear"
		elif(n <= 110):
			return "bunny"
		elif(n <= 140):
			return "squirrel"
		elif(n <= 160):
			return "fox"
		elif(n <= 180):
			return "panda"
		elif(n <= 200):
			return "octopus"
		elif(n <= 220):
			return "dalmation"
		elif(n <= 250):
			return "deer"
		else:
			return "hedgehog"

	def eye_type(n):

		if (n <= 100):
			return "basic"
		elif(n <= 200):
			return "cute"
		elif(n <= 255):
			return "crazy"
		else:
			return "angry"

	def color_picker(n):

		if (n <= 32):
			return "purple"
		elif (n <= 65):
			return "blue"
		elif (n <= 99):
			return "green"
		elif (n <= 149):
			return "yellow"
		elif (n <= 199):
			return "orange"
		elif (n <= 224):
			return "red"
		elif (n <= 240):
			return "bronze"
		elif (n <= 249):
			return "silver"
		else:
			return "gold"


class Coin:

	def __init__(self):
		self.coin = 1

class CoinItem:

	def __init__(self, hashfn):
		self.item_type = type_picker(hashfn[20])
		self.item_name = 

	def type_picker(n):
		return "food"

	def name_picker(n, item_type):

		if(item_type == "food"):
			if(n <= 100):
				return "ice_cream"
			elif(n <= 200):
				return "cake"
			else:
				return "drumstick"