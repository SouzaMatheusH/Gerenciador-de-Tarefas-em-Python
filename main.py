import json
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, descricao, prazo, prioridade):
        tarefa = {
            "descricao": descricao,
            "prazo": prazo,
            "prioridade": prioridade,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso!")

def main():
    lista = TodoList()
    while True:
        print("\n[1] Adicionar Tarefa")
        print("[2] Listar Tarefas Pendentes")
        print("[3] Listar Tarefas Concluídas")
        print("[4] Marcar Tarefa como Concluída")
        print("[5] Remover Tarefa")
        print("[6] Filtrar por Prioridade")
        print("[7] Salvar e Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            descricao = input("Descrição: ")
            prazo = input("Prazo (DD-MM-YYYY): ")
            prioridade = input("Prioridade (alta, média, baixa): ").lower()
            lista.adicionar_tarefa(descricao, prazo, prioridade)


if __name__ == "__main__":
    main()