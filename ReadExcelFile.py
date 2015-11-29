# A code that reads a sheet from an excel file ( xlsx ) and sorts the 
# the file based on the index column 
# pip install xlrd
# pip install xlwt


import xlrd

workbook = xlrd.open_workbook('MastersWork.xlsx')
sheet = workbook.sheet_by_name('Sheet1')

for j in range(0,6):
	for i in range(0,3):
		print (sheet.cell(i,j))
		print (" i j ",i,j)
for i in range(0,3):
  sheet.cell(i,0).value = sheet.cell(i+1,0).value

cell = sheet.cell(0,0)
cell1 = sheet.cell(1,0)
print cell.value == cell1.value #xlrd.XL_CELL_NUMBER
