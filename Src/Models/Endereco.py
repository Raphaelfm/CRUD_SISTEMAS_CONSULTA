#from conexion.oracle_queries import OracleQueries

class Endereco:

    def __init__(self, id_endereco:int, logradouro:str , numero:str, complemento:str , bairro:str , municipio:str , uf: str,
    cep: str):

        self.id_endereco=  id_endereco
        self.logradouro = logradouro
        self.numero = numero
        self.complemento  = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.uf= uf
        self.cep = cep

    def setid_endereco(self, novo:int):
        self.id_endereco=novo
    def setLogradouro(self, novol:str):
        self.logradouro=novol
    def setNumero(self, novon:str):
        self.numero=novon
    def setComplemento(self, novoc:str):
        self.complemento=novoc
    def set_bairro(self, novob:str):
        self.bairro=novob
    def set_municipio(self, novom:str):
        self.municipio=novom
    def set_uf(self, novou:str):
        self.uf=novou
    def set_cep(self, novoc:str):
        self.cep=novoc

    def getId_endereco(self) ->int:
        return self.id_endereco
    def getLogradouro(self) -> str:
        return self.Logradouro
    def getNumero(self) ->str:
        return self.numero
    def getComplemento(self) ->str:
        return self.complemento
    def getBairro(self) ->str:
        return self.complemento
    def getBairro(self) ->str:
        return self.bairro
    def getMunicipio(self) ->str:
        return self.municipio
    def getUf(self) ->str:
        return self.uf
    def getCep(self) ->str:
        return self.cep
    

    

     





