#196, 245, 191, 207, 137, 252, 152, 239, 170, 45, 1, 36, 48, 139, 97, 164, 229,
#89, 89, 50, 152, 143, 149, 164, 155, 136, 12, 72, 197, 26, 55, 242
#200-256 animal, 22 numbers
#
import random
import flask

all_animals = [
    'Angry_bear',
    'Angry_bunny',
    'Angry_dalmation',
    'Angry_deer',
    'Angry_fox',
    'Angry_hedgehog',
    'Angry_octopus',
    'Angry_panda',
    'Angry_squirrel',
    'Basic_bear',
    'Basic_bunny',
    'Basic_dalmation',
    'Basic_deer',
    'Basic_fox',
    'Basic_hedgehog',
    'Basic_octopus',
    'Basic_panda',
    'Basic_Squirrel',
    'Crazy_bear',
    'Crazy_bunny',
    'Crazy_dalamtion',
    'Crazy_deer',
    'Crazy_fox',
    'Crazy_hedgehog',
    'Crazy_octopus',
    'Crazy_panda',
    'Crazy_squirrel',
    'Cute_bear',
    'Cute_bunny',
    'Cute_dalmation',
    'Cute_deer',
    'Cute_fox',
    'Cute_hedgehog',
    'Cute_octopus',
    'Cute_panda',
    'Cute_squirrel',
    ]

class CoinGen:

 	def __init__(self, hashfn, sha):

	 	def which_item(n, hashfn, sha):

	 		# 101-220 animal
		 	# 1-100 coin
		 	#221-256 item

	 		if (n <= 0):
	 			print("I'm a Coin.")
	 			return (0, Coin())
	 		elif (n <= 256):
	 			print("I'm a Creature.")
	 			return (1, CoinCreature(hashfn, sha))
	 		else:
	 			print("I'm an Item.")
	 			return (2, CoinItem(hashfn))

	 	self.item = which_item(hashfn[10], hashfn, sha)

# octopus is now the most rare
class CoinCreature:

	def __init__(self, hashfn, sha):

	 	self.animal_type =  self.animal_type(hashfn[11])
	 	self.eye = self.eye_type(hashfn[12])
	 	self.color_1 = (hashfn[13]/2+128,hashfn[14]/2+128,hashfn[15]/2+128)
	 	self.color_2 = (hashfn[16]/2+128,hashfn[17]/2+128,hashfn[18]/2+128)
	 	self.color_3 = (hashfn[19]/2+128,hashfn[20]/2+128,hashfn[21]/2+128)
	 	self.bg_color = (hashfn[10]/2+128,hashfn[9]/2+128,hashfn[8]/2+128)
                self.image = "generated/" + self.animal_type + str(sha) + ".svg"
                self.sha = sha
                

                if "bunny" in self.animal_type:
                    self.bio = """
                    Keep an eye on your files if you get the bunny . . . and your loved ones for that matter. The bunny is a cute addition to anyone's creature collection, but a bunny with angry eyes is clearly a serial killer?
                    """
                elif "octopus" in self.animal_type:
                    self.bio = """
                     This slimyboi will be the most rarest of all your CryptoCreatures for his artisanally hand-beaded suckers. With only a 0.019% chance of discovering him on any given block, you better hold onto him when you find him!
                    """
                elif "fox" in self.animal_type:
                    self.bio = """
                     Cunning and sly, he will fetch you a handsome price at market!
                    """
                elif "hedgehog" in self.animal_type:
                    self.bio = """
                    The hedgehog is also a sneakyboi, so you may have a hard time finding him too. However, he's also one of our cutest creatures!

                    """
                elif "panda" in self.animal_type:
                    self.bio = """
                    Even though he's almost extinct in real life, the panda is alive and well in the bamboo forests of you PC! Mine for him and hope you get the angry eyes--they're the cutest!
                    """
                elif "dalmatian" in self.animal_type:
                    self.bio = """
                    Arf Arf! Any resemblance to Cupcakke's "Doggystyle" is purely coincidental.
                    """
                elif "deer" in self.animal_type:
                    self.bio = """
                     Sensational! The deer is adorable!
                    """
                elif "squirrel" in self.animal_type:
                    self.bio = """
                    Chomp chomp! Better protect you nutz if you find this guy in your next block! He's not too rare, but the right item can make his worth a lot of CreatureCoins!
                    """
                elif "bear" in self.animal_type:
                    self.bio = """
                    This is not a gay person or that thing from the Revenant--so you should NOT be afraid to mine for this cute and cuddly animal.
                    """
                else:
                    self.bio = "This one is totally new!!!"

	def animal_type(self, n):
            return all_animals[n % len(all_animals)]
            # return 

		# if(n <= 75):
			# return "Bear"
		# elif(n <= 110):
			# return "Bunny"
		# # elif(n <= 140):
		# # 	return "Squirrel"
		# elif(n <= 160):
			# return "Fox"
		# elif(n <= 180):
			# return "Panda"
		# elif(n <= 200):
			# return "Deer"
		# elif(n <= 220):
			# return "Dalmatian"
		# # elif(n <= 253):
		# # 	return "Octopus"
		# else:
			# return "Hedgehog"

	def eye_type(self, n):

		if (n <= 100):
			return "Basic"
		elif(n <= 200):
			return "Cute"
		elif(n <= 255):
			return "Crazy"
		else:
			return "Angry"

