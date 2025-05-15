class Veiculo:
    def __init__(self, id, placa, modelo, capacidade_carga):
        self.__id = id
        self.__placa = placa
        self.__modelo = modelo
        self.__capacidade_carga = capacidade_carga

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, value):
        self.__placa = value

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, value):
        self.__modelo = value

    @property
    def capacidade_carga(self):
        return self.__capacidade_carga

    @capacidade_carga.setter
    def capacidade_carga(self, value):
        self.__capacidade_carga = value


    def calcular_custo(self, distancia):
        return distancia * self.__capacidade_carga * 0.1

    def __str__(self):
        return f"Veículo ID: {self.__id}, Placa: {self.__placa}, Modelo: {self.__modelo}, Capacidade: {self.__capacidade_carga}kg"