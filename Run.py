print('What do you want?\n')
print('Write API Keys to JSON:1')
print('Check the API Keys from JSON:2')
print('Run Tweet:3')
print('Exit:4\n')

num = "none"
num = str(input('Select num?: '))

if num == "1":
	import write_js
elif num == "2":
	import ch_js
elif num == "3":
	import main
	roop = "y"
	while True:
		roop = str(input("\n"+"continue? Y/N: "))
		if roop.lower() == "y":
			import importlib
			importlib.reload(main)
		else:
			break
	print ("exit!")
else:
	print("exit!")
