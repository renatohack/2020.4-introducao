#Este programa analisa a renda mensal total e
#gastos com moradia, educação e transporte
#e informa o percentual da renda mensal comprometida
#por cada custo. 

class expenses:
	def __init__(self, typeOfExpense, percentage, totalSalary):
		self.type = typeOfExpense
		self.total = ""
		self.percentageAllowed = percentage
		self.totalAllowed = percentage*totalSalary/100

	def isMore(self, totalSalary):
		if self.total > self.totalAllowed:
			print("Seus gastos totais com", self.type.upper(), "comprometem",  round((self.total/totalSalary)*100, 2), "% de sua renda total. \nO máximo recomendado é de", self.percentageAllowed,"%. \nPortanto, idealmente, o MÁXIMO de sua renda comprometida com", self.type.upper(), "deveria ser de R$",self.totalAllowed,".\n")
		else:
			print("Seus gastos totais com", self.type.upper(), "comprometem",  round((self.total/totalSalary)*100, 2), "% de sua renda total.\nO máximo recomendado é de",self.percentageAllowed,"%. \nSeus gastos estão dentro da margem recomendada.\n")

print("Renda mensal total: R$ ", end = "")
salario = float(input())

moradia = expenses("moradia", 30, salario)
educacao = expenses("educação", 20, salario)
transporte = expenses("transporte", 15, salario)

gastos = [moradia, educacao, transporte]

for i in range (0, len(gastos)):
	print("Gastos totais com ", gastos[i].type,": R$ ", end = "")
	gastos[i].total = float(input())

print("\n")

print("Diagnóstico:")
for i in range (0, len(gastos)):
	gastos[i].isMore(salario)