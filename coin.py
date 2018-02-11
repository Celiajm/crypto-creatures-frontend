#196, 245, 191, 207, 137, 252, 152, 239, 170, 45, 1, 36, 48, 139, 97, 164, 229,
#89, 89, 50, 152, 143, 149, 164, 155, 136, 12, 72, 197, 26, 55, 242
#200-256 animal, 22 numbers
#
import random
import flask

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
                self.image = "generated/" + self.animal_type + str(sha) + ".svg"
                self.sha = sha

	def animal_type(self, n):

		if(n <= 75):
			return "bear"
		elif(n <= 110):
			return "bunny"
		# elif(n <= 140):
		# 	return "squirrel"
		elif(n <= 160):
			return "fox"
		elif(n <= 180):
			return "panda"
		elif(n <= 200):
			return "deer"
		elif(n <= 220):
			return "dalmatian"
		# elif(n <= 253):
		# 	return "octopus"
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

def rgb_to_color(color):

    r = color[0]
    g = color[1]
    b = color[2]
    rgb = (r<<16) + (g<<8) + b
    return rgb

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