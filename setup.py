import os

# Cores para o terminal
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

# Novo Banner
def exibir_banner():
    os.system("clear")
    print(f"""{GREEN}
╔══════════════════════════════════╗
║   {CYAN}CONFIGURADOR DO ZSH - TERMUX{GREEN}   ║
╠══════════════════════════════════╣
║   {YELLOW}Personalize seu terminal!{GREEN}      ║
╚══════════════════════════════════╝
{RESET}""")

# Lista de temas disponíveis
path = "/data/data/com.termux/files/home/.oh-my-zsh/themes"
themas = os.listdir(path)
themas_sem_extensao = [tema.replace(".zsh-theme", "") for tema in themas]

# Escolher um tema
def escolher_tema():
    exibir_banner()
    print(f"{GREEN}Escolha um tema para o Zsh:\n{RESET}")
    for i, tema in enumerate(themas_sem_extensao):
        print(f"{CYAN}{i + 1} - {tema}{RESET}")

    print(f"{CYAN}0 - Adicionar tema manualmente{RESET}")

    while True:
        try:
            escolha = int(input(f"{YELLOW}Digite o número correspondente ao tema desejado: {RESET}"))
            if 1 <= escolha <= len(themas_sem_extensao):
                return themas_sem_extensao[escolha - 1]
            elif escolha == 0:
                return input(f"{YELLOW}Digite o nome do tema manualmente: {RESET}")
            else:
                print(f"{RED}Número inválido. Tente novamente.{RESET}")
        except ValueError:
            print(f"{RED}Por favor, digite um número válido.{RESET}")

# Gerenciar plugins do Zsh
def gerenciar_plugins():
    exibir_banner()
    zshrc_path = os.path.expanduser("~/.zshrc")

    # Obtendo os plugins atuais
    plugins_atual = []
    if os.path.exists(zshrc_path):
        with open(zshrc_path, "r") as file:
            for linha in file:
                if linha.startswith("plugins="):
                    plugins_atual = linha.strip().replace("plugins=(", "").replace(")", "").split()
                    break

    print(f"{GREEN}Plugins atuais: {CYAN}{', '.join(plugins_atual) if plugins_atual else 'Nenhum'}{RESET}")
    
    print(f"{YELLOW}1 - Adicionar plugins{RESET}")
    print(f"{YELLOW}2 - Remover plugins{RESET}")
    print(f"{YELLOW}3 - Manter plugins atuais{RESET}")

    while True:
        escolha = input(f"{BLUE}Escolha uma opção: {RESET}")

        if escolha == "1":
            novos_plugins = input(f"{YELLOW}Digite os plugins para adicionar (separados por espaço): {RESET}").split()
            plugins_atual.extend(novos_plugins)
            break

        elif escolha == "2":
            if not plugins_atual:
                print(f"{RED}Não há plugins para remover!{RESET}")
                break

            print(f"{CYAN}Plugins disponíveis: {', '.join(plugins_atual)}{RESET}")
            remover = input(f"{YELLOW}Digite os plugins para remover (separados por espaço): {RESET}").split()
            plugins_atual = [p for p in plugins_atual if p not in remover]
            break

        elif escolha == "3":
            break

        else:
            print(f"{RED}Opção inválida! Tente novamente.{RESET}")

    return " ".join(plugins_atual)

# Aplicar mudanças no .zshrc
def modificar_zshrc(tema, plugins):
    zshrc_path = os.path.expanduser("~/.zshrc")

    # Lendo o arquivo atual
    with open(zshrc_path, "r") as file:
        linhas = file.readlines()

    # Modificando o ZSH_THEME e os plugins
    with open(zshrc_path, "w") as file:
        for linha in linhas:
            if linha.startswith("ZSH_THEME="):
                file.write(f'ZSH_THEME="{tema}"\n')
            elif linha.startswith("plugins="):
                file.write(f'plugins=({plugins})\n')
            else:
                file.write(linha)

    print(f"\n{GREEN}Tema e plugins atualizados com sucesso!{RESET}\n\n\n")
    os.system("exec zsh")

# Executando as funções
if __name__ == "__main__":
    exibir_banner()
    tema_escolhido = escolher_tema()
    plugins_escolhidos = gerenciar_plugins()
    modificar_zshrc(tema_escolhido, plugins_escolhidos)
