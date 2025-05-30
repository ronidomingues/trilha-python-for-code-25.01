import os

def clear_screen() -> None:
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')

def map_pcs() -> None:
    registraded_pcs = ()
    while True:
        new_pc = input("Deseja cadastrar um novo computador (ou digite 'exit' para sair): ")
        if new_pc.lower() == "exit":
            break
        else:
            clear_screen()
            new_register = (len(registraded_pcs) + 1,)
            pc_health = input("Seu computador está funcionando bem? (sim/não): ")
            if pc_health.lower() == "sim":
                new_register = new_register + (True,)
                registraded_pcs += (new_register,)
                continue
            else:
                new_register += (False,)
                pc_parts = ()
                part = input("Digite o nome das peças que precisam ser substituída separadas por vírgula: ")
                pc_parts = (part,)
                new_register += (pc_parts,)
            registraded_pcs += (new_register,)

    clear_screen()
    print("PCs registrados:", registraded_pcs)
if __name__ == "__main__":
    clear_screen()
    map_pcs()