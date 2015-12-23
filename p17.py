p = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
q = ['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def printnum(num):
	if num == 1000:
		return("onethousand")
	elif 100 < num <= 199:
		return("one"+"hundredand"+printnum(num%100))
	elif 200 <= num <= 999:
		if num%100 == 0:
			return(p[num//100]+"hundred")
		else:
			return(p[num//100]+"hundredand"+printnum(num%100))
	elif num == 100:
		return("onehundred")
	elif 20 <= num <= 99:
		if num%10 == 0:
			return(q[num//10])
		else:
			return(q[num//10]+printnum(num%10))
	elif 0 <= num <20:
		return(p[num])
r = ''
for i in range (1,1001):
	r+=printnum(i)
print(len(r))



