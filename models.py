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
    table = 'Dip_Abror'
    def __init__(self, temM1, temM2, temT1, temT2, vib, gaz, pojar, date, obM1, obM2, id = None):
        super().__init__(id)
        self.temM1 = temM1
        self.temM2 = temM2
        self.temT1 = temT1
        self.temT2 = temT2
        self.vib = vib
        self.gaz = gaz
        self.pojar = pojar
        self.date = date
        self.obM1 = obM1
        self.obM2 = obM2


    @property
    def obM1(self):
        return self.__obM1
    @obM1.setter
    def obM1(self, obM1):
        if isinstance(obM1, int):
            self.__obM1 = obM1
        else :
            self.__obM1 = 0
            self.__isValid = False
    @property
    def obM2(self):
        return self.__obM2
    @obM2.setter
    def obM2(self, obM2):
        if isinstance(obM2, int):
            self.__obM2 = obM2
        else :
            self.__obM2 = 0
            self.__isValid = False

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
    def vib(self):
        return self.__vib

    @vib.setter
    def vib(self, vib):
        if isinstance(vib, str):
            self.__vib = vib
        else:
            self.__vib = ' '
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
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self.__date = date
        else :
            self.__date = ''
            self.__isValid = False

    def save(self):
        if self.isValid:
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                if self.id is None:
                    cursor.execute(f'''INSERT INTO {TableAvariy.table} (ТемператураМ1, ТемператураМ2, ТемператураТ1, ТемператураТ2, Выбрация, Степен_Газа, Пожар, date, oborodM1, oborodM2)
                    VALUES ('{self.temM1}', '{self.temM2}', '{self.temT1}', '{self.temT2}', '{self.vib}', '{self.gaz}', '{self.pojar}', '{self.date}', {self.obM1}, {self.obM2})''')
                    self.id = cursor.lastrowid
                else :
                    cursor.execute(f'''UPDATE {TableAvariy.table} Температура М1 = '{self.temM1}', Температура М2 = '{self.temM2}',
                    Температура Т1 = '{self.temT1}', Температура Т2 = '{self.temT2}', Выбрация = '{self.vib}', Степен Газа = '{self.pojar}', date = '{self.date}', oborodM1 = {self.obM1}, oborodM2 = {self.obM2} where id {self.id}''')
                conn.commit()

    def objects():
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            res = cursor.execute(f'''SELECT *From {TableAvariy.table}''')
            for item in res:
                yield TableAvariy(item[1], item[2], item[3], item[4], item[5], item[6], item[7], item[8], item[9], item[10], item[0])
            conn.commit()

    def __str__(self) -> str:
        return f'{self.temM1}, {self.temM2}, {self.temT1}, {self.temT2}, {self.vib}, {self.gaz}, {self.pojar}, {self.date}, {self.id}'



   