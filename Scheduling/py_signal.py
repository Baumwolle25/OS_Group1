import signal
import os
import sys

class Terminate(BaseException):
    pass

def sigterm_exception(signalNumber, stackframe):
    raise Terminate()

def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    raise SystemExit('Exiting')

    return


def run_main(main):
    import signal
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGINT, signal.SIG_IGN)  #Der Signal SIGINT wird ignoriert
    signal.signal(signal.SIGTERM, sigterm_exception)
    try:
        sys.exit(main(sys.argv[1:]) or 0)
    except Terminate:
        signal.signal(signal.SIGTERM, signal.SIG_DFL)  #Der Signal SIGTERM wird der Default-Verhalten
        os.kill(os.getpid(), signal.SIGTERM)


signal.pause() #Wart auf ein Signal
