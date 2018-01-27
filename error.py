
def error(text):
	text.replace(" ","");
	letters = 0
	leftBracket = 0
	rightBracket = 0
	length = len(text)
	for n in range(0,length, 1):
		current = text[n]
		if current.isalpha():
			if current != 'p' and current != 'q' and current != 'r' and current != 's':
				return 16
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
				return 2
		if n == length - 1:
			if current == '~':
				return 14
		if current == '~':
			if n > 0:
				if previous == 'p' or previous == 'q' or previous == 'r' or previous == 's':
					return 3
				if after == 'v' or after == '^': 
					return 4
		if current == 'v' or current == '^':
			if previous != 'p' and previous != 'q' and previous != 'r' and previous != 's':
				return 5
			if after == 'v' or after == '^' or after == ')': 
				return 6		
		if current == '(':
			if n == length-1 or n == length -2:
				return 7
			if n > 0:
				if previous != 'v' and previous != '^' and previous != '(' and previous != '~':
					return 8
			if after == ')' or after == 'v' or after == '^':
				return 9
			leftBracket += 1;
		if current == ')':
			if n == 0 or n == 1:
				return 10
			if previous == '~' or previous == 'v' or previous == '^':
				return 11
			if after != 'v' and after != '^' and after != ')':
				return 12
			if n == length - 2 and after != ')':
				return 15
			rightBracket += 1
	if letters == 0 or letters == length or leftBracket != rightBracket:
		return 13
	else:
		return 0