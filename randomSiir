import random
def listToString(str):

    str1 = ""

    for con in str:
        str1 += con
    return str1

def siirverici():
	value1 = random.randint(0,23)
	f = open("textfile.txt", "r+")
	content = f.read()
	x = content.splitlines()

	if value1 == 0:
		value1 = 4
	else:
		pass
	value2 = (value1 - 1)*4
	value3 = value1*4
	data = x[value2:value3]
	value = 0
	line_count = 0
	for line in data:
		if line !="\n":
			line_count += 1

	msg = str(data)
	msg = "\n".join([str(i) for i in data])
	return(msg)
