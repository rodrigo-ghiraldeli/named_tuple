class Jogador:

    def __init__(self, nome, time, numero):
        self.nome = nome
        self.time = time
        self.numero = numero
        self._t = (self.nome, self.time, self.numero)

    def __repr__(self):
        return f'Jogador(nome={self.nome}, time={self.time}, numero={self.numero})'
    
    def __getitem__(self, numero):
        print('__getitem__')
        return self._t[numero]
    
    def __len__(self):
        return len(self._t)
    
    def count(self, att):
        return len([x for x in self._t if x == att])
    
    def index(self, att):
        for x, y in enumerate(self._t):
            if y == att:
                return x
