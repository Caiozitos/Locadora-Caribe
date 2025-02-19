from tkinter import *
from PIL import Image, ImageTk
# rgfg
# Back-end ===============================================================================================================================================

# Função de filtro de itens
def filtrarItens(lista, tipoFiltro, filtro):                    # Recebe uma lista de itens, um atributo para filtrar e uma referência de filtro
    listaFinal = []                                             # Criação da lista final que é retornada no final
    if tipoFiltro == "titulo":                                  # Filtragem por título
        for item in lista:
            if item.titulo == filtro:
                listaFinal.append(item)

    elif tipoFiltro == "tipo":                                  # Filtragem por tipo
        for item in lista:
            if item.tipo == filtro:
                listaFinal.append(item)

    elif tipoFiltro == "ano":                                   # Filtragem por ano
        for item in lista:
            if item.ano == filtro:
                listaFinal.append(item)

    elif tipoFiltro == "disponib":                              # Filtragem por disponibilidade
        for item in lista:
            if item.disponib == filtro:
                listaFinal.append(item)

    return listaFinal

# Selecionar o item para mostrar informações e atualizar a interface
def infoItem(item):
    global itemSelecionado
    itemSelecionado = item
    
    # Removendo todos os widgets dentro do display antes de adicionar novos
    for widget in display.winfo_children():
        widget.destroy()

    # Exibir título do item
    tituloItem = Label(display, text="Informações", font=("Arial", 20, "bold"), 
                       background="#3c3d61", foreground="white")
    tituloItem.pack(pady=10)

    # Converter para PhotoImage
    img = Image.open(item.capa)
    img = img.resize((140, 200), Image.LANCZOS) 
    capa = ImageTk.PhotoImage(img)
    capaLabel = Label(display, image=capa)
    capaLabel.image = capa
    capaLabel.pack(anchor="nw",padx=10)

    # Exibindo as informações do item
    


# Função de listar os itens na interface, sempre ao lado esquerdo da tela
def listarItens(lista):                                         # Recebe uma lista de itens para mostrar
    for i, item in enumerate(listaItens):
        # Caixa de cada item
        frame = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
        frame.place(x=520, y=10 + 110 * i, width=500, height=100)

        # Título do item
        titulo = Label(frame, text=item.titulo, fg="white", bg="#3c3d61", font=("Arial", 18, "bold"))
        titulo.pack(padx=5,pady=1,anchor="w")
        
        # Ano e tipo do item
        textoSubtitulo = f"{item.tipo} - {item.ano}"
        subtitulo = Label(frame,text=textoSubtitulo,fg="white", bg="#3c3d61", font=("Arial", 12))
        subtitulo.pack(padx=5,pady=2,anchor="w")

        # Verificando e configurando a disponibilidade do item
        if item.disponib:
            iconeDisp = "disponibilidadeTrue.png"
            textDisp = "Disponível"
            corDisp = "lime"
        else:
            iconeDisp = "disponibilidadeFalse.png"
            textDisp = "Indisponível"
            corDisp = "red"
        
        # Imagem da bolinha
        status = PhotoImage(file=f"Imagens/{iconeDisp}")

        # Mostrando a imagem
        imagem = Label(frame,image=status,highlightthickness=0,background="#3c3d61")
        imagem.image = status
        imagem.pack(padx=3,pady=1,anchor="w",side="left")

        # Mostrando o texto de disponibilidade
        textoimagem = Label(frame,text=textDisp,fg=corDisp,bg="#3c3d61", font=("Arial",10,"bold"))
        textoimagem.pack(padx=3,pady=1,side="left")

        # Mostrando o botão de ver o item selecionado
        botaoVer = Button(frame, text="Ver item", borderwidth=1, highlightbackground="white", highlightthickness=2, 
                  background="#1b1b33", foreground="white", font=("Arial",10,"bold"), 
                  command=lambda item=item: infoItem(item))  

        botaoVer.pack(padx=3,pady=3,anchor="e")
    
# Classe de item
class Item:
    def __init__(self,idNum,titulo,ano,tipo,disponib=True):
        self._id = idNum
        self.ano = ano
        self.titulo = titulo
        self.tipo = tipo
        self.disponib = disponib
        self.estoque = 1
        self.capa = f"Capas/{self._id}.png"


    def getId(self):
        return self._id

global listaItens
listaItens = [
    Item(100, "Forza Horizon 5", "2021", "Jogo"),
    Item(101, "Esquadrão Suicida", "2016", "Filme"),
    Item(102, "The Witcher 3", "2015", "Jogo"),
    Item(103, "Interstellar", "2014", "Filme"),
    Item(104, "Red Dead Redemption 2", "2018", "Jogo"),
    Item(105, "Cyberpunk 2077", "2020", "Jogo"),
    Item(106, "Oppenheimer", "2023", "Filme"),
    Item(107, "The Last of Us Part II", "2020", "Jogo"),
    Item(108, "Duna", "2021", "Filme"),
    Item(109, "God of War Ragnarok", "2022", "Jogo"),
    Item(110, "Avatar: O Caminho da Água", "2022", "Filme"),
    Item(111, "Horizon Forbidden West", "2022", "Jogo"),
    Item(112, "John Wick 4", "2023", "Filme"),
    Item(113, "Spider-Man 2", "2023", "Jogo"),
    Item(114, "Guardiões da Galáxia Vol. 3", "2023", "Filme")
]


# Front-end ===============================================================================================================================================
janela = Tk()
janela.geometry("940x560")
janela.title("Locadora Caribe")
janela["bg"] = "#1b1b33"
janela.resizable(False, False)
janela.attributes("-toolwindow",False)
janela.iconbitmap("Imagens/logoProjetoIco.ico")

itemSelecionado = ""

display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(x=10,y=10,width=395,height=540)

if itemSelecionado == "":
    displayTexto = Label(display, text="Seja bem-vindo à \nLocadora Caribe!!", 
                         font=("Arial", 20, "bold"), background="#3c3d61", 
                         foreground="white")
    displayTexto.pack(pady=20, anchor="center")

    logo = PhotoImage(file="Imagens/logoProjeto.png")
    displayLogo = Label(display,image=logo,background="#3c3d61")
    displayLogo.pack(anchor="center")
    displayLogo.image = logo

    displayTextoMenor = Label(display, 
        text="A Locadora Caribe é um projeto desenvolvido por Caio Enzo Bessa de Oliveira e José Fernandes Figueirêdo Filho, sob a orientação do professor Ciro Daniel Gurgel de Moura, no Instituto Federal do Rio Grande do Norte (IFRN). Criado para simular a experiência de uma locadora moderna, permitindo o aluguel de jogos e filmes por meio de uma interface intuitiva e prática.\n\nSelecione um item para ver suas informações.",
        font=("Arial", 12), background="#3c3d61", foreground="white", 
        wraplength=370, justify="center") 
    displayTextoMenor.pack(pady=5,padx=10,side="bottom") 

listarItens(listaItens)
janela.mainloop()
