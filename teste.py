# Simplesmente irá iniciar o tkinter
# E tambem iniciar uma tela em tamanho padrao, mas redimensionavel
import tkinter as tk
root  = tk.Tk()


# Vai pré-definir o tamanho da Janela
root.geometry("500x500")

# Define o titulo da janela
root.title("Minha primeira Interface Grafica (GUI")

# Inserindo uma label
# Definindo onde sera exposta: root
# Definindo o texto
# Definindo a fonte e seu tamanho
# E de fato colocando a Label na tela, usando pack
label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=25, pady=25)

# Criando um caixa de texto
# Para textos mais extensos
textbox = tk.Text(root, height=3, font=('Arial', 16))
textbox.pack()

# Criando uma caixa de texto menor
# Para textos menores, sem quebra de linha
myentry = tk.Entry(root)
myentry.pack()

# Criando botoes
btn = tk.Button(root, text="Clique aqui", font=('Arial', 18))
btn.pack()

# Criando botoes, porem em formato de colunas e linhas, uma tabela
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

# Empacotando, usando o fill=x para preencher todas as bordas laterais ate o proximo elemento, ou fim da janela
buttonframe.pack(fill="x")


# Criando um botao usando place, para definir tamanho e localização na hora de colocar na tela
outrobtn = tk.Button(root, text="Testando")
outrobtn.place(x=300, y=200, height=100, width=100)

# ao chegar neste ponto, o script volta a execução de onde root foi criado
root.mainloop()