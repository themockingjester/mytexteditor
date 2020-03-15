
import openpyxl
class Words_Suggestor():
    def __init__(self,str2):
        self.str1=str(str2)
        self.Words_Suggestor_working()
    def list_return(self):
        return self.newlis
    def Words_Suggestor_working(self):
        self.newlis = []
        wb = openpyxl.load_workbook("words_library.xlsx")
        sheet = wb['Sheet1']  # wb.get_sheet_names())
        self.newlis2=[]
        try:

            if ord(self.str1[0]) >= 65 and ord(self.str1[0]) <= 90:

                constforsubtraction = 64
            elif ord(self.str1[0]) >= 97 and ord(self.str1[0]) <= 122:

                constforsubtraction = 96
            else:
                constforsubtraction = -1
            if constforsubtraction > 0:
                columnvalue = ord(self.str1[0]) - constforsubtraction

                for i in range(1, sheet.max_row + 1):
                    value = str(sheet.cell(row=i, column=columnvalue).value)
                    sd=self.str1
                    if sd in value:
                        self.newlis.append(value)


        except:
            pass

