#Used to add Dictionary Info
dict = {"apples":5,"pears":12,"bananas":92}

print dict

#get length of Dictionary
print ("Dict is {} long".value(len(dict)))

#Add Value to dictiionary
print "\nAdd Value to Dictionary"
dict["strawberrys"]=32
print dict

#Remove value from dictionary
print "\nRemove Value from Dictionary"
del dict["pears"]
print dict

#Test Dictionary
if "carrot" in dict:
  print "There are no Carrots in Dict !!"
else
  print "We have Carrots!!"

#Loop through Dictionary
print "\nLoop through Dictionary"
for fruit,val in dict.items():
  print "We have {} {}".value(val,fruit)
