from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference
# Giving the path of the excel file
workbook = load_workbook(r"E:\PythonProject\Hospital (1).xlsx")
# Getting the sheet names
sheet_list = workbook.get_sheet_names()

# Printing the total sheets
# print(sheet_list)

def doc_hos(workbook, sheet_name, doc_num):
    mastersheet = workbook["Mastersheet"]
    for i in range(1, sheet_name.max_row + 1):
        # to check the value in column 1
        if (sheet_name.cell(row=i, column=1).value == doc_num):
            mastersheet.append([cell_value(sheet_name, 1, 1), cell_value(sheet_name, i, 1)])
            for j in range(2, sheet_name.max_column + 1):
                mastersheet.append([cell_value(sheet_name, 1, j), cell_value(sheet_name, i, j)])
                workbook.save(r"E:\PythonProject\Hospital (1).xlsx")

# Defining function
def cell_value(cel1, cel2, cel3):
    # print(len(a))
    return (cel1.cell(row=cel2, column=cel3).value)


if 'Mastersheet' in workbook.sheetnames:
    mas = workbook['Mastersheet']
    workbook.remove(mas)
workbook.create_sheet("Mastersheet")

doc_num = int(input("Enter the Doctor ID : "))
for k in range(0, len(sheet_list)):
    sheetName = workbook[sheet_list[k]]
    doc_hos(workbook, sheetName, doc_num)
"""
mastersheet = workbook.get_sheet_by_name("Mastersheet")
values = Reference(mastersheet, min_col=1, min_row=4,
                   max_col=2, max_row=8)
# for bar graph
chart = BarChart()
chart.add_data(values)
chart.title = " BAR-CHART "
chart.x_axis.title = " X_AXIS "
chart.y_axis.title = " Y_AXIS "
mastersheet.add_chart(chart, "E2")
workbook.save("E:\PythonProject\Hospital (1).xlsx")
"""


mastersheet = workbook.get_sheet_by_name("Mastersheet")
values = Reference(mastersheet, min_col=1, min_row=4,
                   max_col=2, max_row=mastersheet.max_row)
chart = BarChart()
chart.add_data(values)
chart.title = " BAR-CHART "
chart.x_axis.title = " X_AXIS "
chart.y_axis.title = " Y_AXIS "
mastersheet.add_chart(chart, "E2")
workbook.save("E:\PythonProject\Hospital (1).xlsx")
