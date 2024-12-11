def obter_opcao(mensagem, opcoes):
    print(mensagem)
    for chave, valor in opcoes.items():
        print(f"{chave} - {valor}")
    escolha = input("Digite o número correspondente: ")
    return opcoes.get(escolha, "Inválido")

def gerar_treino(biotipo, dias, tipo_exercicio):
    print("\nGerando seu plano de treino personalizado...\n")
    if biotipo == "Inválido" or dias == "Inválido" or tipo_exercicio == "Inválido":
        print("Informações inválidas fornecidas. Por favor, reinicie o programa e tente novamente.")
        return

    treinos = {
        "Full Body": ["Supino reto com barra", "Agachamento", "Flexão de braços"],
        "ABC": {
            "Dia A": ["Supino reto com barra", "Tríceps na polia", "Flexão de braços"],
            "Dia B": ["Puxada na frente", "Rosca direta", "Remada curvada"],
            "Dia C": ["Agachamento", "Elevação lateral", "Stiff"]
        },
        "ABCDE": {
            "Dia A": ["Supino reto com barra"],
            "Dia B": ["Tríceps na polia"],
            "Dia C": ["Puxada na frente"],
            "Dia D": ["Rosca direta"],
            "Dia E": ["Agachamento"]
        }
    }

    plano = treinos.get(dias, [])
    if isinstance(plano, dict):
        for dia, exercicios in plano.items():
            print(f"{dia}: {', '.join(exercicios)}")
    else:
        print(f"Treino sugerido: {', '.join(plano)}")

    salvar_treino_em_arquivo(biotipo, dias, tipo_exercicio, plano)

def salvar_treino_em_arquivo(biotipo, dias, tipo_exercicio, treino):
    with open("plano_de_treino.txt", "w") as arquivo:
        arquivo.write("Plano de Treino Personalizado\n")
        arquivo.write(f"Biotipo: {biotipo}\n")
        arquivo.write(f"Dias disponíveis para treino: {dias}\n")
        arquivo.write(f"Tipo de exercício preferido: {tipo_exercicio}\n\n")
        if isinstance(treino, dict):
            for dia, exercicios in treino.items():
                arquivo.write(f"{dia}: {', '.join(exercicios)}\n")
        else:
            arquivo.write(f"Treino sugerido: {', '.join(treino)}\n")
    print("\nSeu plano de treino foi salvo em 'plano_de_treino.txt'.")

def main():
    print("\n🏋️‍♂️ Assistente de Personal Trainer - Gerador de Treino Ideal 🏋️‍♂️")
    biotipos = {"1": "Ectomorfo", "2": "Mesomorfo", "3": "Endomorfo"}
    dias_disponiveis = {"1": "Full Body", "3": "ABC", "5": "ABCDE"}
    tipos_exercicio = {
        "1": "Funcional",
        "2": "Maquinário",
        "3": "Peso Livre",
        "4": "Cardio",
        "5": "HIIT"
    }

    biotipo = obter_opcao("\nEscolha seu biotipo corporal:", biotipos)
    dias = obter_opcao("\nQuantos dias por semana você tem disponível para treinar?", dias_disponiveis)
    tipo_exercicio = obter_opcao("\nEscolha o tipo de exercício preferido:", tipos_exercicio)

    gerar_treino(biotipo, dias, tipo_exercicio)

if __name__ == "__main__":
    main()
