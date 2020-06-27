print("Coded BY Arnav MEhta")
def main():
	print('standard form of a quadratic: ax^2 + bx + c = 0')
	print('Put your quadratic in standard form.')

	a = float(input("What is \"a\" without variable? "))
	b = float(input("What is \"b\" without variable? "))
	c = float(input("What is \"c\" or constant term? "))
	option_1 = 0
	option_2 = 0

	if ((b*b)-(4*a*c)) < 0:
		print('answer involves imaginary numbers')
	else:
		root1 = ((-b + (((b*b)-(4*a*c))**(1/2)))/(2*a))
		root2 = ((-b - (((b*b)-(4*a*c))**(1/2)))/(2*a))
	print(f"\nfirst root is {root1}")
	print(f"Second root is {root2}")

	d = (b*b)-(4*a*c)
	print(f' Also the D is {int(d)}\n \n')
	
if __name__ == "__main__":
		# ~ for i in range(1,9999):
			# ~ main()
	while True:
		main()
