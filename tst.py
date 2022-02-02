n=5
for i in range(1,n+1):
	x=65
	for j in range(1,n-i+1):
		print(chr(x)," ",end='')
		x=x+1
	print()
for i in range(n-1,0,-1):
	x=65
	for j in range(1,n-i+1):
		print(chr(x)," ",end='')
		x=x+1
	print()