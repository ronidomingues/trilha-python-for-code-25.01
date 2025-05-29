def passwd_is_strong() -> bool:
  passwd = input("Digite a sua senha: ").split()
  if len(passwd) < 4 or len(passwd) > 16:
    print('Sua senha precisa ter entre 4 e 16 caracteres.')
    return False
  else:
    pass
  

def senha_forte() -> str:
  senha = input("Digite sua senha: ").split()
  numeros=["1", "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0"]
  print(senha)
  if 4 > len(senha):
    return "Sua senha precisa ter no mínimo 4 caracteres. "
  else:
    for c in senha:
      if c.isalnum():
        if c.isupper():
            index = 0
            while index <= 10:
              if numeros [index] in senha:
                return "Senha atende a todos os requisitos de segurança, senha *forte*. "
              else:
                return "Sua senha *não* atende a todos os requisitos de segurança, necessario incluir *numeros*. "
            index =  index + 1
        else:
          return "Sua senha precisa de letras *maiúsculas*, *números* e letras *minúsculas*. "
      else:
        return "Sua senha precisa de letras e/ou números. "

resultado = senha_forte(exemplo)
print(resultado)

if __name__ == "__main__":
  passwd_is_strong()