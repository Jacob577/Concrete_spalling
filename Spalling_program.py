import pickle
from os import system, name 
from plot_area import PlotSpalling
running = True

def import_models():
	with open('classification_model.pickle', "rb") as file:
		classification_model = pickle.load(file)

	with open('regression_model.pickle', "rb") as file:
		upper_model = pickle.load(file)
	return classification_model, upper_model

def makePrediction(parameters,length):
	will_spall = 0
	classification_model, regression_model = import_models()
	probability_spall = classification_model.predict_proba([parameters])[0][1]

	if float(probability_spall) > 0.1:
		will_spall = 1

	print('The probability of spalling is {}'.format(str(probability_spall*100)[0:4] + '%'))
	
	if will_spall == 0:
		print('Very low probability of spalling')
		print('The amount of spalling will with 90' + '%' + ' certainty not surpass {} mm.'.format(str(float(regression_model.predict([parameters]))*length)[0:4]))

	if will_spall:
		print('The amount of spalling will with 80' + '%' + ' certainty not surpass {} mm.'.format(str(float(regression_model.predict([parameters]))*length)[0:4]))


while running:
	_ = system('cls')
	print('!!WARNING!!')
	print('This application is not validated and should be used with causion.')
	print('\n')
	print('To get an estimation if and how much the concrete in question will spall:\nEnter requestet parameters when asked and press enter.')
	print('Do not include units.')
	print('Please enter the lengeth of one of the sides on the quadratic examined slab [m]')
	length = float(input('Length: '))
	print('Please enter applied Load [kN]\n')
	load = input('Load: ')
	print('Enter moisture content in mass percentage [%]\n')
	moisture = input('Moisture content: ')
	print('Enter compressive strenth [MPa]\n')
	compressive_strenth = input('Compressive strenth: ')

	try:
		parameters = [load, moisture, compressive_strenth]
		makePrediction(parameters,length)
		with open('classification_model.pickle', "rb") as file:
			classification_model = pickle.load(file)
		PlotSpalling(length,float(classification_model.predict([parameters])))


	except:
		print('Oops!! Something went wrong, are you sure you only entered numbers and not any ","?')

	
	print('\n')
	print('Would you like to make another prediction?')
	print('Press y for another prediction.')

	another = str(input())

	if another == 'y':
		running = True
	else:
		running = False