class Coin:

	def __init__(self):
		self.coin = 1

class CoinItem:

	def __init__(self, hashfn):
		self.item_type = self.type_picker(hashfn[22])
		self.item_name = self.name_picker(hashfn[23], self.item_type)

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

def test(hashfn ,sha):

	init_coin = CoinGen(hashfn, sha)

	item = init_coin.item

	animal_string = ""

	if item[0] == 1:
		animal = item[1]
		animal_string = "I'm a "
		animal_string += str(animal.animal_type)
		animal_string += " with "
		animal_string += str(animal.eye)
		animal_string += " eyes and "
		animal_string += str(animal.color_1)
		animal_string += " fur."
		print(animal_string)

	if item[0] == 2:
		item = item[1]
        item_string = "I am a "
        item_string += str(item.item_type)
        item_string += ". I am a "
        item_string += str(item.item_name)
        item_string += "."
        print(item_string)

	return

def gen_list():

	rand_list = []

	for i in range(32):
		rand_list.append(random.randint(1,256))

	return rand_list

# test(gen_list())

def sha_to_list(sha):

	byte_list = []

	for i in range(32):
		byte_list.append(int("0x"+sha[:2],0))
		sha = sha[2:]

	return byte_list

app = flask.Flask(__name__)

@app.route('/token/<sha>')
def show_token(sha=None):
	byte_list = sha_to_list(sha)
	coin = CoinGen(byte_list, sha).item

	#List of colors
	color_list = ['#d3f6f0','#92e4d6','#5fd1be','#38bfa9','#12b499',
	'#fff2db','#ffdfa4','#ffce75','#ffc04b','#ffaf1a','#fedadd','#fda2a9',
	'#fg737d','#fb4a57','#fa192a']

	items = ["Cake.svg", "Drumstick.svg","Ice_cream.svg"]
	item_len = len(items)
	for i in range(0, item_len):
		items[i] = "/static/" + items[i]

	print(coin[0])
	if(coin[0] == 1):
		replace(coin[1].animal_type, coin[1], sha)
		print coin[1].image
	# file_name = 'static/' + coin[1].animal_type + str(sha) + ".svg"
	return flask.render_template("token.html", coin=coin)

@app.route("/")
def space_index():
    animals = []
    for sha in open("./ledger.txt").readlines():
        sha = sha[:-1]
        animal = CoinGen(sha_to_list(sha), sha).item
	if(animal[0] == 1):
            replace(animal[1].animal_type, animal[1], sha)
            print animal[1].image
            animals.append(animal[1])
    return flask.render_template("index.html", animals=animals)

@app.route('/static/<path:path>')
def serve_static_files(path):
    return send_from_directory('static', path)

@app.route("/templates/about-us.html")
def about_us_page():
    return flask.render_template("about-us.html", coin=None)

def replace(fname, creature, hash_number):

    f = open('static/' + fname + ".svg", 'r')
    content = f.read()

    color1 = creature.color_1
    hc1 = 'rgb(' + str(color1[0]) + ',' +  str(color1[1]) + ',' + str(color1[2]) + ')'
    color2 = creature.color_2
    hc2 = 'rgb(' + str(color2[0]) + ',' +  str(color2[1]) + ',' + str(color2[2]) + ')'
    color3 = creature.color_3
    hc3 = 'rgb(' + str(color3[0]) + ',' +  str(color3[1]) + ',' + str(color3[2]) + ')'

    content = content.replace('#bebebe', hc1)
    content = content.replace('#725af7', hc2)
    content = content.replace('#6edaf4', hc3)
    f.close()

    new_f = open('static/generated/'+fname+str(hash_number)+".svg", 'w')

    new_f.write(content)
    new_f.close()
