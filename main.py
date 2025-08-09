# Sistema de marcação de consultas simples em Python

# Lista para armazenar as consultas
consultas = []

def mostrar_menu():
    print("\n--- Sistema de Marcação de Consultas ---")
    print("1. Agendar consulta")
    print("2. Visualizar consultas")
    print("3. Cancelar consulta")
    print("4. Sair")

def agendar_consulta():
    nome = input("Digite o nome do paciente: ")
    data = input("Digite a data da consulta (dd/mm/aaaa): ")
    hora = input("Digite o horário da consulta (hh:mm): ")
    consulta = {'nome': nome, 'data': data, 'hora': hora}
    consultas.append(consulta)
    print("Consulta agendada com sucesso!")

def visualizar_consultas():
    if not consultas:
        print("Nenhuma consulta agendada.")
    else:
        print("\nConsultas agendadas:")
        for idx, c in enumerate(consultas, start=1):
            print(f"{idx}. {c['nome']} - {c['data']} às {c['hora']}")

def cancelar_consulta():
    visualizar_consultas()
    if consultas:
        try:
            escolha = int(input("Digite o número da consulta que deseja cancelar: "))
            if 1 <= escolha <= len(consultas):
                removida = consultas.pop(escolha - 1)
                print(f"Consulta de {removida['nome']} cancelada com sucesso.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, digite um número válido.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            agendar_consulta()
        elif opcao == '2':
            visualizar_consultas()
        elif opcao == '3':
            cancelar_consulta()
        elif opcao == '4':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()