from DSAndAlgorithms.DSModule.Queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == '__main__':
    print(hotPotato(["Bill", "Ram", "Sham", "Jodu", "Modhu", "Sheron", "Beron", "Prema"], 7))
