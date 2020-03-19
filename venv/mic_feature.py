import threading
import openpyxl, time
import speech_recognition as sr
import json  # used for catching the exception thrown by google audio

r = sr.Recognizer()


class mic_feature:
    def __init__(self):

        thread5 = threading.Thread(target=self.working())
        thread5.start()

    def working(self):
        if 1 == 1:

            self.st = ""
            ctr = 0

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.3)
                if 1 == 1:

                    print("Speak Anything :")
                    # time.sleep(4)
                    try:
                        audio = r.listen(source, phrase_time_limit=4)

                    except:

                        print("internal problem occured in listening")

                    try:

                        text = r.recognize_google(audio, language='en-US')
                        response = json.dumps(text, ensure_ascii=False).encode(
                            'utf8')  # this is must otherwise above line will throw exception

                        text = text.lower()

                        '''wb = openpyxl.load_workbook("training.xlsx")
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
                        '''
                        text = text + " "
                        self.st = text

                    except:
                        s = "can't recognize"
            return 0
        else:
            print('couldn\'t understand')

    def get(self):
        return self.st
