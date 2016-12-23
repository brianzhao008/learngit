varA = 883774
varB = 8888383


x = type(varA)
y = type(varB)

print x,y

if type(varA) is int and type(varB) is int:
    if varA > varB:
        print "bigger"
    elif varA == varB:
        print "equal"
    elif varA < varB:
        print "smaller"
else:
    print "string involved"