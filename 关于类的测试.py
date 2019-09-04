class test:
	def __init__(self, x):
		self.x = x
		self.z = self.x
	
	def change_x(self):
		self.x += 1
		print(self.x)
		print('z' + str(self.z))
		
	def see_x(self):
		print('!' + str(self.x))
		
		
if __name__ == "__main__":
	ts = test(10)
	ts.change_x()
	ts.see_x()
		