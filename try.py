def adjective_to_verb(sentence, index):
	verb = sentence.split(" ")[index]

	if verb[-1] == ".":
		verb = verb[:-1]
	return verb + "en"
