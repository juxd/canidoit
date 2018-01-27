
def error(text):
	text = text.replace(" ","");
	letters = 0
	leftBracket = 0
	rightBracket = 0
	length = len(text)
	list = ['p','q','r','s','v','~','(',')','^']
	for n in range(0,length, 1):
		current = text[n]
		if current not in list:
			return 1
		if current.isalpha() and current != 'v':
			if current != 'p' and current != 'q' and current != 'r' and current != 's':
				return 1
		if n < length - 1:
			after = text[n+1]
		if n > 0:
			previous = text[n-1]
		if current == 'p' or current == 'q' or current == 'r' or current == 's': 
			letters += 1
			if n < length - 1:
				if after == 'p' or after == 'q' or after == 'r' or after == 's' or after == '(' or after == '~':
					return 1
		if n == 0 or n == length - 1:
			if current == 'v' or current == '^':
				return 1
		if n == length - 1:
			if current == '~':
				return 1
		if current == '~':
			if n > 0:
				if previous == 'p' or previous == 'q' or previous == 'r' or previous == 's':
					return 1
				if after == 'v' or after == '^': 
					return 1
		if current == 'v' or current == '^':
			if previous != 'p' and previous != 'q' and previous != 'r' and previous != 's':
				return 1
			if after == 'v' or after == '^' or after == ')': 
				return 1		
		if current == '(':
			if n == length-1 or n == length -2:
				return 1
			if n > 0:
				if previous != 'v' and previous != '^' and previous != '(' and previous != '~':
					return 1
			if after == ')' or after == 'v' or after == '^':
				return 1
			leftBracket += 1;
		if current == ')':
			if n == 0 or n == 1:
				return 1
			if previous == '~' or previous == 'v' or previous == '^':
				return 1
			if after != 'v' and after != '^' and after != ')':
				return 1
			if n == length - 2 and after != ')':
				return 1
			rightBracket += 1
	if letters == 0 or letters == length or leftBracket != rightBracket:
		return 1
	else:
		return 0