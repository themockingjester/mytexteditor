class words_filter():
    def __init__(self,str):    
                    str=str.split(" ")
                    lis1=[]
                    for m in str:
                        if '\n' not in m:
                            lis1.append(m)
                        else:
                            lis2=m.split('\n')
                            for u in lis2:
                                lis1.append(u)
                    self.lis3=[]
                    for m in lis1:
                        if '\t' not in m:
                            self.lis3.append(m)
                        else:
                            lis2=m.split('\t')
                            for u in lis2:
                                self.lis3.append(u)


    def output(self):

        lis=set(self.lis3)
        return lis