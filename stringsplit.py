def split_string(string,ch,inte):

	q = string 
	c = ch
	i = inte
	s =list(q)
	#Check if integer value is negative or positive 
	if i <= 0:
		# split the string one time 
		r1 = split_once(s,c)
		print r1
	else:
		#split according to the integear value
		r2 = split_acc_intger(s,c,i)
		print r2
def split_once(s,c):
	y = 0
	d = []
	for x in range(len(s)):
		if s[x] == c:
			p=s[y:x]
			d.append(''.join(p))
			y = x + 1
		elif x == len(s)-1:
			p=s[y:]
			d.append(''.join(p))
	return d

def split_acc_intger(s,c,i):
	y = 0
	d =[]
	count = 1
	for x in range(len(s)):
		# the leat number will 1
		if s[x] == c:
			p=s[y:x]
			d.append(''.join(p))
			y = x + 1
			count += 1
		elif count == i :
			p=s[y:]
			d.append(''.join(p))
			break
	return d




split_string('192.168.16.1','.',3)



