import os
import dotenv; dotenv.load_dotenv()
from maestro_client import MaestroClient

def task_is_running(*, size=20, _print=False):
    client = MaestroClient(
        login=os.getenv("BOTCITY_LOGIN", ""),
        key=os.getenv("BOTCITY_KEY", ""),
        base_url="https://developers.botcity.dev"
    )

    client.authenticate()

    x = client.tasks.list(size=size).data['content']
    print(len(x)) if _print else None
    task_running = 0
    for i in x:
        if i['state'] == 'RUNNING':
            task_running += 1
        #print(i['activityName'], " - ", i['state'])
    #display(x)
    if task_running > 0:
        print(f"Existem {task_running} tarefas em execução.") if _print else None
        return True
    else:
        print("Não existem tarefas em execução.") if _print else None
        return False
    
if __name__ == "__main__":
    print(f"{task_is_running(size=200, _print=True)=}")