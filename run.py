# This is the main file to run our programm

from Monitoring.Monitoring import Monitoring

try:
	with Monitoring() as bot:
    		bot.land_first_page()
    		bot.choose_qualification()
    		bot.scroll()
    		bot.push_the_button()
    		bot.results()

except Exception as e:
	if 'in PATH' in str(e):
		print('Seems we have a problem running with this programm to start from command line')
	else:
		raise
