import json
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tarefas = []
        self.carregar_tarefas()

    def adicionar_tarefa(self, descricao, prazo, prioridade):
        tarefa = {
            "descricao": descricao,
            "prazo": prazo,
            "prioridade": prioridade,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        print(f"Tarefa '{descricao}' adicionada com sucesso!")

    def listar_pendentes(self):
        print("\nTarefas Pendentes:")
        for tarefa in self.tarefas:
            if not tarefa["concluida"]:
                self.exibir_tarefa(tarefa)

    def listar_concluidas(self):
        print("\nTarefas Concluídas:")
        for tarefa in self.tarefas:
            if tarefa["concluida"]:
                self.exibir_tarefa(tarefa)

    def marcar_concluida(self, descricao):
        for tarefa in self.tarefas:
            if tarefa["descricao"] == descricao:
                tarefa["concluida"] = True
                print(f"Tarefa '{descricao}' marcada como concluída.")
                return
        print(f"Tarefa '{descricao}' não encontrada.")

    def remover_tarefa(self, descricao):
        self.tarefas = [t for t in self.tarefas if t["descricao"] != descricao]
        print(f"Tarefa '{descricao}' removida.")

    def filtrar_por_prioridade(self, prioridade):
        print(f"\nTarefas com Prioridade {prioridade.capitalize()}:")
        for tarefa in self.tarefas:
            if tarefa["prioridade"] == prioridade:
                self.exibir_tarefa(tarefa)

    def exibir_tarefa(self, tarefa):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"- {tarefa['descricao']} | Prazo: {tarefa['prazo']} | Prioridade: {tarefa['prioridade']} | Status: {status}")

    def salvar_tarefas(self):
        with open("tarefas.json", "w") as arquivo:
            json.dump(self.tarefas, arquivo, indent=4)
        print("Tarefas salvas no arquivo 'tarefas.json'.")

    def carregar_tarefas(self):
        try:
            with open("tarefas.json", "r") as arquivo:
                self.tarefas = json.load(arquivo)
            print("Tarefas carregadas com sucesso.")
        except FileNotFoundError:
            print("Nenhum arquivo de tarefas encontrado. Iniciando com lista vazia.")

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
        elif opcao == "2":
            lista.listar_pendentes()
        elif opcao == "3":
            lista.listar_concluidas()
        elif opcao == "4":
            descricao = input("Descrição da tarefa a concluir: ")
            lista.marcar_concluida(descricao)
        elif opcao == "5":
            descricao = input("Descrição da tarefa a remover: ")
            lista.remover_tarefa(descricao)
        elif opcao == "6":
            prioridade = input("Filtrar por prioridade (alta, média, baixa): ").lower()
            lista.filtrar_por_prioridade(prioridade)
        elif opcao == "7":
            lista.salvar_tarefas()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()