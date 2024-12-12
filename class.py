class computer:
    def  __init__(self,cpu,ram):
       self.cpu=cpu
       self.ram=ram
    def config(self):
      print(self.cpu)
      print(self.ram)
com1=computer('15','16')
com1.config()
com2=computer('17','18')
com2.config()
