import argparse
import logging
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
from time import sleep

from Entities.task_states import task_is_running

LOGS_DIR = Path(__file__).parent / "logs"


def _configure_logging() -> None:
    LOGS_DIR.mkdir(exist_ok=True)
    log_file = LOGS_DIR / "app.log"

    formatter = logging.Formatter(
        fmt="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)

    logging.basicConfig(level=logging.INFO, handlers=[file_handler, stream_handler])


logger = logging.getLogger(__name__)

MAX_RUNTIME = timedelta(hours=3)


class Main:
    @staticmethod
    def exec(minutes: int = 10) -> None:
        start_time = datetime.now()
        deadline = start_time + MAX_RUNTIME
        counter_running = 0

        logger.info(
            "Monitoramento iniciado. Reinicia após %d minuto(s) inativo(s). "
            "Encerra automaticamente em %s.",
            minutes,
            deadline.strftime("%H:%M:%S"),
        )

        while True:
            if datetime.now() >= deadline:
                logger.warning(
                    "Tempo máximo de monitoramento (%s) atingido. Encerrando sem reiniciar.",
                    MAX_RUNTIME,
                )
                return

            try:
                running = task_is_running()
            except RuntimeError as exc:
                logger.error("Erro ao verificar tarefas: %s", exc)
                logger.error("Encerrando o script.")
                sys.exit(1)

            if running:
                counter_running = 0
                logger.info("Tarefa em execução. Reiniciando contagem.")
            else:
                counter_running += 1
                remaining = minutes - counter_running
                logger.info(
                    "Nenhuma tarefa ativa. Contagem: %d/%d minuto(s).",
                    counter_running,
                    minutes,
                )

                if counter_running >= minutes:
                    logger.warning("Limite atingido. Reiniciando o PC...")
                    subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
                    return

                logger.info(
                    "Aguardando %d minuto(s) para reiniciar.",
                    remaining,
                )

            sleep(60)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Reinicia o PC quando não há tarefas BotCity ativas por N minutos."
    )
    parser.add_argument(
        "--minutes",
        type=int,
        default=10,
        metavar="N",
        help="Minutos de inatividade contínua antes de reiniciar (padrão: 10).",
    )
    return parser.parse_args()


if __name__ == "__main__":
    _configure_logging()
    args = _parse_args()
    Main.exec(minutes=args.minutes)

