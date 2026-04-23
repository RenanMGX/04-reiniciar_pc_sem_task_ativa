# Reiniciar PC quando não houver tarefa do BotCity em execução

Descrição
---
Utilitário em Python que monitora tarefas gerenciadas pelo BotCity e reinicia o Windows quando não há nenhuma execução ativa por um período contínuo configurável.

Índice
---

- [Visão geral](#visão-geral)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Parâmetros](#parâmetros)
- [Comportamento esperado](#comportamento-esperado)
- [Escopo das verificações](#escopo-das-verificações)
- [Segurança](#segurança)
- [Agendamento (opcional)](#agendamento-opcional)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão geral

O script principal é `main.py`. A cada minuto ele chama `task_is_running()` (implementada em `Entities/task_states.py`) e, se não houver tarefas ativas por N minutos consecutivos (padrão: 10), executa:

```
shutdown /r /t 0
```

## Requisitos

- Python 3.8+
- Dependências listadas em `requirements.txt` (ex.: `python-dateutil`).

> Observação: instale as dependências pelo `requirements.txt`; não é necessário instalar pacotes individualmente.

## Instalação

1. Crie e ative um ambiente virtual.

PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

CMD:

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

2. Instale dependências:

```bash
pip install -r requirements.txt
```

## Uso

Executar diretamente:

```bash
python main.py
```

Executar programaticamente:

```python
from main import Main
Main.exec(minutes=30)
```

## Parâmetros

- `minutes` (int): minutos de inatividade contínua antes de reiniciar (padrão: 10).

## Comportamento esperado

- Quando `task_is_running()` retorna True, o contador é zerado.
- Se o contador atingir `minutes` sem novas execuções, o script chama o comando de reinício e encerra.
- O script encerra automaticamente após 3 horas de execução sem reiniciar (proteção contra loops longos).

## Escopo das verificações

As verificações são exclusivamente para tarefas do BotCity. Se você usa outro orquestrador, adapte `Entities/task_states.py` para implementar a lógica de verificação adequada.

## Segurança

- O comando de reinício encerra a sessão do usuário imediatamente — salve seu trabalho antes de executar.
- Teste o script manualmente antes de agendar reinícios automáticos.

## Agendamento (opcional)

Use o Agendador de Tarefas do Windows para executar o script no logon ou em horários específicos. Recomenda-se utilizar um arquivo .bat que ative o venv e execute `python main.py`.

Exemplo (conteúdo do arquivo `run_script.bat`):

```bat
@echo off
call venv\Scripts\activate.bat
python %~dp0main.py
```

## Contribuição

Pull requests e issues são bem-vindos. Contribuições recomendadas:

- Melhorar a detecção em `Entities/task_states.py`.
- Adicionar argumentos via `argparse` para configurar `minutes` pela linha de comando.

## Licença

MIT — veja o arquivo `LICENSE`.

## Alterações recentes

- README reescrito para eliminar redundâncias; instalação centralizada via `requirements.txt`.
- `LICENSE` (MIT) e `requirements.txt` adicionados.
Script em Python para reiniciar o Windows quando não houver tarefas do BotCity em execução por um período contínuo configurável.

## Visão geral
O script verifica a função `task_is_running()` (em `Entities/task_states.py`) a cada minuto; se nenhuma tarefa for detectada por N minutos consecutivos (padrão: 10), ele executa:

```
shutdown /r /t 0

## Escopo
As verificações consideram exclusivamente tarefas gerenciadas pelo BotCity. A função `task_is_running()` deve ser adaptada se você usar outro orquestrador.

## Requisitos e instalação
- Python 3.8+
- Instale dependências usando o `requirements.txt` do projeto:

```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
Ou, em CMD:

```cmd
venv\Scripts\activate.bat
pip install -r requirements.txt
```
Se preferir instalar a dependência mínima diretamente:

```bash
pip install python-dateutil

## Uso
Executar manualmente:

```bash
python main.py

Uso programático (exemplo):
```python
from main import Main
Main.exec(minutes=30)

## Comportamento
- Reinicia a contagem assim que `task_is_running()` retorna True.
- Reinicia o PC quando o período configurado (minutos) for atingido sem tarefas ativas.
- Encerra após 3 horas de monitoramento sem atingir o tempo configurado (proteção).

## Segurança
O comando de reinício não salva trabalho aberto. Teste o script manualmente antes de agendar execuções automáticas.

## Agendamento (opcional)
Use o Agendador de Tarefas do Windows para executar o script no logon ou em horários específicos. Aponte para o `python.exe` e passe o caminho para `main.py` como argumento.

## Contribuição
Melhorias na função `task_is_running()`, correções e sugestões são bem-vindas.

## Alterações recentes
- README e LICENSE adicionados; README consolidado para remover redundâncias.
- `requirements.txt` incluído com dependências do ambiente.

## Licença
MIT — veja o arquivo `LICENSE`.

## Contato
Renan Brian Hermenegildo Oliveira <renan.oliveira@patrimar.com.br>
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

