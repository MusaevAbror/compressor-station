from abc import ABC, abstractmethod
from settings import db_path
import sqlite3
class BaseModel(ABC):
    def __init__(self, id = None):
        self.id = id
        self.__isValid = True

    @property
    def isValid(self):
        return self.__isValid
    @isValid.setter
    def isValid(self, isValid):
        self.__isValid = isValid

    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def objects():
        pass
    
    # @abstractmethod
    # def get_by_id(self):
    #     pass

    # @abstractmethod
    # def delete(self):
    #     pass

class TableAvariy(BaseModel):
    table = "avariya"
    def __init__(self, temM1, temM2, temT1, temT2, vib_M1, vib_M2, gaz, pojar, obM1, obM2, date, time, cause, id = None):
        super().__init__(id)
        self.temM1 = temM1
        self.temM2 = temM2
        self.temT1 = temT1
        self.temT2 = temT2
        self.vib_M1 = vib_M1
        self.vib_M2 = vib_M2
        self.gaz = gaz
        self.pojar = pojar
        self.date = date
        self.obM1 = obM1
        self.obM2 = obM2
        self.time = time
        self.cause = cause


    @property
    def temM1(self):
        return self.__temM1
    @temM1.setter
    def temM1(self, temM1):
        if isinstance(temM1, str):
            self.__temM1 = temM1
        else :
            self.__temM1 = '0'
            print("Asas")
            self.__isValid = False
    
    @property
    def temM2(self):
        return self.__temM2

    @temM2.setter
    def temM2(self, temM2):
        if isinstance(temM2, str):
            self.__temM2 = temM2
        else :
            self.__temM2 = '0'
            self.__isValid = False
    
    
    @property
    def temT1(self):
        return self.__temT1
    
    @temT1.setter
    def temT1(self, temT1):
        if isinstance(temT1, str):
            self.__temT1 = temT1
        else:
            self.__temT1 = '0'
            self.__isValid = False

    @property
    def temT2(self):
        return self.__temT2
    
    @temT2.setter
    def temT2(self, temT2):
        if isinstance(temT2, str):
            self.__temT2 = temT2
        else :
            self.__temT2 = '0'
            self.__isValid = False

    @property
    def vib_M1(self):
        return self.__vib_M1

    @vib_M1.setter
    def vib_M1(self, vib_M1):
        if isinstance(vib_M1, str):
            self.__vib_M1 = vib_M1
        else:
            self.__vib_M1 = ' '
            self.__isValid = False
    
    
    @property
    def vib_M2(self):
        return self.__vib_M2

    @vib_M2.setter
    def vib_M2(self, vib_M2):
        if isinstance(vib_M2, str):
            self.__vib_M2 = vib_M2
        else :
            self.__vib_M2 = ' '
            self.__isValid = False
    
   
    @property
    def gaz(self):
        return self.__gaz

    @gaz.setter
    def gaz(self, gaz):
        if isinstance(gaz, str):
            self.__gaz = gaz
        else :
            self.__gaz = ""
            self.__isValid = False
    @property
    def pojar(self):
        return self.__pojar

    @pojar.setter
    def pojar(self, pojar):
        if isinstance(pojar, str):
            self.__pojar = pojar
        else :
            self.__pojar = " "
            self.__isValid = False




    @property
    def obM1(self):
        return self.__obM1
    
    @obM1.setter
    def obM1(self, obM1):
        if isinstance(obM1, str):
            self.__obM1 = obM1
        else :
            self.__obM1 = " "
            self.__isValid = False
    
    @property
    def obM2(self):
        return self.__obM2
    
    @obM2.setter
    def obM2(self, obM2):
        if isinstance(obM2, str):
            self.__obM2 = obM2
        else :
            self.__obM2 = " "
            self.__isValid = False

    
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self.__date = date
        else :
            self.__date = ''
            self.__isValid = False

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        if isinstance(time, str):
            self.__time = time
        else :
            self.__time = ""
            self.__isValid = False

    @property
    def cause(self):
        return self.__cause

    @cause.setter
    def cause(self, cause):
        if isinstance(cause, str) :
            self.__cause = cause
        else:
            self.__cause = " "
            self.__isValid = False
        

    def save(self):
        if self.isValid:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                if self.id is None:
                    print(self.cause)
                    cursor.execute(f'''INSERT INTO {TableAvariy.table} (Температура_М1, Температура_М2, Температура_Т1, Температура_Т2, Выбрация_М1, Выбрация_М2, Степен_Газа, Пожар, Обород_М1, Обород_М2, Дата, Время, Причина)
                    VALUES ('{self.temM1}', '{self.temM2}', '{self.temT1}', '{self.temT2}', '{self.vib_M1}', '{self.vib_M2}', '{self.gaz}', '{self.pojar}', '{self.obM1}', '{self.obM2}', '{self.date}', '{self.time}', '{self.cause}')''')
                    self.id = cursor.lastrowid
                    print("Save qilindi")
                else :
                    cursor.execute(f'''UPDATE {TableAvariy.table} set Температура_М1 = '{self.temM1}', Температура_М2 = '{self.temM2}',
                    Температура_Т1 = '{self.temT1}', Температура_Т2 = '{self.temT2}', Выбрация_М1 = '{self.vib_M1}', Выбрация_М2 = '{self.vib_M2}', Степен_Газа = '{self.pojar}', , Пожар = '{self.pojar}', Обород_М1 = '{self.obM1}', Обород_М2 = '{self.obM2}', Дата = '{self.date}', Время = '{self.time}', Причина = '{self.cause}' where id {self.id}''')
                conn.commit()

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            res = cursor.execute(f'''SELECT *From {TableAvariy.table}''')
            
            for item in res:
                yield TableAvariy(item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[11], item[12], item[13], item[0])
            conn.commit()
    
    def __str__(self) -> str:
        return f'{self.temM1}, {self.temM2}, {self.temT1}, {self.temT2}, {self.vib_M1}, {self.vib_M2}, {self.gaz}, {self.pojar}, {self.obM1}, {self.obM2}, {self.date}, {self.time}, {self.cause}, {self.id}'
