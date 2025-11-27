import tkinter
import random





print(" - - - QUIZ INTERATIVO - - - ")


def sortear_jogador(jogador1,jogador2):
    jogadores = [jogador1,jogador2]
    input("Informe o NOME do jogador 1: ",jogador1)
    input("Informe o NOME do jogador 2:", jogador2)
    jogador_sorteado = random.choice(jogadores)

    print(f"O jogador sorteado para iniciar o jogo é: {jogador_sorteado}")

def sortear_pergunta():
    perguntas = [
    {
        "pergunta": "Qual é o maior planeta do Sistema Solar?",
        "opcoes": ["A) Terra", "B) Marte", "C) Júpiter"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual país é considerado o mais populoso do mundo atualmente?",
        "opcoes": ["A) Índia", "B) China", "C) Indonésia"],
        "resposta": "A"
    },
    {
        "pergunta": "Em qual oceano fica a Fossa das Marianas, o ponto mais profundo conhecido?",
        "opcoes": ["A) Atlântico", "B) Pacífico", "C) Índico"],
        "resposta": "B"
    },
    {
        "pergunta": "Quantos elementos químicos a Tabela Periódica possui oficialmente?",
        "opcoes": ["A) 103", "B) 112", "C) 118"],
        "resposta": "C"
    },
    {
        "pergunta": "Quem foi o autor da teoria da relatividade geral?",
        "opcoes": ["A) Isaac Newton", "B) Nikola Tesla", "C) Albert Einstein"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual é a capital oficial da Austrália?",
        "opcoes": ["A) Sydney", "B) Melbourne", "D) Camberra"],
        "resposta": "D"
    },
    {
        "pergunta": "Em que ano ocorreu a queda do Muro de Berlim?",
        "opcoes": ["A) 1975", "B) 1989", "C) 1995"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual é o maior deserto quente do mundo?",
        "opcoes": ["A) Gobi", "B) Saara", "D) Kalahari"],
        "resposta": "B"
    },
    {
        "pergunta": "Em qual país se originou o Renascimento?",
        "opcoes": ["A) França", "B) Inglaterra", "C) Itália"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual desses animais é considerado o maior animal que já existiu na Terra?",
        "opcoes": ["A) Tiranossauro rex", "B) Baleia-azul", "D) Megalodon"],
        "resposta": "B"
    }
]

numero_rodadas = input("Digite o número de rodadas:")

perguntas_sorteadas = random.sample(perguntas,numero_rodadas)
for p in perguntas_sorteadas:
    print(p["pergunta"])

    for opcao in p["opcoes"]:
        print(opcao)


    resposta_usuario = input("Digite a alternativa correta").upper()

    if resposta_usuario == p["resposta"]:
        print("Resposta correta!")


    else:
         print(f"✘ Resposta errada! A correta era: {p['resposta']}\n")