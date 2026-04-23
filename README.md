# Reiniciar PC quando não houver tarefa do BotCity em execução

Utilitário em Python que monitora tarefas gerenciadas pelo BotCity Maestro e reinicia o Windows quando não há nenhuma execução ativa por um período contínuo configurável.

## Índice

- [Visão geral](#visão-geral)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Parâmetros](#parâmetros)
- [Comportamento](#comportamento)
- [Logs](#logs)
- [Segurança](#segurança)
- [Agendamento (opcional)](#agendamento-opcional)
- [Licença](#licença)

---

## Visão geral

O script principal é `main.py`. A cada minuto ele chama `task_is_running()` (em `Entities/task_states.py`) e verifica se há tarefas com estado `RUNNING` no BotCity Maestro. Se nenhuma tarefa estiver ativa por N minutos consecutivos (padrão: 10), executa:

```
shutdown /r /t 0
```

---

## Requisitos

- Python 3.8+
- Arquivo `.env` na raiz do projeto com as variáveis:
  ```
  BOTCITY_LOGIN=<seu_login>
  BOTCITY_KEY=<sua_chave>
  ```

---

## Instalação

1. Crie e ative um ambiente virtual:

   **PowerShell:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   **CMD:**
   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie o arquivo `.env` na raiz do projeto com suas credenciais do BotCity:
   ```
   BOTCITY_LOGIN=seu_login
   BOTCITY_KEY=sua_chave_de_acesso
   ```

---

## Uso

**Linha de comando:**
```bash
python main.py
python main.py --minutes 30
```

**Programático:**
```python
from main import Main
Main.exec(minutes=30)
```

> Ao usar programaticamente, configure o logging antes de chamar `Main.exec()`:
> ```python
> import logging
> logging.basicConfig(level=logging.INFO)
> ```

---

## Parâmetros

| Parâmetro   | Tipo | Padrão | Descrição                                            |
|-------------|------|--------|------------------------------------------------------|
| `--minutes` | int  | `10`   | Minutos de inatividade contínua antes de reiniciar. |

---

## Comportamento

1. A cada minuto, consulta a API do BotCity Maestro.
2. Se `task_is_running()` retornar `True`, o contador é zerado.
3. Se o contador atingir `--minutes` sem tarefas ativas, o script executa o reinício.
4. Se a API falhar (rede, credenciais inválidas, resposta inesperada), o erro é registrado em log e o script encerra com código `1` — **o PC não é reiniciado**.
5. Após 3 horas de execução sem reiniciar, o script encerra automaticamente (proteção contra loops longos).

---

## Logs

Os logs são gravados em `logs/app.log` (criado automaticamente) e exibidos no console, com timestamp e nível de severidade.

A pasta `logs/` está no `.gitignore` e não é rastreada pelo Git.

---

## Segurança

- O comando de reinício encerra a sessão imediatamente — salve trabalhos em aberto antes de executar.
- Nunca comite o arquivo `.env` no repositório. Ele já está coberto pelo `.gitignore`.
- Teste o script manualmente antes de agendar execuções automáticas.

---

## Agendamento (opcional)

Use o Agendador de Tarefas do Windows para executar o script no logon ou em horários específicos. Crie um arquivo `.bat` que ative o venv e execute o script:

```bat
@echo off
call "%~dp0venv\Scripts\activate.bat"
python "%~dp0main.py" --minutes 10
```

---

## Licença

MIT — veja o arquivo `LICENSE`.
