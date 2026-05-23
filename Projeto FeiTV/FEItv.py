##EZEQUIEL BOTELHO ROCHA

##RA: 22.126.025.0

##TURMA: 301

##PROFESSOR: MURILO


##FUNÇÃO CADASTRAR USUÁRIO
def cadastrar_usuario():
    Cadastrar_usuario = input("Digite seu novo usuário: ")
    Cadastrar_senha = input("Digite sua nova senha: ")
    
    ##USUÁRIO JA CADASTRADO
    arquivo = open("usuarios.txt", "a+")
    for linha in arquivo:
        dados = linha.strip().split(",")
        usuario_arquivo = dados[0]
        if Cadastrar_usuario == usuario_arquivo:
            print("Usuário ja cadastrado! faça somente o login.")
            arquivo.close()
            return False
    
    ##CADASTRO DO USUÁRIO
    arquivo = open("usuarios.txt", "a")
    arquivo.write(str(Cadastrar_usuario) + "," + str(Cadastrar_senha) + "\n")
    print("\n""Usuário cadastrado com sucesso!""\n")
    arquivo.close()
    return True

##FUNÇÃO LOGIN DE USUÁRIO
def login_usuario():
    Usuario = input("Digite seu usuário: ")
    Senha = input("Digite sua senha: ")
    
    arquivo = open("usuarios.txt", "r")
    for linha in arquivo:
        dados = linha.strip().split(",")
        usuario_arquivo = dados[0]
        senha_arquivo = dados[1]
        if Usuario == usuario_arquivo and Senha == senha_arquivo:
            print("\n""Login realizado com sucesso!")
            arquivo.close()
            return True
    arquivo.close()
    print("Usuário não encontrado! faça o cadastro.")
    return False
   
##FUNÇÃO BUSCAR VÍDEO 
def buscar_video():
    Buscar_video = input("Digite o nome do filme: ")
    
    arquivo = open("videos.txt", "r")
    encontrado = False
    
    for linha in arquivo:
        dados = linha.strip().split(";")
        titulo = dados[0]
        
        if Buscar_video.lower() in titulo.lower():
            print("\n""Filme encontrado:""\n")
            print("Título:", dados[0])
            print("Tempo:", dados[1])
            print("Criador:", dados[2])
            print("Curtidas:", dados[3])
            encontrado = True
            
    if not encontrado:
        print("Filme não encontrado!")   
    arquivo.close()
    enter = input("\n" "clique ENTER para voltar ao menu.")
    
##FUNÇÃO CURTIR VÍDEO    
def curtir_video():
    Buscar_video = input("Digite o nome do filme para curtir: ").strip()
    
    arquivo = open("videos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    for linha in linhas:
        if Buscar_video.lower() in linha.lower():
            arquivo = open("curtidos.txt", "a+")
            arquivo.write(linha.strip() + "\n")
            print("\n""Vídeo curtido e salvo com sucesso!")
            arquivo.close()
            break
    else:
        print("Filme não encontrado.")
    enter = input("\n" "clique ENTER para voltar ao menu.")
    
##FUNÇÃO DESCURTIR VÍDEO    
def descurtir_video():
    Buscar_video = input("Digite o nome do filme para descurtir: ")
    
    arquivo = open("curtidos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    arquivo = open("curtidos.txt", "w")
    for linha in linhas:
        if Buscar_video.lower() not in linha.strip().lower():
            arquivo.write(linha)
            
    print("\n""Curtida removida com sucesso!")
    arquivo.close()
    enter = input("\n" "clique ENTER para voltar ao menu.")
    
##FUNÇÃO CRIAR LISTA DE FAVORITOS
def criar_lista():
    lista = input("Dê um nome para a lista de vídeos favoritos: ")
    
    arquivo = open(lista + ".txt", "a+")
    arquivo.close()
    print("Lista salva!")
    enter = input("\n" "clique ENTER para voltar ao menu.")

##FUNÇÃO PARA EXCLUIR LISTA DE FAVORITOS
def excluir_lista():
    import os
    lista = input("Digite o nome da lista para excluir: ")
    
    if os.path.exists(lista + ".txt"):
        os.remove(lista + ".txt")
        print("Lista excluída com sucesso!")
    else:
        print("Essa lista nao existe.")
    enter = input("\n" "clique ENTER para voltar ao menu.")

##FUNÇÃO DE ADICIONAR VIDEO NA LISTA DE FAVORITOS   
def adicionar_video_lista():
    nome_filme= input("Digite o nome do filme que deseja adicionar na sua lista de favoritos: ")
    nome_lista= input("Digite o nome da lista que deseja salva o seu filme: ")
    
    arquivo = open("videos.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    for linha in linhas:
        if nome_filme.lower() in linha.lower():
            arquivo = open(nome_lista + ".txt", "a")
            arquivo.write(nome_filme + "\n")
            arquivo.close()
            print("Filme adicionado na sua lista de favoritos")
            break
    else:
        print("filme nao encontrado.")
    enter = input("\n" "clique ENTER para voltar ao menu.")        

##FUNÇÃO DE REMOVER VIDEO DA LISTA DE FAVORITOS   
def remover_video_lista():
    nome_filme = input("Digite o nome do filme que deseja remover da sua lista de favoritos: ")
    nome_lista = input("Digite o nome da lista que esta o filme que deseja excluir:  ")   

    arquivo = open(nome_lista + ".txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()

    arquivo = open(nome_lista + ".txt", "w")

    encontrado = False

    for linha in linhas:
        if nome_filme.lower() != linha.strip().lower():
            arquivo.write(linha)
        else:
            encontrado = True
    arquivo.close()
    if encontrado:
        print("Vídeo excluído com sucesso da sua lista de favoritos!")
    else:
        print("Esse vídeo não está na sua lista!")
    input("\nclique ENTER para voltar ao menu.")

##MENU COMPLETO.
    

print ("\n" + "------------------FEItv------------------")
print ("\n" + "Seja Bem-vindo!")


print ("\n" + "Escolha uma opção: ")

print ("\n" + "[1] CADASTRAR USUÁRIO")
print ("[2] LOGIN DE USUÁRIO" + "\n")

OPCAO = input("escolha uma opção: ")

logado = False

if OPCAO == "1":
    logado = cadastrar_usuario()

elif OPCAO == "2":
    logado = login_usuario()

if logado:
    while True: 
        print("\n--------------------MENU--------------------")
    
        print("[3] BUSCAR VÍDEO")
        print("[4] CURTIR VÍDEO")
        print("[5] DESCURTIR VÍDEO")
        print("[6] CRIAR LISTA DE FAVORITOS")
        print("[7] EXCLUIR LISTA DE FAVORITOS")
        print("[8] ADICIONAR VÍDEOS NA LISTA DE FAVORITOS")
        print("[9] REMOVER VÍDEOS DA LISTA DE FAVORITOS")
        print("[0] SAIR\n")

        OPCAO = input("Escolha uma opção: ")

        if OPCAO == "3":
            buscar_video()
        elif OPCAO == "4":
            curtir_video()
        elif OPCAO == "5":
            descurtir_video()
        elif OPCAO == "6":
            criar_lista()
        elif OPCAO == "7":
            excluir_lista()
        elif OPCAO == "8":
            adicionar_video_lista()
        elif OPCAO == "9":
            remover_video_lista()
        elif OPCAO == "0":
            print("Saindo do FEItv!")
            break
        

    
    

         
    
    
            
    
    
    
    

    

    
