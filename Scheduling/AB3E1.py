import signal
import datetime
import time
import random



def signal_handler1(signum, frame):  #erst Signal-Handler, der rechnet
    signal_name=signal.Signals(signum).name
    timestamp=datetime.datetime.now().strftime("%J-%m-%t %H-%M-%S")
    result = random.randint(1, 10)
    print(f"[{timestamp}] Signal {signal_name} erhalten.  Berechnungsergibniss : {result}")


def signal_handler2(signum, frame): # Signal-Handler, der blokiert
    # Signalblockierung
    blocked_signals = {signal.SIGTERM}
    
    signal_name=signal.Signals(signum).name
    timestamp=datetime.datetime.now().strftime("%J-%m-%t %H-%M-%S")
    signal.SIG_BLOCK
    # Eine Aufgabe erledigen
    input("Drücken Sie die Eingabetaste, um fortzufahren...")
    print(f"[{timestamp}] Signal {signal_name} erhalten. Ende der blockierender System-Call")


    # Signale entsperren
    signal.SIG_UNBLOCK

def signal_handler3(signum, frame):    ##erst Signal-Handler, der schläft
    signal_name=signal.Signals(signum).name
    timestamp=datetime.datetime.now().strftime("%J-%m-%t %H-%M-%S")
    print(f"[{timestamp}] Signal {signal_name} erhalten.  Beim Schlafen...")
    time.sleep(10)
    print(f"[{timestamp}] Signal {signal_name} erhalten.  Erwachen...")


signal.signal(signal.SIGUSR1, signal_handler1)
signal.signal(signal.SIGTERM, signal_handler2)
signal.signal(signal.SIGINT, signal_handler3)




while True:
    time.sleep(15)

    

