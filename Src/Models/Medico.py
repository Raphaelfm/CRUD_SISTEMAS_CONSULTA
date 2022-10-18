class Medico(Endereco):

    def __init__(self, id_medico:int, crm:str, nome:str, celular:str, id_endereco:int):
        super().__init__(id_endereco:int, logradouro:str , numero:str, complemento:str , bairro:str , municipio:str , uf: str,cep: str)
        self.id_medico=id_medico
        self.crm=crm
        self.nome=nome
        self.celular=celular
        self.id_endereco=id_endereco
    

    def setId_medico(self, novoim:int):
        self.id_medico=novoim
    def setCrm(self, novoc:str):
        self.crm=novoc
    def setNome(self, novon:str):
        self.nome=novon
    def setCelular(self, novoce:str):
        self.celular=novoce
    def setId_endereco(self, novoe:int):
        self.id_endereco=novoe
    
    def getId_medico(self) ->int:
        return self.id_medico
    def getCrm(self) -> str:
        return self.crm
    def getNome(self) ->str:
        return self.nome
    def getCelular(self) ->str:
        return self.celular
    def getId_endereco(self)->int:
        return self.id_endereco