import logging
import os

import dotenv
from maestro_client import MaestroClient

dotenv.load_dotenv()

logger = logging.getLogger(__name__)


def task_is_running(*, size: int = 20) -> bool:
    """Verifica se há tarefas em execução no BotCity Maestro.

    Raises:
        RuntimeError: se a autenticação ou a listagem de tarefas falhar.
    """
    login = os.getenv("BOTCITY_LOGIN", "")
    key = os.getenv("BOTCITY_KEY", "")

    if not login or not key:
        raise RuntimeError(
            "Credenciais BOTCITY_LOGIN e/ou BOTCITY_KEY não configuradas no .env"
        )

    try:
        client = MaestroClient(
            login=login,
            key=key,
            base_url="https://developers.botcity.dev",
        )
        client.authenticate()
        response = client.tasks.list(size=size)
    except Exception as exc:
        raise RuntimeError(f"Falha ao consultar tarefas no BotCity: {exc}") from exc

    content = (response.data or {}).get("content")
    if content is None:
        raise RuntimeError(
            "Resposta inesperada da API do BotCity: campo 'content' ausente."
        )

    running = [task for task in content if task.get("state") == "RUNNING"]
    count = len(running)

    if count > 0:
        logger.info("Existem %d tarefa(s) em execução.", count)
        return True

    logger.info("Nenhuma tarefa em execução.")
    return False


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    result = task_is_running(size=200)
    print(f"{result=}")