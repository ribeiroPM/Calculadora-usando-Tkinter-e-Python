import tkinter as tk
root  = tk.Tk()

def mostra_na_tela(oq_exibir=""):
	# Label onde sera exibido o resultado
	tamanho_maximo = 46
	# Limpando a tela
	tk.Label(reponse_frame, text=" "*tamanho_maximo, font=('Arial', 30)).grid(column=0, row=0)

	# Exibindo a reposta na janela
	label = tk.Label(reponse_frame, text=f"{oq_exibir}", font=('Arial', 30))
	label.grid(column=0, row=0)


def limpar_tela():
	mostra_na_tela()

def limpar_equacao():
	pass

def tratar_equacao():
	pass

def resolver_equacao():
	global equacao
	operador = equacao['operador']
	n1 = float(equacao['numeros'][0])
	n2 = float(equacao['numeros'][1])
	resposta = ''
	if operador == '+':
		resposta = n1 + n2
	if operador == '-':
		resposta = n1 - n2
	if operador == '*':
		resposta = n1 * n2
	if operador == '/':
		resposta = n1 / n2

	return resposta

def forma_equacao(numero):
	global equacao
	if equacao['operador'] == None:
		onde_alterar = 0
	else:
		onde_alterar = 1
	equacao['numeros'][onde_alterar] += numero
	print(equacao)
	mostra_na_tela(equacao['numeros'][onde_alterar])

def adicionar_operador(operador):
	global equacao
	limpar_tela()
	if equacao['operador'] ==  None:
		equacao['operador'] = operador
	else:
		resultado = resolver_equacao()
		mostra_na_tela(resultado)
		if equacao['operador'] != '=':
			equacao['numeros'][0] = str(resultado)
			equacao['numeros'][1] = ''
			equacao['operador'] = None

		
		
# Definindo o Tamanho da Janela
root.geometry("450x600")

# Definindo o nome da janela
root.title("Calculadora simples")

# Criando o frame onde serão exibidas as respostas
reponse_frame = tk.Frame(root)
reponse_frame.pack()

# Equação que sera alterada durante a execução do programa
equacao = {"numeros": ['', ''], "operador": None}

# Iniciando o mostrador
mostra_na_tela()

# >>>>> Funções responsaveis por pegar os caracteres escolhidos
def add_equacao_9():
	forma_equacao('9')
def add_equacao_8():
	forma_equacao('8')
def add_equacao_7():
	forma_equacao('7')
def add_equacao_6():
	forma_equacao('6')
def add_equacao_5():
	forma_equacao('5')
def add_equacao_4():
	forma_equacao('4')
def add_equacao_3():
	forma_equacao('3')
def add_equacao_2():
	forma_equacao('2')
def add_equacao_1():
	forma_equacao('1')
def add_equacao_0():
	forma_equacao('0')
def add_equacao_ponto():
	forma_equacao('.')

def add_equacao_mais():
	adicionar_operador('+')
def add_equacao_menos():
	adicionar_operador('-')
def add_equacao_vezes():
	adicionar_operador('*')
def add_equacao_div():
	adicionar_operador('/')
def add_equacao_igual():
	adicionar_operador('=')



# >>>>> Criando o teclado da calculadora
keyboard_frame = tk.Frame(root)
keyboard_frame.columnconfigure(0, weight=1)
keyboard_frame.columnconfigure(1, weight=1)
keyboard_frame.columnconfigure(2, weight=1)
keyboard_frame.columnconfigure(3, weight=1)

# Botões numéricos
botao_9 = tk.Button(keyboard_frame, text="9", command=add_equacao_9, font=('Arial', 18))
botao_9.grid(row=1, column=0, sticky=tk.W+tk.E)
botao_8 = tk.Button(keyboard_frame, text="8", command=add_equacao_8, font=('Arial', 18))
botao_8.grid(row=1, column=1, sticky=tk.W+tk.E)
botao_7 = tk.Button(keyboard_frame, text="7", command=add_equacao_7, font=('Arial', 18))
botao_7.grid(row=1, column=2, sticky=tk.W+tk.E)
botao_6 = tk.Button(keyboard_frame, text="6", command=add_equacao_6, font=('Arial', 18))
botao_6.grid(row=2, column=0, sticky=tk.W+tk.E)
botao_5 = tk.Button(keyboard_frame, text="5", command=add_equacao_5, font=('Arial', 18))
botao_5.grid(row=2, column=1, sticky=tk.W+tk.E)
botao_4 = tk.Button(keyboard_frame, text="4", command=add_equacao_4, font=('Arial', 18))
botao_4.grid(row=2, column=2, sticky=tk.W+tk.E)
botao_3 = tk.Button(keyboard_frame, text="3", command=add_equacao_3, font=('Arial', 18))
botao_3.grid(row=3, column=0, sticky=tk.W+tk.E)
botao_2 = tk.Button(keyboard_frame, text="2", command=add_equacao_2, font=('Arial', 18))
botao_2.grid(row=3, column=1, sticky=tk.W+tk.E)
botao_1 = tk.Button(keyboard_frame, text="1", command=add_equacao_1, font=('Arial', 18))
botao_1.grid(row=3, column=2, sticky=tk.W+tk.E)
botao_0 = tk.Button(keyboard_frame, text="0", command=add_equacao_0, font=('Arial', 18))
botao_0.grid(row=4, column=1, sticky=tk.W+tk.E)
botao_ponto = tk.Button(keyboard_frame, text=".", command=add_equacao_ponto, font=('Arial', 18))
botao_ponto.grid(row=4, column=0, sticky=tk.W+tk.E)

# Botões de operações
botao_igual = tk.Button(keyboard_frame, text="+", command=add_equacao_mais, font=('Arial', 18))
botao_igual.grid(row=1, column=3, sticky=tk.W+tk.E)
botao_menos = tk.Button(keyboard_frame, text="-", command=add_equacao_menos, font=('Arial', 18))
botao_menos.grid(row=2, column=3, sticky=tk.W+tk.E)
botao_vezes = tk.Button(keyboard_frame, text="x", command=add_equacao_vezes, font=('Arial', 18))
botao_vezes.grid(row=3, column=3, sticky=tk.W+tk.E)
botao_div = tk.Button(keyboard_frame, text="/", command=add_equacao_div, font=('Arial', 18))
botao_div.grid(row=4, column=3, sticky=tk.W+tk.E)
botao_div = tk.Button(keyboard_frame, text="=", command=add_equacao_igual, font=('Arial', 18))
botao_div.grid(row=4, column=2, sticky=tk.W+tk.E)

# Coloca o teclado na tela, de forma que o tamanho fique igualitario ate as bordas da tela
keyboard_frame.pack(fill="x")



# ao chegar neste ponto, o script volta a execução de onde root foi criado
root.mainloop()
