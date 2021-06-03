#Percent Multiplier
print('Welcome to the % Checker!')

startingValue = float(input('Enter A Starting Number: '))

percent = float(input('Enter a percent: % '))

incOrDec = str(input('Do you want to increase or decrease by that percent?\nPlease type increase or decrease:').lower())

#----------#

def percentInc(startingValue, percent):
	result = startingValue*(percent/100 + 1)
	print(result)
	
def percentDec(startingValue,percent):
	result = startingValue*(100-percent/100)
	print(result)

#----------#	

if incOrDec == 'increase':
	print('A percent increase of:')
	percentInc(startingValue,percent)
elif incOrDec == 'decrease':	
	print('A percent increase of:')
	percentDec(startingValue,percent)
else:
	print('Error')