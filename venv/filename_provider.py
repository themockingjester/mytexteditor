class filename_provider():
    def __init__(self, str2):
        str2 = str(str2)
        str2 = str2[::-1]
        self.str = str2
        str1 = ''
        for i in self.str:
            if i != '/':
                str1 = str1 + i
            else:
                break
        str1 = str1[::-1]
        print(str1)
        self.output = str1
        self.get

    def get(self):
        print(self.output)
        return self.output
