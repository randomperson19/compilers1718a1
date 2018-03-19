def getchar(words,pos):
	""" returns char at pos of words, or None if out of bounds """

	if pos<0 or pos>=len(words): return None

	return words[pos]
	

def scan(text,transition_table,accept_states):
	""" Scans `text` while transitions exist in 'transition_table'.
	After that, if in a state belonging to `accept_states`,
	returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 'q0'
	
	while True:
		
		c = getchar(text,pos)	# get next char
		
		if state in transition_table and c in transition_table[state]:
		
			state = transition_table[state][c]	# set new state
			pos += 1	# advance to next char
			
		else:	# no transition found

			# check if current state is accepting
			if state in accept_states:
				return accept_states[state],pos

			# current state is not accepting
			return 'ERROR_TOKEN',pos
			
	
# the transition table, as a dictionary


td = { 'q0':{ '3':'q1','4':'q1','5':'q1','6':'q1','7':'q1','8':'q1','9':'q1','0':'q2','1':'q2','2':'q3'},
       'q1':{ ':':'q6','.':'q6' },
       'q2':{ '0':'q5','1':'q5','2':'q5','3':'q5','4':'q5','5':'q5','6':'q5','7':'q5','8':'q5','9':'q5',':':'q6','.':'q6'},
       'q3':{ '0':'q4','1':'q4','2':'q4','3':'q4',':':'q6','.':'q6'},
       'q4':{ ':':'q6','.':'q6'},
       'q5':{ ':':'q6','.':'q6'},
       'q6':{ '0':'q7','1':'q7','2':'q7','3':'q7','4':'q7','5':'q7'},
       'q7':{ '0':'q8','1':'q8','2':'q8','3':'q8','4':'q8','5':'q8','6':'q8','7':'q8','8':'q8','9':'q8', }
       } 

# the dictionary of accepting states and their
# corresponding token

ad = { 'q8':'TIME_TOKEN'}


# get a string from input
text = input('Give a 24h clock time: ')

# scan text until no more input
while text:	# that is, while len(text)>0
	
	# get next token and position after last char recognized
	token,position = scan(text,td,ad)
	
	if token=='ERROR_TOKEN':
		print('ERROR_TOKEN')
		break
	
	print("token:",token,"string:",text[:position])
	
	# remaining text for next scan
text = text[position:]
