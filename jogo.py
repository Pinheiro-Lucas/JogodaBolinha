from graphics import *
import time

# Variáveis globais
resolucao = 500
fundo = color_rgb(33, 33, 33)
botoes = color_rgb(255, 248, 171)
dificuldade = 2
acabou = False

# Cria o Menu Principal
jogo = GraphWin('Menu do Jogo', resolucao, resolucao, autoflush=False)
jogo.setBackground(fundo)

# Função de animação (futura)
def animacao(self, x, y):
    self.undraw()
    self.move(x, y)
    self.draw(jogo)
    time.sleep(1)
    self.undraw()
    self.move(-x, -y)
    self.draw(jogo)
    time.sleep(1)

# Animação de seleção
def resetar_outline(listaop, s):
    global fundo
    for element in listaop:
        if listaop.index(element) == s - 1:
            element.setOutline('white')
        else:
            element.setOutline(fundo)

# Função do Retângulo
def retangulo(x1, y1, x2, y2):
    global botoes, resolucao, jogo
    self = Rectangle(Point(resolucao * (x1 / 100), resolucao * (y1 / 100)),
                     Point(resolucao * (x2 / 100), resolucao * (y2 / 100)))
    self.setWidth(3)
    self.setFill(botoes)
    self.draw(jogo)
    return self

# Função do Texto
def texto_ret(ret, msg):
    global fundo, resolucao, jogo
    self = Text(ret.getCenter(), msg)
    self.setTextColor(fundo)
    self.setStyle('bold')
    self.setFace('times roman')
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25, 1500: 30}
    self.setSize(tamanho_normal[resolucao])
    self.draw(jogo)
    return self

# Função de Texto sem Retângulo
def texto_sem_ret(x, y, t, msg):
    global botoes, resolucao, jogo
    self = Text(Point(resolucao*(x/100), resolucao * (y/100)), msg)
    self.setStyle('bold')
    self.setTextColor(botoes)
    self.setFace('times roman')
    if t:
        tamanho_maior = {250: 15, 500: 20, 750: 25, 1000: 30, 1500: 35}
        self.setSize(tamanho_maior[resolucao])
        self.draw(jogo)
        return self
    tamanho_normal = {250: 10, 500: 15, 750: 20, 1000: 25, 1500: 30}
    self.setSize(tamanho_normal[resolucao])
    self.draw(jogo)
    return self

# Função da Bolinha
def bola(x, y):
    global jogo, resolucao
    raio = {250: 5, 500: 10, 750: 15, 1000: 20, 1500: 25}
    self = Circle(Point(resolucao*(x/100), resolucao * (y/100)), raio[resolucao])
    self.setFill('red')
    self.setOutline('red')
    self.draw(jogo)
    return self

# Função para Mudar a Resolução
def mudar_resolucao():
    global jogo, resolucao, fundo
    jogo.close()
    jogo = GraphWin('Menu do Jogo', resolucao, resolucao)
    jogo.setBackground(fundo)

# Função de limpar o Menu
def limpar(lista):
    for _ in lista:
        _.undraw()

# Menu de Resolução
def menu_resolucao():
    global resolucao, jogo, fundo
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 15, 95, 5)
    op2 = retangulo(5, 30, 95, 20)
    op3 = retangulo(5, 45, 95, 35)
    op4 = retangulo(5, 60, 95, 50)
    op5 = retangulo(5, 75, 95, 65)
    op6 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '250x250')
    texto2 = texto_ret(op2, '500x500')
    texto3 = texto_ret(op3, '750x750')
    texto4 = texto_ret(op4, '1000x1000')
    texto5 = texto_ret(op5, '1500x1500')
    texto6 = texto_ret(op6, '< Voltar')

    lista = (op1, op2, op3, op4, op5, op6, texto1, texto2, texto3, texto4, texto5, texto6)

    while not selecionou:
        teclas = jogo.checkKey()

        # Setinha p/ cima
        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        # Setinha p/ baixo
        elif teclas == 'Down':
            if selecionado != 6:
                selecionado += 1
        # Enter
        elif teclas == 'Return':
            if selecionado != 6:
                opcoes = [250, 500, 750, 1000, 1500]
                resolucao = opcoes[selecionado - 1]
                mudar_resolucao()
            limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = [op1, op2, op3, op4, op5, op6]
        resetar_outline(listaop, selecionado)

