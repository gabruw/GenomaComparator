# Functions
def parse(enter):
	cont = {}

	for i in ['A', 'T', 'C', 'G']:
		for j in ['A', 'T', 'C', 'G']:
			cont[i+j] = 0

	for k in range(len(enter) - 1):
		cont[enter[k] + enter[k+1]] += 1

	# HTML
	i = 1
	for k in cont:
		transp = cont[k]/max(cont.values())
		exit.write("<div style='width: 100px; border: 1px solid #111111; height: 100px; float: left; color: #FFFFFF; background-color: rgba(0, 0, 0, "+ str(transp) +");'>"
						+ k +
					"</div>")
	
		if i%4 == 0:
			exit.write("<div style='clear: both;'></div>")
		i += 1

# Read .txt Documents 
enterH = open("18s_humano.txt").read()
enterB = open("16s_bacteria.txt").read()
exit = open("Result.html", "w")

# Remove break lines
enterH = enterH.replace("\n", "")
enterB = enterB.replace("\n", "")

# Function call
exit.write("<h1>Humano</h1>")
parse(enterH)

exit.write("<br>")

exit.write("<h1>Bactéria</h1>")
parse(enterB)

exit.close()