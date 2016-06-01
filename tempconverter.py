#Temperature converter



def conversion():

	while True:
	
		try:
			temp = int(input("Enter a temperature: "))
	
		except ValueError:
			print("Invalid input. Please enter a number.")
			continue

		
	
		else:
		
			while True:
			
				tC = (5/9) * (temp - 32)
				tF = (9/5) * temp + 32
			
				print("Would you like to convert to Fahrenheit or Celius?")
				choice = input("Enter F or C: ")
	
				if choice.lower() == 'f':
					print(tF)
					print("{} C = {} F".format(temp, tF))
					break
				elif choice.lower() == 'c':
					print(tC)
					print("{} F = {} C".format(temp, tC))
					break
				else:
					print("Invalid input. Please enter 'F' or 'C'.")
					continue
				break
		
		print("Would you like to convert again?")
		print("Y/n")
		again = input("> ")
		
		if again != 'n':
			conversion()
		else:
			print("Goodbye.")
			break

		break
	
conversion()
	