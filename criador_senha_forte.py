import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    print("Bem-vindo ao Gerador de Senhas com Palavra-Chave!")
    print("Vamos criar uma senha forte e fácil de lembrar para você.")
    print("---")
    palavra_chave = input("Digite a palavra-chave: ")
    try:
        tamanho_total = int(input("Digite o tamanho total da senha: "))
        tamanho_palavra = len(palavra_chave)
        if tamanho_total < tamanho_palavra:
            print("O tamanho total deve ser maior ou igual ao tamanho da palavra-chave.")
        else:
            tamanho_aleatorio = tamanho_total - tamanho_palavra
            parte_aleatoria = gerar_senha(tamanho_aleatorio)
            senha_quase_pronta = palavra_chave + parte_aleatoria
            lista_senha = list(senha_quase_pronta)
            random.shuffle(lista_senha)
            senha_final = ''.join(lista_senha)
            print(f"Sua senha forte é: {senha_final}")
    except ValueError:
        print("Por favor, insira um número válido para o tamanho da senha.")