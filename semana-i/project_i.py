import os
import getpass

def passwd_consecutives(passwd: str) -> bool:
  """
  Função para verificar se a senha contém três dígitos consecutivos.
  Essa função recebe uma string como parâmetro e retorna um valor booleano.
  Se a senha contiver três dígitos consecutivos (como '123' ou '987'), a função retorna True.
  Caso contrário, retorna False.
  """
  for index in range(len(passwd) - 2):
    three_chars = passwd[index:index + 3]
    if three_chars.isdigit():
      digit_1, digit_2, digit_3 = int(three_chars[0]), int(three_chars[1]), int(three_chars[2])
      if (digit_2 == digit_1 + 1 and digit_3 == digit_2 + 1) or (digit_2 == digit_1 - 1 and digit_3 == digit_2 - 1):
        return True
  return False

def secure_passwd() -> None:
  """
  Função para solicitar uma senha forte ao usuário.
  Essa função não possui entrada de parâmetros e não retorna nenhum valor.
  Ela exibe as regras para uma boa senha e solicita que o usuário insira uma senha que atenda a esses critérios.
  Se a senha não atender aos critérios, a função solicitará que o usuário insira uma nova senha até que uma senha válida seja fornecida.
  """
  print("Regras para uma boa senha:".center(50, "-"))
  print("Sua senha deve atender às seguintes regras:")
  print("--------------------------------------------------")
  print("1. Deve ter entre 8 e 16 caracteres.")
  print("2. Não pode conter espaços no início ou no final.")
  print("3. Deve conter pelo menos um número.")
  print("4. Deve conter pelo menos duas letras (uma maiúscula e uma minúscula).")
  print("5. Deve conter pelo menos um caractere especial.")
  print("6. Não pode conter três dígitos consecutivos (como '123' ou '987').")
  print("--------------------------------------------------")
  get_passwd = getpass.getpass("Por favor, digite uma senha forte: ")
  if get_passwd != get_passwd.strip():
    os.system("cls" if os.name == "nt" else "clear")
    print("\033[31mSua senha não pode conter espaços no início ou no final. Por favor, digite novamente.\n\n\033[0m")
    secure_passwd()
  elif len(get_passwd) < 8 or len(get_passwd) > 16:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"\033[31mSua senha possui {len(get_passwd)} cractreses, mas ela precisa ter entre 8 e 16 caracteres. Por favor, digite novamente.\033[0m")
    secure_passwd()
  else:
    if not any(char.isdigit() for char in get_passwd):
      os.system("cls" if os.name == "nt" else "clear")
      print("\033[31mSua senha precisa conter pelo menos um número. Por favor, digite novamente.\033[0m")
      secure_passwd()
    elif not any(char.isalpha() for char in get_passwd):
      os.system("cls" if os.name == "nt" else "clear")
      print("\033[31mSua senha precisa conter pelo menos duas letras, uma maiúscula e uma minúscula. Por favor, digite novamente.\033[0m")
      secure_passwd()
    elif not any(char in "!@#$%^&*()-_+=<>?{}[]|:;'" for char in get_passwd):
      os.system("cls" if os.name == "nt" else "clear")
      print("\033[31mSua senha precisa conter pelo menos um caractere especial. Por favor, digite novamente.\033[0m")
      secure_passwd()
    elif not any(char.islower() for char in get_passwd):
      os.system("cls" if os.name == "nt" else "clear")
      print("\033[31mSua senha precisa conter pelo menos uma letra minúscula. Por favor, digite novamente.\033[0m")
      secure_passwd()
    elif not any(char.isupper() for char in get_passwd):
      os.system("cls" if os.name == "nt" else "clear")
      print("\033[31mSua senha precisa conter pelo menos uma letra maiúscula. Por favor, digite novamente.\033[0m")
      secure_passwd()
    elif passwd_consecutives(get_passwd):
      os.system("cls" if os.name == "nt" else "clear")
      print("\033[31mSua senha não pode conter três dígitos consecutivos (como '123' ou '987'). Por favor, digite novamente.\033[0m")
      secure_passwd()
    else:
      print("\n\n--------------------------------------------------")
      print("Parabéns! Sua senha atende a todos os critérios.")
      print(f"A senha digitada foi: {get_passwd}")
      print("--------------------------------------------------")

if __name__ == "__main__":
  os.system("cls" if os.name == "nt" else "clear")
  secure_passwd()