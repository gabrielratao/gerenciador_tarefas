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
    banco.getData()

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
    def submit_value():
        valor = input_entry.get()
        banco.removeTaksById(valor)
        
        input_entry.destroy()  # Remove o campo de entrada após o uso
        submit_button.destroy()
    # Criando uma entrada de texto para inserir valores
    input_entry = tk.Entry(root, width=20)
    input_entry.pack(pady=5)

    # Criando um botão para submeter o valor inserido
    submit_button = tk.Button(root, text="Enviar", command=submit_value)
    submit_button.pack(pady=5)

def on_button4_click():
    def submit_value():
        id = input_id.get()
        dt_created = input_dt_created.get()
        title = input_title.get()
        task_description = input_task_description.get()
        dt_deliver = input_dt_deliver.get()
        
        if banco.existId(id) == False:
            newTask = cd.Task(id, dt_created, title, task_description, dt_deliver)
            banco.addTask(newTask)
            print(f'{id} task adcionada ao banco')
        else:
            print(f'{id} Task ja existente')
        # Remove o campo de entrada após o uso

        input_id.destroy()  
        input_dt_created.destroy()
        input_title.destroy()
        input_task_description.destroy()
        input_dt_deliver.destroy()
        submit_button.destroy()
        label_valor.destroy()

    # Removendo o texto de instrução quando o usuário interagir com a caixa de entrada
    def remove_placeholderID(event):
        if input_id.get() == "Digite o Id":
            input_id.delete(0, tk.END)
    def remove_placeholder_dt_created(event):
        if input_dt_created.get() == "Digite data criação":
            input_dt_created.delete(0, tk.END)
    def remove_placeholder_title(event):
        if input_title.get() == "Digite o titulo":
            input_title.delete(0, tk.END)
    def remove_placeholder_dt_deliver(event):
        if input_dt_deliver.get() == "Digite a data de entrega":
            input_dt_deliver.delete(0, tk.END)
    def remove_placeholder_task_description(event):
        if input_task_description.get() == "Digite descrição":
            input_task_description.delete(0, tk.END)

    # Criando um rótulo para descrever a caixa de entrada
    label_valor = tk.Label(root, text="Digite as informações para a Task")
    label_valor.pack(pady=5)

    # Criando entradas de texto para inserir valores
    input_id = tk.Entry(root, width=20)
    input_id.pack(pady=5)
    input_id.insert(0, "Digite o Id")
    input_id.bind("<FocusIn>", remove_placeholderID)

    input_dt_created = tk.Entry(root, width=20)
    input_dt_created.pack(pady=5)
    input_dt_created.insert(0, "Digite data criação")
    input_dt_created.bind("<FocusIn>", remove_placeholder_dt_created)

    input_title = tk.Entry(root, width=20)
    input_title.pack(pady=5)
    input_title.insert(0, "Digite o titulo")
    input_title.bind("<FocusIn>", remove_placeholder_title)

    input_dt_deliver = tk.Entry(root, width=20)
    input_dt_deliver.pack(pady=5)
    input_dt_deliver.insert(0, "Digite a data de entrega")
    input_dt_deliver.bind("<FocusIn>", remove_placeholder_dt_deliver)

    input_task_description = tk.Entry(root, width=20)
    input_task_description.pack(pady=5)
    input_task_description.insert(0, "Digite descrição")
    input_task_description.bind("<FocusIn>", remove_placeholder_task_description)

    
    # Criando um botão para submeter o valor inserido
    submit_button = tk.Button(root, text="Enviar", command=submit_value)
    submit_button.pack(pady=5)
    

def limpar_texto():
    text_area.configure(state="normal")
    text_area.delete(1.0, tk.END)
    text_area.configure(state="disabled")

# Criando a janela principal
root = tk.Tk()
root.title("Esqueleto de uma iterface interativa")

# Definindo o tamanho da janela
largura = 1000
altura = 500
root.geometry(f"{largura}x{altura}")

# Criando os botões
button1 = tk.Button(root, text="Visualizar Tasks", command=on_button1_click)
button2 = tk.Button(root, text="Visualizar Task pela Id", command=on_button2_click)
button3 = tk.Button(root, text="Remover Task pela Id", command=on_button3_click)
button4 = tk.Button(root, text="Nova Task", command=on_button4_click)
button_limpar = tk.Button(root, text="Limpar", command=limpar_texto)

# Posicionando os botões na janela
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button_limpar.pack(pady=10)

# Criando uma área de texto para exibir as mensagens
text_area = tk.Text(root, height=12, width=100)
text_area.pack(pady=20)



# Redirecionando a saída padrão (stdout) para a área de texto
sys.stdout = TextRedirector(text_area, "stdout")

# Iniciando o loop de eventos
root.mainloop()
