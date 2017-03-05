import random

def taunts(health):
	if health == 100:
		return('Successfully integrated over the path to the candy')
	else:
		taunt_list = ['Math is cool.', 'Electromagnetism is my friend', 'I have a first AND second kind', 'herp', 'derp', 'Plenty of applications to classical mechanics!', 'Integrate THIS, gurl.', 'Beyonce has nothing on my integrals']
		rand = random.randrange(0,len(taunt_list))
		return(taunt_list[rand])