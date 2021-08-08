import pdb
import ptrace.debugger
import signal
import subprocess
import sys

# What we are doing here: Get the instruction pointer -> execute a single step -> get the new instruction pointer.


def debugger_(pid):

    debugger = ptrace.debugger.PtraceDebugger()

    print("Attach the running process %s" % pid)

    process = debugger.addProcess(pid, False)

    print("IP before: %#x" % process.getInstrPointer())

    print("Execute a single step")

    process.singleStep()

    #  singleStep() hands back control to the child (target) process
    #  so we wait for it to give up control again with waitSignals.

    process.waitSignals(signal.SIGTRAP)

    print("IP after: %#x" % process.getInstrPointer())

    process.cont()

    process.detach()

    debugger.quit()


def main():

    child_process = subprocess.Popen("/home/ira/Downloads/Projects/SS Project/child.py",
                                    shell=True,
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
    try:
        debugger_(child_process.pid)
    except:
        print("-----------------------------------")
    child_process.kill()
    child_process.wait()


if __name__ == "__main__":
    main()
