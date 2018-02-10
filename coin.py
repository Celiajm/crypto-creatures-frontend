#196, 245, 191, 207, 137, 252, 152, 239, 170, 45, 1, 36, 48, 139, 97, 164, 229,
#89, 89, 50, 152, 143, 149, 164, 155, 136, 12, 72, 197, 26, 55, 242
#200-256 animal, 22 numbers
#
import random

class CoinGen:

 	def __init__(self, hashfn):

	 	def which_item(n, hashfn):

	 		# 101-220 animal
		 	# 1-100 coin
		 	#221-256 item

	 		if (n <= 100):
	 			print "I'm a Coin."
	 			return (0, Coin())
	 		elif (n <= 220):
	 			print "I'm a Creature."
	 			return (1, CoinCreature(hashfn))
	 		else:
	 			print "I'm an Item."
	 			return (2, CoinItem(hashfn))

	 	self.item = which_item(hashfn[10], hashfn)

class CoinCreature:

	def __init__(self, hashfn):

	 	self.animal_type =  self.animal_type(hashfn[11])
	 	self.eye = self.eye_type(hashfn[12])
	 	self.color_1 = self.color_picker(hashfn[13])
	 	self.color_2 = self.color_picker(hashfn[14])
	 	self.color_3 = self.color_picker(hashfn[15])

	def animal_type(self, n):

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

	def eye_type(self, n):

		if (n <= 100):
			return "basic"
		elif(n <= 200):
			return "cute"
		elif(n <= 255):
			return "crazy"
		else:
			return "angry"

	def color_picker(self, n):

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
		self.item_type = self.type_picker(hashfn[20])
		self.item_name = 0

	def type_picker(self, n):
		return "food"

	def name_picker(self, n, item_type):

		if(item_type == "food"):
			if(n <= 100):
				return "ice_cream"
			elif(n <= 200):
				return "cake"
			else:
				return "drumstick"

def test(hashfn):

	init_coin = CoinGen(hashfn)

	item = init_coin.item

	if item[0] == 1:
		animal = item[1]
		animal_string = "I'm a "
		animal_string += str(animal.animal_type)
		animal_string += " with "
		animal_string += str(animal.eye)
		animal_string += " eyes and "
		animal_string += str(animal.color_1)
		animal_string += " fur."
		print animal_string

	return 

def gen_list():

	rand_list = []

	for i in range(32):
		rand_list.append(random.randint(1,256))

	return rand_list

test(gen_list())

