# Projeto acadêmico: sistema de gerenciamento de UPA.
# Dependências
# Recursos para manipulação de datas, execução de comandos do sistema e visualização de dados.
from datetime import datetime, timedelta
import os
import matplotlib.pyplot as plt

# Configurações do painel

# Define o tema escuro para os gráficos do painel.
plt.style.use("dark_background")

# Limpa o terminal em sistemas Windows e Linux.
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Dados operacionais da unidade de pronto atendimento.

# Lista de pacientes aguardando atendimento.
waiting_list = []

# Salas disponíveis para atendimento.
rooms = {
    1: None,
    2: None,
    3: None
}

# Duração estimada de cada consulta, em minutos.
CONSULTATION_TIME = 30

# Indica se a saída do sistema foi confirmada.
exit_confirmed = False

# Dados demonstrativos utilizados pelo painel; não representam registros reais de pacientes.
hourly_data = {
    "horas": [
        "06h", "07h", "08h",
        "09h", "10h", "11h",
        "12h", "13h", "14h",
        "15h", "16h", "17h"
    ],
    "pacientes": [
        68, 15, 28, 35,
        42, 48, 51, 44,
        39, 37, 41, 53
    ],
    "espera_media": [
        12, 18, 25, 40,
        55, 60, 75, 58,
        45, 42, 50, 80
    ]
}

# Distribuição demonstrativa dos sintomas registrados.
symsymptoms_data = {
    "Febre": 84,
    "Gripe": 73,
    "Dor muscular": 41,
    "Pressão alta": 22,
    "Dor abdominal": 36
}

# Distribuição demonstrativa de pacientes por faixa etária.
age_data = {
    "0-12": 31,
    "13-17": 18,
    "18-30": 76,
    "31-45": 59,
    "46-60": 42,
    "60+": 37
}
# Indicadores operacionais demonstrativos.
flags = {
    "daily_patients": 313,
    "average_time": 27,
    "ocupation": 92,
    "priority_queue": 41,
    "ended_consults": 287
}

