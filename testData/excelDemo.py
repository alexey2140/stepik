#import openpyxl

#book = openpyxl.load_workbook("/Users/alexcosy/Downloads/PythonExcelDemo.xlsx")
#sheet = book.active
#cell = sheet.cell(row=1, column=2)
#print(cell.value)

#cellWithNameTC1 = sheet.cell(row=2, column=2)

#print(cellWithNameTC1.value)

#cellWithNameTC1.value = "Alex"

#print(cellWithNameTC1.value)

#print(sheet.max_row)

#print(sheet.max_column)

#print(sheet['A5'].value)

#print("----ALL CELLS----")

#for column in range(1, sheet.max_column + 1):
#    print("--------")
#    for i in range(1, sheet.max_row + 1):
#        print(sheet.cell(row=i, column=column).value)

adminUsername = "v_adm1"
adminPassword = "Qwerty1!"

formTemplateLink = "https://maportalqa.medavante.net/designer/form/2381e139-2018-45a7-9d6f-792d530bfa57/designer/page/2/block/46a5f762-8770-4ed5-bed9-635e4d11cf31"
