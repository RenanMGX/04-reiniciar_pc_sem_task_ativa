from Entities.task_states import task_is_running
from time import sleep
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os


class Main:
    @staticmethod
    def exec(minutes=10):
        now = datetime.now()
        
        counter_running = 0
        while True:
            if datetime.now() > now + relativedelta(hours=3):
                return
            
            if task_is_running():
                counter_running = 0
                print("Tarefa em execução. Reiniciando contagem...")
            else:
                counter_running += 1
                print(f"Nenhuma tarefa em execução. Contagem: {counter_running} minuto(s).")
                if counter_running > minutes:
                    print("Reiniciando o PC...")
                    os.system("shutdown /r /t 0")
                    return
                else:
                    print(f"Aguardando {minutes - counter_running} minuto(s) para reiniciar o PC...")
            sleep(60)
            
            

if __name__ == "__main__":
    Main.exec()