# Menu de Dificuldade
def menu_dificuldade():
    global fundo, resolucao, dificuldade
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 30, 95, 20)
    op2 = retangulo(5, 45, 95, 35)
    op3 = retangulo(5, 60, 95, 50)
    op4 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, 'FÁCIL')
    texto2 = texto_ret(op2, 'NORMAL')
    texto3 = texto_ret(op3, 'DIFÍCIL')
    texto5 = texto_ret(op4, '< Voltar')

    dificuldades = ('FÁCIL', 'NORMAL', 'DIFÍCIL')
    texto4 = texto_sem_ret(50, 10, True, f'DIFICULDADE ATUAL: {dificuldades[dificuldade - 1]}')

    lista = (op1, op2, op3, op4, texto1, texto2, texto3, texto4, texto5)

    while not selecionou:
        teclas = jogo.checkKey()

        # Setinha p/ cima
        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
        # Setinha p/ baixo
        elif teclas == 'Down':
            if selecionado != 4:
                selecionado += 1
        # Enter
        elif teclas == 'Return':
            if selecionado != 4:
                opcoes = [1, 2, 3]
                dificuldade = opcoes[selecionado - 1]
            limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = [op1, op2, op3, op4]
        resetar_outline(listaop, selecionado)

def menu_comojogar():
    global fundo, resolucao
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '< Voltar')

    texto2 = texto_sem_ret(50, 10, True, 'COMO JOGAR:')
    texto3 = texto_sem_ret(50, 20, False, 'Você tem três vidas')
    texto4 = texto_sem_ret(50, 25, False, 'Não deixe a bolinha cair')
    texto5 = texto_sem_ret(50, 30, False, 'A velocidade aumenta conforme o tempo')
    texto6 = texto_sem_ret(50, 35, False, 'Utilize as setinhas para controlar a barra')
    texto7 = texto_sem_ret(50, 40, False, 'Recupere a vida coletando os corações')
    texto8 = texto_sem_ret(50, 45, False, 'Aproveite os modos mais desafiadores')

    lista = (op1, texto1, texto2, texto3, texto4, texto5, texto6, texto7, texto8)

    while not selecionou:
        teclas = jogo.checkKey()

        # Enter
        if teclas == 'Return':
            limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = [op1]
        resetar_outline(listaop, selecionado)

def menu_creditos():
    global fundo, resolucao
    selecionou, selecionado = False, 1

    op1 = retangulo(5, 95, 95, 85)

    texto1 = texto_ret(op1, '< Voltar')

    texto2 = texto_sem_ret(50, 10, True, 'CRÉDITOS:')
    texto3 = texto_sem_ret(50, 20, False, 'Lucas Pinheiro')
    texto4 = texto_sem_ret(50, 25, False, 'Thiago Rabelo')
    texto5 = texto_sem_ret(50, 30, False, 'Giulia Yule')
    texto6 = texto_sem_ret(50, 35, False, 'Maria Antônia')
    texto7 = texto_sem_ret(50, 40, False, 'Luiz Falcão')

    lista = (op1, texto1, texto2, texto3, texto4, texto5, texto6, texto7)

    while not selecionou:
        teclas = jogo.checkKey()

        # Enter
        if teclas == 'Return':
            limpar(lista)
            return True
        # ESC
        elif teclas in ['Escape', 'BackSpace']:
            limpar(lista)
            menu_principal()

        # Função para checagem do selecionado
        listaop = [op1]
        resetar_outline(listaop, selecionado)

def jogo_principal():
    global resolucao, fundo, jogo, acabou

    jogo = GraphWin('Jogo da Bolinha', resolucao, resolucao, autoflush=False)
    jogo.setBackground(fundo)

    iniciar, bateuu, bateu_barra, bateu_esq, bateu_dir, bateu_cima = False, False, False, False, False, False

    texto0 = texto_sem_ret(50, 50, True, 'PARA INICIAR O JOGO')
    texto1 = texto_sem_ret(50, 60, True, 'APERTE ENTER')

    while not iniciar:

        teclas = jogo.checkKey()

#       Iniciar quando clicar Enter
        if teclas == 'Return':
            texto = [texto0, texto1]
            limpar(texto)
            iniciar = True
        elif teclas in ['Escape', 'BackSpace']:
            acabou = True

#   Para X:
#   1 = Direita
#  -1 = Esquerda

