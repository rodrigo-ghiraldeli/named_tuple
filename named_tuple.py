from collections import namedtuple

n_t = namedtuple('jogador', ['nome', 'time', 'camisa'])

print(n_t)

j = n_t('Ronaldo', 'Brasil', 9)

print(j)

print(j[0])
print(j[::2])
print(j.nome)