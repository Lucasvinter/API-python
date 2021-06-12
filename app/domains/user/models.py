class Usuario():
    def __init__(self, cpf, email, telefone, datanascimento, id=None):
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        # self.__datanascimento = datanascimento
        self.__id = id
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def datanascimento(self):
        return self.__datanascimento

    @datanascimento.setter
    def datanascimento(self, datanascimento):
        self.__datanascimento = datanascimento


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def serialize(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'email': self.email,
            'telefone': self.telefone,
            'datanascimento': self.datanascimento
        }