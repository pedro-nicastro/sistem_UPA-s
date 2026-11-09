# Sistema de Gerenciamento de UPA

Projeto acadêmico desenvolvido para uma atividade da faculdade. O programa simula, de forma didática, algumas rotinas de atendimento de uma Unidade de Pronto Atendimento (UPA), como cadastro de pacientes, organização da fila e controle de salas.

## Objetivo

Demonstrar conceitos de programação em Python por meio de um sistema de console que organiza pacientes por prioridade e apresenta indicadores em um painel gráfico.

## Funcionalidades

- Cadastro de pacientes com indicação de prioridade.
- Organização da fila, com pacientes prioritários atendidos primeiro.
- Encaminhamento do próximo paciente para uma sala disponível.
- Consulta da fila de espera.
- Liberação manual de salas.
- Exibição de um painel com gráficos e indicadores demonstrativos.

## Tecnologias

- Python 3
- Matplotlib

## Como executar

1. Instale o Python 3.
2. Instale a dependência do painel gráfico:

   ```bash
   python -m pip install matplotlib
   ```

3. Execute o programa na pasta do projeto:

   ```bash
   python gerenciador_upa.py
   ```

## Observação

Este projeto tem finalidade exclusivamente acadêmica e demonstrativa. Os números apresentados no painel são dados fictícios e o programa não deve ser utilizado para atendimento real, armazenamento de informações de pacientes ou tomada de decisões clínicas.

