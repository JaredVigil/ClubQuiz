from option import option

class question:
	text = ""
	num = 0
	qOption = []
	
	def __init__(self ,text, num, qOption):
		self.text = text
		self.num = num
		self.qOption = qOption
		
	def make_optionArry(a,aOnum,pointA,b,bOnum,pointB,c,cOnum,pointC,d,dOnum,pointD):
		optionA = option(a,aOnum,pointA)
		optionB = option(b,bOnum,pointB)
		optionC = option(c,cOnum,pointC)
		optionD = option(d,dOnum,pointD)
		oArray = [optionA,optionB,optionC,optionD]
		return oArray
		
