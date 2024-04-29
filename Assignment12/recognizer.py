"""
Program: recognizer.py
Author: Cesar Guevara

Modify the grammar checker of this chapter’s Case Study, in the file recognizer.py, 
so that it recognizes the following additional types of variations in phrases:
A verb phrase with no prepositional phrase (example: “The boy saw the girl”).
A noun phrase in which the noun is modified by an adjective (example: “The girl 
hit the red ball with a bat”).
A sentence that connects two independent clauses with a conjunction (example: 
“The boy threw the ball and the girl hit the ball”).
You should add new variables for the sets of adjectives and conjunctions. 
1. Significant constants:
	articles
	nouns
	verbs
	prepositions
2. The inputs are:
	userInput
3. Computations:

4. The outputs are:
	messages to the user
"""
articles = ("A", "THE", "SOME", "ANY")
nouns = ("BOY", "GIRL", "BAT", "BALL", "CAT", "DOG", "PARK", "SCHOOL", "APPLE", "CAR","COMPUTER","PYTHON","SNAKE","BOA")
adjectives = ("RED", "BIG", "SMALL", "BLUE", "YOUNG", "OLD", "HAPPY", "SAD", "TALL", "SHORT","FAST","SLOW")
verbs = ("HIT", "SAW", "LIKED", "THREW", "RAN", "JUMPED", "SLEPT", "ATE", "DRANK", "WROTE","BIT","HELD","DRANK","ATE")
prepositions = ("WITH", "BY", "UNDER", "OVER", "BEFORE", "AFTER", "BESIDE", "ON", "AT")
conjunctions = ("AND", "OR", "BUT", "BECAUSE", "ALTHOUGH", "WHILE", "IF")
# sentence = nounphrase verbphrase {conjunction sentence}
def sentence(words):
	if not words:
		return False
	if nounPhrase(words) and verbPhrase(words):
		if not words:
			return True
		if words[0] in conjunctions:
			words.pop(0)
			return sentence(words)
	return False

# nounphrase = article [adjective] noun
def nounPhrase(words):
	if len(words) < 2:
		return False
	article = words.pop(0)
	if words[0] in adjectives:
		words.pop(0)
	noun = words.pop(0)
	return article in articles and noun in nouns

# verbphrase = verb [nounphrase [prepositionalphrase]]
def verbPhrase(words):
	if not words:
		return False
	verb = words.pop(0)
	if verb not in verbs:
		return False
	if not nounPhrase(words):
		return True  # Allows verb phrases without a following noun phrase
	if words and words[0] in prepositions:
		return prepositionalPhrase(words)
	return True

# prepositionalphrase = preposition nounphrase
def prepositionalPhrase(words):
	if len(words) < 1:
		return False
	preposition = words.pop(0)
	return preposition in prepositions and nounPhrase(words)

def main():
	while True:
		userInput = input("Enter a sentence or press return to quit: ")
		if userInput == "":
			break
		words = userInput.upper().split()
		if sentence(words):
			print("Ok, grammatically correct")
		else:
			print("Not ok, grammatically incorrect")

if __name__ == "__main__":
	main()
