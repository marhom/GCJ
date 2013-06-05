def decToA(language, phrase):
	output = []
	if len(language) < 2:
		output = [language[0] for i in phrase]
	else:
		temp = phrase
		while(temp >= 1):
			s = temp % len(language)
			#print s
			#print language[s]
			output.append(language[temp % len(language)])
			temp = temp / len(language)
		output.reverse()
		print output
		output = ''.join(output)
	return output
def AtoDec(language, phrase):
	decOut = 0
	print phrase
	phrase = str(phrase)
	print phrase
	count = len(phrase)-1
	for c in phrase:
		print language.find(c)
		
		print len(language)**count
		decOut = decOut + language.find(c) * len(language)**count
		print decOut
		count = count-1
	return decOut
	
def alienTranslate(phrase, inL, outL):
	decimal = AtoDec(inL, phrase)
	alien = decToA(outL, decimal)
	print decimal
	print alien

# def runTranslate(filename):
	# fd = open(filename,'rU')
