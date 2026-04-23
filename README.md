# Reiniciar PC quando não houver tarefa em execução

Script simples em Python que reinicia o computador se nenhuma tarefa estiver em execução por um período contínuo configurável.

## Visão geral

O script monitora a função `task_is_running()` (em `Entities/task_states.py`) a cada minuto. Se não for detectada nenhuma tarefa em execução por N minutos consecutivos (padrão: 10), o script executa o comando de reinício do Windows:

```
shutdown /r /t 0
```

Use com cautela — o comando reinicia imediatamente sem salvar trabalho aberto.

## Pré-requisitos

- Python 3.8+ (testado com Python 3.x)
- Dependência: python-dateutil

Instalar dependências:

```bash
pip install python-dateutil
```

Instalação rápida (venv / requirements)

Recomenda-se criar um ambiente virtual e instalar as dependências a partir do `requirements.txt` gerado para este projeto:

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Windows (CMD):

```cmd
venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Arquivos relevantes

- `main.py` — script principal
- `Entities/task_states.py` — contém `task_is_running()` que deve retornar True quando houver tarefa ativa

## Uso

## Escopo das verificações

As tarefas verificadas pelo script são exclusivamente as tarefas do BotCity. A função `task_is_running()` presente em `Entities/task_states.py` deve implementar a lógica de checagem baseada nas execuções gerenciadas pelo BotCity. Se você usar outro orquestrador ou método de verificação, adapte essa função conforme necessário.


Executar o script manualmente:

```bash
python main.py
```

O tempo limite (minutos) pode ser alterado passando um argumento para `Main.exec()`. Exemplo para 30 minutos:

```python
from main import Main
Main.exec(minutes=30)
```

## Comportamento

- O script reinicia a contagem quando `task_is_running()` retorna True.
- Se não houver tarefa em execução por mais do que o valor de `minutes`, o script chama o comando de reinício e encerra.
- Após 3 horas de monitoramento sem atingir o tempo configurado, o script encerra automaticamente (proteção contra loops longos).

## Avisos de segurança

- O comando de reinício encerra a sessão do usuário imediatamente. Salve todos os trabalhos antes de executar.
- Tenha cuidado ao configurar execução automática — teste manualmente antes de agendar reinícios automáticos.

## Agendamento (opcional) — Agendador de Tarefas do Windows

1. Abra o Agendador de Tarefas do Windows.
2. Crie uma nova tarefa básica e aponte para o interpretador Python com o caminho do `main.py` como argumento, ou chame um script .bat que ative o venv e execute `python main.py`.
3. Configure para executar no logon ou em um agendamento recorrente, conforme desejado.

Exemplo de comando no campo "Programa/script":

```
C:\Path\to\python.exe r:\#Rotinas\04 - reiniciar_pc_sem_task_ativa - Renan\main.py
```

Nota: ajustar os caminhos conforme seu ambiente. Teste executando manualmente antes.

## Contribuição

Reportar problemas, enviar melhorias na função `task_is_running()` ou adicionar opções de configuração via argparse são bem-vindos.

## Últimas mudanças

- Adicionado `README.md` e `LICENSE` (MIT).
- Adicionada nota indicando que as tarefas verificadas são exclusivamente do BotCity.
- Adicionado `requirements.txt` com dependências do ambiente (ex.: `python-dateutil`).

## Licença

Este repositório está licenciado sob a licença MIT — veja o arquivo `LICENSE`.

## Contato

Renan Brian Hermenegildo Oliveira <renan.oliveira@patrimar.com.br>

