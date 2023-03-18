import pyttsx3

n = input("Enter the number  ")

dic = {
  "1" : "ones",
  "2" : "twos",
  "3" : "threes",
  "4" : "fours",
  "5" : "sixs",
  "7" : "sevens",
  "8" : "eights",
  "9" : "nines",
  "10" : "tens"
} 
txt =""
for i in range(1,11):
  mul = i*int(n)
  txt+= str(i) +" "+dic[n] +" are " + str(mul) +"\n"
print(txt)
engine=pyttsx3.init()
engine.setProperty('voice', 'ml')
engine.say(txt)
engine.runAndWait()