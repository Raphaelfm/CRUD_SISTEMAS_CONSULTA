class Consulta:

    def __init__(self, id_consulta:int, id_paciente:int, id_medico:int, descricao_consulta:str, dt_consulta:str ):
        self.id_consulta=id_consulta
        self.id_paciente=id_paciente
        self.id_medico=id_medico
        self.descricao_consulta=descricao_consulta
        self.dt_consulta=dt_consulta

    def setId_consulta(self, novoic:int):
        self.id_consulta=novoic
    def setId_paciente(self, novoip:int):
        self.id_paciente=novoip
    def setId_medico(self, novoim:int):
        self.id_medico=novoim
    def setDescricao_consulta(self, novod:str):
        self.descricao_consulta=novod
    def setDt_consulta(self, novodc:str):
        self.dt_consulta=novodc

    def getId_consulta(self) ->int:
        return self.id_consulta
    def getId_paciente(self) ->int:
        return self.id_paciente
    def getId_medico(self) -> int:
        return self.id_medico
    def getDescricao_consulta(self) ->str:
        return self.descricao_consulta
    def getDt_consulta(self) ->str:
        return self.dt_consulta
    
