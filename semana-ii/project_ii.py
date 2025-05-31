import os

def clear_screen() -> None:
    """
    A função não recebe parâmetros e não retorna valores.
    Descrição:
    -----------
    Função para limpar a tela do terminal.
    Utiliza 'cls' para Windows e 'clear' para outros sistemas operacionais.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def get_pc_parts() -> tuple[str, ...]:
    """
    A função não recebe parâmentros e retorna uma tupla de strings.
    Descrição:
    -----------
    Função para obter os componentes de um computador que estão com defeito.
    Solicita ao usuário o número de componentes defeituosos (entre 1 e 15 componentes).
    Verifica se o número é válido e solicita os nomes dos componentes.
    Se o número for inválido, solicita novamente o número.
    Por fim, retorna uma tupla contendo os nomes dos componentes.
    """
    while True:
        num_parts = input("Quantos componentes estão com defeito? (1, 2, 3, ... 15): ")
        if num_parts.isdigit() and 1 <= int(num_parts) <= 15:
            break
        print("Número inválido. Por favor, insira um número válido.")
    pc_parts = ()
    for num in range(1, int(num_parts) + 1):
        while True:
            part = input(f"Digite o {num}º componente com defeito: ").strip().capitalize()
            if part:
                pc_parts += (part,)
                break
            print("Nome inválido. Por favor, insira um nome válido.")
    return pc_parts

def map_pcs() -> None:
    """
    A função não recebe parâmetros e não retorna valores.
    Descrição:
    -----------
    Função para cadastrar computadores e registrar seus estados.
    Solicita ao usuário se deseja cadastrar um computador e, caso sim, se ele está funcionando bem.
    Se não estiver, solicita os componentes defeituosos.
    Exibe uma tupla dos computadores cadastrados e uma tupla com os IDs dos computadores que funcionam bem.
    """
    try:
        registered_pcs = ()
        healthy_pcs = ()
        while True:
            new_pc = input("Deseja cadastrar um computador? (y/n): " if len(registered_pcs) == 0 else "Deseja cadastrar outro computador? (y/n): ")
            if new_pc.lower() == "n":
                break
            elif new_pc.lower() == "y":
                clear_screen()
                pc_id = 100 + (len(registered_pcs)+1)
                while True:
                    pc_health = input("Esse computador está funcionando bem? (y/n): ")
                    if pc_health.lower() == "y":
                        registered_pcs += ((pc_id, True, ()),)
                        healthy_pcs += (pc_id,)
                        clear_screen()
                        break
                    elif pc_health.lower() == "n":
                        clear_screen()
                        registered_pcs += ((pc_id, False, get_pc_parts()),)
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
                        continue
            else:
                print("Opção inválida. Tente novamente.")
                continue
        clear_screen()
        print("----------------------------------------------")
        print("Cadastro de computadores concluído.")
        print("----------------------------------------------")
        print("Computadores cadastrados:\n", registered_pcs)
        print("Computadores funcionando bem:\n", healthy_pcs)
        print("----------------------------------------------")
    except KeyboardInterrupt:
        clear_screen()
        print("\nOperação cancelada pelo usuário.")
        return

if __name__ == "__main__":
    clear_screen()
    map_pcs()