class mic_feature:
    def __init__(self):
        try:
            import speech_recognition as sr
            import json  # used for catching the exception thrown by google audio
            r = sr.Recognizer()

            ctr = 0

            import openpyxl, time

            u = 1
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                while 1:

                    print("Speak Anything :")
                    # time.sleep(4)
                    try:
                        audio = r.listen(source)

                    except:

                        print("internal problem occured in listening")
                        continue
                    try:

                        text = r.recognize_google(audio, language='en-IN')
                        response = json.dumps(text, ensure_ascii=False).encode(
                            'utf8')  # this is must otherwise above line will throw exception

                        text = text.lower()
                        print(text)
                        wb = openpyxl.load_workbook("training.xlsx")
                        time.sleep(1)
                        sheet = wb['Sheet1']  # wb.get_sheet_names())

                        for i in range(2, sheet.max_row + 1):
                            if ((sheet.cell(row=i, column=1).value == text)):
                                ctr = 1
                                self.s = sheet.cell(row=i, column=2).value
                                # time.sleep(2.5)
                                print(sheet.cell(row=i, column=2).value)
                                break
                            else:
                                pass
                        # print("ctr="+ str(ctr))

                        if (ctr == 0):
                            s = "cant find that in our data"
                            self.s = text

                        else:
                            pass

                    except:
                        s = "can't recognize"

        except:
            print('sry this feature is not supportable in your pc')

    def get(self):
        return self.s
