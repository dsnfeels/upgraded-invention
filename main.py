import json
import os

ARQUIVO = "tarefas.json"

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=2)

def listar():
    tarefas = carregar_tarefas()
    for i, t in enumerate(tarefas):
        print(f"{i}: {t}")

def criar():
    tarefa = input("Digite a nova tarefa: ")
    tarefas = carregar_tarefas()
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionadaaa!")

def atualizar():
    listar()
    i = int(input("Qual tarefa deseja atualizar (número)? "))
    nova = input("Digite a nova descrição: ")
    tarefas = carregar_tarefas()
    tarefas[i] = nova
    salvar_tarefas(tarefas)
    print("Tarefa atualizada!")

def deletar():
    listar()
    i = int(input("Qual tarefa deseja deletar (número)? "))
    tarefas = carregar_tarefas()
    tarefas.pop(i)
    salvar_tarefas(tarefas)
    print("Tarefa deletada!")

def menu():
    while True:
        print("\n1. Listar\n2. Criar\n3. Atualizar\n4. Deletar\n5. Sair")
        op = input("Escolha uma opção: ")
        if op == "1":
            listar()
        elif op == "2":
            criar()
        elif op == "3":
            atualizar()
        elif op == "4":
            deletar()
        elif op == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
