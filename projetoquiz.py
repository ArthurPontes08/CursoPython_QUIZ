from tkinter import Tk
import random


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
            "opcoes": ["A) Sydney", "B) Melbourne", "C) Camberra"],
            "resposta": "C"
        },
        {
            "pergunta": "Em que ano ocorreu a queda do Muro de Berlim?",
            "opcoes": ["A) 1975", "B) 1989", "C) 1995"],
            "resposta": "B"
        },
        {
            "pergunta": "Qual é o maior deserto quente do mundo?",
            "opcoes": ["A) Gobi", "B) Saara", "C) Kalahari"],
            "resposta": "B"
        },
        {
            "pergunta": "Em qual país se originou o Renascimento?",
            "opcoes": ["A) França", "B) Inglaterra", "C) Itália"],
            "resposta": "C"
        },
        {
            "pergunta": "Qual desses animais é considerado o maior animal que já existiu na Terra?",
            "opcoes": ["A) Tiranossauro rex", "B) Baleia-azul", "C) Megalodon"],
            "resposta": "B"
        }
    ]

jogadores = []
jogador_sorteado = ""
perguntas_sorteadas = []
rodada_atual = 0
placar = {}


def iniciar_jogo():
    global jogadores,jogador_sorteado,perguntas_sorteadas,rodada_atual,placar

    jogador1 = entry_jogador1.get()
    jogador2 = entry_jogador2.get()
    if not jogador1 or not jogador2:
        messagebox.showwarning("Aviso, Informe o nome dos dois jogadores")
        return


    jogadores = [jogador1,jogador2]
    placar = {jogador1: 0,jogador2: 0}
    jogador_sorteado = random.choice(jogadores)

    try:
        numero_rodadas = int(entry_rodadas.get())
        if numero_rodadas <= 0 or numero_rodadas > len(perguntas):
            raise ValueError

    except ValueError:
        messagebox.showwarning("Aviso", f"Digite um número de rodadas entre 1 e {len(perguntas)}")
        return


    perguntas_sorteadas = random.sample(perguntas, numero_rodadas)
    rodada_atual = 0



def mostrar_pergunta():
    global rodada_atual


    if rodada_atual >= len(perguntas_sorteadas):
        fim_jogo()
        return

    p = perguntas_sorteadas[rodada_atual]
    





def verificar_resposta():
    for p in perguntas_sorteadas:
        print("\n" + p["pergunta"])

        for opcao in p["opcoes"]:
            print(opcao)

        resposta_usuario = input("Digite a alternativa correta: ").upper()

        if resposta_usuario == p["resposta"]:
            print("✔ Resposta correta!")
        else:
            print(f"✘ Resposta errada! A correta era: {p['resposta']}")



        