#   Para Y:
#   1 = Baixo
#  -1 = Cima
    x, y = 1, -1
    bolinha = bola(50, 50)
    margem()
    # Bateu = 40 < x < 60
    if dificuldade == 1:
        barra = retangulo(30, 75, 70, 78)
    elif dificuldade == 3:
        barra = retangulo(45, 75, 55, 78)
    else:
        barra = retangulo(40, 75, 60, 78)
    barra.setWidth(2)
    barra.setOutline('red')

    while not acabou:
        teclas = jogo.checkKey()

        if teclas == 'Right' and barra.getP2().getX() < resolucao-11:
            barra.move(5, 0)
        elif teclas == 'Left' and barra.getP1().getX() > 11:
            barra.move(-5, 0)
        elif teclas in ['Escape', 'BackSpace']:
            acabou = True

        x, y = bateu(bolinha, x, y)
        bolinha.move(resolucao*(x/1000*dificuldade), resolucao*(y/1000*dificuldade))
        update(60)
    exit()


def margem():
    global resolucao, fundo
    self = Rectangle(Point(1, 1), Point(resolucao-1, resolucao-1))
    self.setOutline('red')
    self.setWidth(10)
    self.draw(jogo)
    self = Line(Point(0, resolucao-1), Point(resolucao, resolucao-1))
    self.setOutline(fundo)
    self.setWidth(10)
    self.draw(jogo)

def bateu(ball, x, y):
    global acabou
    raio = {250: 5, 500: 10, 750: 15, 1000: 20, 1500: 25}
    if ball.getCenter().getX() <= raio[resolucao]+5 and ball.getCenter().getY() <= raio[resolucao]+5:
        x, y = 1, 1
        return x, y
    elif ball.getCenter().getX() >= resolucao-raio[resolucao]-6 \
            and ball.getCenter().getY() >= resolucao-raio[resolucao]-6:
        acabou = True
        return x, y
    elif ball.getCenter().getX() <= raio[resolucao]+5:
        x = 1
        return x, y
    elif ball.getCenter().getY() <= raio[resolucao]+5:
        y = 1
        return x, y
    elif ball.getCenter().getX() >= resolucao-raio[resolucao]-6:
        x = -1
        return x, y
    elif ball.getCenter().getY() >= resolucao-raio[resolucao]-6:
        acabou = True
        return x, y

    return x, y

# Menu Principal
def menu_principal():
    global fundo, resolucao, jogo
    selecionado = 1
    selecionou, selecionou_opcao = False, False

    op1 = retangulo(5, 35, 95, 20)
    op2 = retangulo(5, 50, 95, 40)
    op3 = retangulo(5, 65, 95, 55)
    op4 = retangulo(5, 80, 95, 70)
    op5 = retangulo(5, 95, 95, 85)

#   Função texto em prática
    texto0 = texto_sem_ret(50, 10, True, 'MENU PRINCIPAL')
    texto5 = texto_ret(op1, 'JOGAR')
    texto1 = texto_ret(op2, 'RESOLUÇÃO')
    texto2 = texto_ret(op3, 'DIFICULDADE')
    texto3 = texto_ret(op4, 'COMO JOGAR')
    texto4 = texto_ret(op5, 'CRÉDITOS')

    while not selecionou:

        teclas = jogo.checkKey()

#       Setinha p/ cima
        if teclas == 'Up':
            if selecionado != 1:
                selecionado -= 1
#       Setinha p/ baixo
        elif teclas == 'Down':
            if selecionado != 5:
                selecionado += 1
#       Enter
        elif teclas == 'Return':
            lista = [op1, op2, op3, op4, op5, texto0, texto1, texto2, texto3, texto4, texto5]
            limpar(lista)
            if selecionado == 1:
                jogo.close()
                selecionou = True
                jogo_principal()
            elif selecionado == 2:
                selecionou_opcao = menu_resolucao()
            elif selecionado == 3:
                selecionou_opcao = menu_dificuldade()
            elif selecionado == 4:
                selecionou_opcao = menu_comojogar()
            elif selecionado == 5:
                selecionou_opcao = menu_creditos()
#       ESC
        elif teclas in ['Escape', 'BackSpace']:
            exit()

#       Função para checagem do selecionado
        if selecionou_opcao:
            selecionou_opcao = False
            menu_principal()

        listaop = [op1, op2, op3, op4, op5]
        resetar_outline(listaop, selecionado)


# Abre o Menu/Start
menu_principal()