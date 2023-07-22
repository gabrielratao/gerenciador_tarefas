import tkinter as tk
import sys
import crud as cd


banco = cd.Data()

taskOne = cd.Task()
taskOne.setDate('2023-07-20')
taskOne.setTitle('Limpar o Quarto')
taskOne.setTaskDescription('Arrumar as roupas do gabideiro e tirar a tela da mesa e arrumar os fios')
taskOne.setDeliverDate('2023-07-21')
banco.addTask(taskOne)

taskTwo = cd.Task('2', '2023-07-22', 'Arrumar Cozinha', 'Lavar a louça e guardar os pratos e talheres', '2023-07-23')
banco.addTask(taskTwo)


class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, msg):
        self.widget.configure(state="normal")
        self.widget.insert("end", msg, (self.tag,))
        self.widget.configure(state="disabled")

def on_button1_click():
    print(banco.getData())

def on_button2_click():
    def submit_value():
        valor = input_entry.get()
        print(banco.getTaskById(valor))
        
        input_entry.destroy()  # Remove o campo de entrada após o uso
        submit_button.destroy()
    # Criando uma entrada de texto para inserir valores
    input_entry = tk.Entry(root, width=20)
    input_entry.pack(pady=5)

    # Criando um botão para submeter o valor inserido
    submit_button = tk.Button(root, text="Enviar", command=submit_value)
    submit_button.pack(pady=5)

def on_button3_click():
    print("Botão 3 foi clicado!")

def limpar_texto():
    text_area.configure(state="normal")
    text_area.delete(1.0, tk.END)
    text_area.configure(state="disabled")

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de Interface Gráfica")

# Definindo o tamanho da janela
largura = 1000
altura = 500
root.geometry(f"{largura}x{altura}")

# Criando os botões
button1 = tk.Button(root, text="Visualizar Tasks", command=on_button1_click)
button2 = tk.Button(root, text="Visualizar Task pela Id", command=on_button2_click)
button3 = tk.Button(root, text="Botão 3", command=on_button3_click)
button_limpar = tk.Button(root, text="Limpar", command=limpar_texto)

# Posicionando os botões na janela
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button_limpar.pack(pady=10)

# Criando uma área de texto para exibir as mensagens
text_area = tk.Text(root, height=12, width=100)
text_area.pack(pady=20)

# Criando uma entrada de texto para inserir valores
# input_entry = tk.Entry(root, width=20)
# input_entry.pack(pady=5)

# Redirecionando a saída padrão (stdout) para a área de texto
sys.stdout = TextRedirector(text_area, "stdout")

# Iniciando o loop de eventos
root.mainloop()