# Painel de indicadores
# Exibe os gráficos e os indicadores operacionais da unidade.
def abrir_dashboard():
    # Cria a janela principal do painel.
    program_window = plt.figure(
        figsize=(16, 9),
        facecolor="#202020FF"
    )
    # Define o título geral do painel.
    program_window.suptitle(
        "DASHBOARD UPA - GERENCIAMENTO HOSPITALAR",
        color="white",
        fontsize=22
    )
    
    # Gráfico 1: fluxo de pacientes por horário.
    # Define a área do primeiro gráfico.
    ax1 = program_window.add_subplot(2, 2, 1)
    # Define a cor de fundo da área do gráfico.
    ax1.set_facecolor("#1E1E1E")
    # Representa a evolução do volume de pacientes ao longo do dia.
    ax1.plot(
        hourly_data["horas"],
        hourly_data["pacientes"],
        color="#00E5FF",
        linewidth=4,
        marker="o",
        markersize=8,
        markerfacecolor="white"
    )
    # Define o título e os rótulos dos eixos.
    ax1.set_title(
        "Fluxo de Pacientes",
        color="white",
        fontsize=16
    )
    ax1.set_xlabel("Horário", color="white")
    ax1.set_ylabel("Pacientes", color="white")
    # Exibe uma grade discreta para facilitar a leitura dos valores.
    ax1.grid(alpha=0.2)
    # Oculta as bordas superior e direita para simplificar a visualização.
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    # Ajusta a cor dos rótulos para manter o contraste com o tema escuro.
    ax1.tick_params(colors="white")
    
    # Gráfico 2: tempo médio de espera por horário.
    ax2 = program_window.add_subplot(2, 2, 2)
    ax2.set_facecolor("#1E1E1E")
    # Representa o tempo médio de espera ao longo do dia.
    ax2.plot(
        hourly_data["horas"],
        hourly_data["espera_media"],
        color="#00FF9C",
        linewidth=4,
        marker="o",
        markersize=8,
        markerfacecolor="white"
    )
    ax2.set_title(
        "Tempo Médio de Espera",
        color="white",
        fontsize=16
    )
    ax2.set_xlabel("Horário", color="white")
    ax2.set_ylabel("Minutos", color="white")
    ax2.grid(alpha=0.2)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.tick_params(colors="white")

    # Gráfico 3: sintomas mais frequentes.
    ax3 = program_window.add_subplot(2, 2, 3)
    ax3.set_facecolor("#1E1E1E")
    # Compara a frequência dos sintomas por meio de barras.
    bar = ax3.bar( 
        symsymptoms_data.keys(),
        symsymptoms_data.values()
    )
    # Define uma cor distinta para cada barra.
    colors_list = [
        "#00E5FF",
        "#00FF9C",
        "#FFD93D",
        "#FF4C4C",
        "#9D4EDD"
    ]
    # Aplica as cores na ordem definida acima.
    for bar, color in zip(bar, colors_list):
        bar.set_color(color)
    ax3.set_title(
        "Sintomas Mais Comuns",
        color="white",
        fontsize=16
    )
    ax3.tick_params(colors="white")
    ax3.spines["top"].set_visible(False)
    ax3.spines["right"].set_visible(False)
    ax3.grid(alpha=0.2)
    
    # Área de indicadores-chave de desempenho.
    ax4 = program_window.add_subplot(2, 2, 4)
    # Oculta os eixos, pois esta área exibe somente texto.
    ax4.axis("off")
    ax4.set_facecolor("#1E1E1E")
    # Total de pacientes atendidos no dia.
    ax4.text(
        0.1,
        0.85,
        f"Pacientes Hoje: {flags['daily_patients']}",
        color="white",
        fontsize=18
    )
    # Tempo médio de espera.
    ax4.text(
        0.1,
        0.65,
        f"Tempo Médio: {flags['average_time']} min",
        color="#00FF9C",
        fontsize=18
    )
    # Taxa de ocupação das salas.
    ax4.text(
        0.1,
        0.45,
        f"Ocupação: {flags['ocupation']}%",
        color="#FFD93D",
        fontsize=18
    )
    # Quantidade de casos prioritários.
    ax4.text(
        0.1,
        0.25,
        f"Casos Prioritários: {flags['priority_queue']}",
        color="#FF4C4C",
        fontsize=18
    )
    # Quantidade de consultas concluídas.
    ax4.text(
        0.1,
        0.05,
        f"Consultas Finalizadas: {flags['ended_consults']}",
        color="#00E5FF",
        fontsize=18
    )
    # Ajusta o espaçamento para evitar sobreposição dos elementos.
    plt.tight_layout()
    # Exibe a janela do painel.
    plt.show()
    
# Execução principal do sistema.

