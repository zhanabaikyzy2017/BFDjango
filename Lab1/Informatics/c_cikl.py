import math

a= int(input())
b = int(input())

while a<=b:
	srt = int(math.sqrt(a))
	if srt*srt == a:
		print (a)
	a=a+1	