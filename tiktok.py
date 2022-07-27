user = input('digite o nome de perfil\n>>>')
n = 1
likes = []
while True:
    like = input('digite o numero de curtidas do video {}\n>>>'.format(n))
    try:
        like = int(like)
        likes.append(like)
    except:
        print('Por favor insira uma entrada válida')
        continue
    quit = input('Encerrar?\n >>>')
    quit = quit.strip().lower()
    if quit == 'sim' or quit == 's':
        break
    n += 1
print('O perfil do {a} teve {b} curtidas com a média de {c} curtidas por video'.format(a = user,b=sum(likes),c=sum(likes)/len(likes)))
