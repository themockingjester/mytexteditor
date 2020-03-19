import openpyxl


class Words_adder():
    def __init__(self,list):

        self.list = list

        wb = openpyxl.load_workbook("words_library.xlsx")
        sheet = wb['Sheet1']  # wb.get_sheet_names())

        for k in self.list:

            try:
                if ord(k[0])>=65 and ord(k[0])<=90:
                    constforsubtraction=64
                elif ord(k[0])>=97 and ord(k[0])<=122:
                    constforsubtraction = 96
                else :
                    constforsubtraction = -1
                if constforsubtraction > 0:
                    columnvalue=ord(k[0])-constforsubtraction
                    ctr=0
                    for i in range(1, sheet.max_row + 1):
                        if ((sheet.cell(row=i, column=columnvalue).value == k)):
                            ctr = 1
                            s = sheet.cell(row=i, column=columnvalue).value
                            # time.sleep(2.5)

                            break
                        else:
                            pass
                    # print("ctr="+ str(ctr))

                    if (ctr == 0):

                        for i in range(1, sheet.max_row + 2):
                            # print('maxrow',sheet.max_row)

                            if str(sheet.cell(row=i, column=columnvalue).value) == 'None':
                                cell = sheet.cell(row=i, column=columnvalue)
                                cell.value = k

                                break

                    else:
                        pass
            except:
                pass

        wb.save("words_library.xlsx")
