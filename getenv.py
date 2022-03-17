import os

class Getenv():
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath('.env'))

    def env(self, variable):
        self.file = open(f'{self.path}\\.env')
        for linea in self.file.readlines():
            chart = linea.strip().find('=')
            value1 = linea[ : chart]
            data = linea[chart + 1 : ]
            if(value1 == variable):
                self.file.close()
                return data.strip()
        self.file.close()