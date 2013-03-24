class copy:
    def method(self):
	from sys import argv
	self.script,self.source,self.copy=argv
	fd=open(self.source,'r')
	self.txt=fd.read()
	fd2=open(self.copy,'w')
	fd2.write(self.txt)
	fd2.close()
	fd.close()
	fd2=open(self.copy,'r')
	self.txt2=fd2.read()
a=copy()
a.method()
