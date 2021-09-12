#8-1
def display_message():
	print(f"we are learning python")

#8-2
def favorite_book(title):
	print(f"{title} is mike's favorite book")

#8-3
def make_shirt(size, text="I love python"):
	print(f"I would like an {size} tshirt with the word {text} on it")

#8-4
def describe_city(city="bublin", country="ireland"):
	print(f"{city} is in {country}")

#8-6
def city_country(city, country):
	capital = f"{city}, {country}"
	return capital.title()

citi = city_country('havana', 'cuba')


#8-9
def show_messages(messages):
	for message in messages:
		msg = f"here is a {message}"
		print(msg)


def send_messages(messages, sent_messages):
	while messages:
		sending = messages.pop()
		print(f"sending messages:{sending}")
		sent_messages.append(sending)

messages = ['asldfadsf', 'sadfasdfas', 'sdfsadfasdf']
sent_messages = []

#8-10
def sandwhich(*args):
	print(f"you want a sandwhich with the following:")
	for arg in args:
		print(f"-{arg}")



#8-13 
def profile(first_name, last_name, **kwargs):
	kwargs['first'] = first_name
	kwargs['last'] = last_name
	return kwargs

user_profile = profile('Josh', 'Mines', location='SLC', age='22')

#8-14
def car(make, model, **kwargs):
	kwargs['make'] = make
	kwargs['model'] = model
	return kwargs

car_profile =  car('subaru', 'zer', mileage='1111111', age='234343')



