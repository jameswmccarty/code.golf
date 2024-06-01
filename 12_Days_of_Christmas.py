g=("A Partridge in a Pear Tree.","Two Turtle Doves, and","Three French Hens,","Four Calling Birds,","Five Gold Rings,","Six Geese-a-Laying,","Seven Swans-a-Swimming,","Eight Maids-a-Milking,","Nine Ladies Dancing,","Ten Lords-a-Leaping,","Eleven Pipers Piping,","Twelve Drummers Drumming,")
s='On the'
for i,d in enumerate(('First','Second','Third','Fourth','Fifth','Sixth','Seventh','Eighth','Ninth','Tenth','Eleventh','Twelfth')):
	print(s,d,"day of Christmas\nMy true love sent to me")
	if i==0:
		s='\n'+s
	n=i
	while n>-1:
		print(g[n])
		n-=1
