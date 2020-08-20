import os
import pyttsx3

pyttsx3.speak("Welcome to interactive system.")
print()
print("speak/type which software you want to open with,stating \"run/open\" and name of \"software\". \n eg: can you run notepad for me.")
print()
print("Type \"quit\" or \"exit\" to stop")

print()
while True:
	print("Chat with me: ",end=" ")
	p=input()

	if ("run" in p) or ("open" in p):
	  if("notepad" in p):
	    os.system("notepad")
	  elif("atom" in p):
	    os.system("atom")
	  elif("visual studio" in p) or ("VS code" in p) or ("vs code" in p):
	    os.system("code")    
	  elif("Firefox" in p):
	    os.system("firefox")
	  elif("Chrome" in p) or ("chrome" in p):
	    os.system("chrome")
	  elif("Hyper Terminal" in p) or ("hyper" in p):
	    os.system("hyper")
	  elif("Acrobat Reader" in p):
	    os.system("AcroRd32")
	  elif("KM Player" in p):
	    os.system("KMPlayer") 
	elif("exit" in p) or ("quit"):
	    break
	else:
	  print("wrong input")