# Mantém o sistema em execução até que a saída seja confirmada.
while True:
    clear_screen()
    # Registra o horário atual para atualizar o estado do atendimento.
    now = datetime.now()
    print("-" * 45)
    print("GERENCIADOR DE POSTO DE SAÚDE")
    print("-" * 45)

    # Exibe o estado atual das salas.
    print("STATUS DAS SALAS:")
    
    # Percorre as salas cadastradas.
    for room_number in rooms:
        room_data = rooms[room_number]
        
        # Informa quando a sala está disponível.
        if room_data == None:
            print(f"Sala {room_number}: 🟢 Livre")
        else:
            # Calcula o tempo restante da consulta.
            time_diff = room_data["exit_time"] - now
            total_seconds = time_diff.total_seconds()
            remaining_minutes = int(total_seconds / 60)

            # Limita o tempo restante a zero quando a consulta já terminou.
            if remaining_minutes < 0:
                remaining_minutes = 0

            # Informa o tempo restante enquanto o atendimento está em andamento.
            if remaining_minutes > 0:
                status = f"{remaining_minutes} min restantes"
            else:
                status = "⚠️ CONSULTA CONCLUÍDA"

            print(
                f"Sala {room_number}: 🔴 {room_data['patient_name']} ({status})"
            )

    print("-" * 45)

    # Apresenta as opções do menu principal.
    print(f"Fila de espera: {len(waiting_list)} pessoas")
    print("1 - Cadastrar Paciente")
    print("2 - Chamar para Sala Livre")
    print("3 - Ver Lista de Espera")
    print("4 - Liberar Sala Manualmente")

    # Solicita uma segunda confirmação antes de encerrar o sistema.
    if not exit_confirmed:
        print("5 - Atualizar Status / Sair")
    else:
        print("5 - ⚠️ CONFIRMAR SAÍDA? (Escolha outra opção para cancelar)")

    # Opção para abrir o painel de indicadores.
    print("6 - Dashboard")
    option = input("\nEscolha uma opção: ")

    # Cancela a solicitação de saída se outra opção for selecionada.
    if option != '5':
        exit_confirmed = False

    # Cadastra um paciente na fila de espera.
    if option == '1':
        name = input('Nome do paciente: ')
        priority = int(input("Prioridade (1-Pref / 0-Norm): "))
        arrival_time = now.strftime("%H:%M:%S")
        # Cria o registro do paciente com nome, prioridade e horário de chegada.
        new_patient = {
            "name": name,
            "priority": priority,
            "arrival": arrival_time
        }
        waiting_list.append(new_patient)
        print(f"✅ {name} adicionado.")
        input("Pressione Enter...")

    # Encaminha o próximo paciente para uma sala disponível.
    elif option == '2':
        free_room = None
        # Localiza a primeira sala disponível.
        for room_number in rooms:
            if rooms[room_number] == None:
                free_room = room_number
                break
        # Informa quando todas as salas estão ocupadas.
        if free_room == None:
            print("⚠️ Todas as salas ocupadas!")
            input("Pressione Enter...")
        # Informa quando não há pacientes aguardando atendimento.
        elif len(waiting_list) == 0:
            print("📭 Fila vazia!")
            input("Pressione Enter...")
        else:
            # Separa os pacientes prioritários.
            priority_queue = []
            # Separa os pacientes sem prioridade.
            normal_queue = []
            # Organiza a fila com os casos prioritários antes dos demais.
            for p in waiting_list:
                if p["priority"] == 1:
                    priority_queue.append(p)
                else:
                    normal_queue.append(p)
            # Mantém os pacientes prioritários no início da fila.
            waiting_list = priority_queue + normal_queue
            # Remove da fila o próximo paciente a ser atendido.
            next_patient = waiting_list.pop(0)
            # Estima o horário de término com base na duração configurada.
            exit_estimate = now + timedelta(minutes=CONSULTATION_TIME)
            # Registra o paciente e o horário previsto de término na sala.
            rooms[free_room] = {
                "patient_name": next_patient["name"],
                "exit_time": exit_estimate
            }
            print(f"📢 {next_patient['name']} para a Sala {free_room}!")
            input("Pressione Enter...")

    # Exibe os pacientes que aguardam atendimento.
    elif option == '3':
        clear_screen()
        print("📋 --- FILA DE ESPERA ATUAL ---")
        # Informa quando a fila está vazia.
        if len(waiting_list) == 0:
            print("Fila vazia.")
        else:
            # Lista os pacientes na ordem atual de atendimento.
            for i, p in enumerate(waiting_list, 1):
                tipo = "⭐ P" if p["priority"] == 1 else "N"
                print(
                    f"{i}. [{tipo}] {p['name']} - Chegada: {p['arrival']}"
                )
        print("-" * 30)
        input("\nPressione Enter para voltar...")
        
    # Libera manualmente uma sala.
    elif option == '4':
        target_room = int(input("Liberar qual sala? "))
        # Verifica se o número informado corresponde a uma sala cadastrada.
        if target_room in rooms:
            rooms[target_room] = None
            print(f"✅ Sala {target_room} liberada.")
        else:
            print("Sala inválida.")
        input("Pressione Enter...")

    # Atualiza o estado ou encerra o sistema após confirmação.
    elif option == '5':
        if not exit_confirmed:
            exit_confirmed = True
            # O estado será atualizado na próxima iteração do laço principal.
        else:
            print("Encerrando sistema... Até a próxima! 🏥")
            break
        
    # Abre o painel de indicadores.
    elif option == '6':
        # Exibe os gráficos e os indicadores operacionais.
        abrir_dashboard()

