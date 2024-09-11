# classe
class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome # public
        self._idade = idade # protected
        self.__email = email # private

    # metodo get idade
    @property
    def idade(self):
        return self._idade
    
    # metodo set idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

 # metodo get email
    @property
    def email(self):
        return self.__email
    
    # metodo set idade

    @email.setter
    def email(self, email):
        self.__email = email
    
    
    
    
    
    
    
    '''
    # método de acesso (forma de como "errada")
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email

    def get_idade(self):
        return self._idade
    
    def set_idade(self, idade):
        self._idade = idade
'''
    
