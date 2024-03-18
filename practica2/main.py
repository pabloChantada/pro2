import sys
from classes import Process, ManagerQueue
from materiales.array_queue import ArrayQueue

def parse_file(lines):
    # Con el espacio no va muy bien, pero con el punto y coma si
    lines = [x.replace(" ",";") for x in lines]
    lines = [x.strip("") for x in lines]
    for i in range(len(lines)):
        lines[i] = lines[i].split(";")

    record_queue = ArrayQueue()
    for i in range(len(lines)):
        record_queue.record_queue.enqueue(Process(lines[i][0], lines[i][1], lines[i][2], lines[i][3], lines[i][4]))
        
    return record_queue
            
    
def main():
    # Penalizaciones a usuarios con tiempo de ejecucion alto y digan que es bajo
    # Se aplica en el siguiente proceso del usuario que llegue a cualquiera de las 
    # colas de ejecucion
    
    # Una unica cola de registros; se añaden todos los registros en orden de llegada y se
    # procesan en orden de llegada a las colas correspondientes
    with open(sys.argv[1]) as f:
        lines = f.readlines()
        record_queue = parse_file(lines)
        manager = ManagerQueue()
        
        time = 0
        # Añadir mas condicones
        while not(record_queue.is_empty()):
            # Si tiene al menos un proceso en la cola se añade a la cola correspondientek
            time += 1
            print(f"Time: {time}")
            # Si la cola de registros no esta vacia se añaden a las colas correspondientes
            if not(record_queue.is_empty()):
                actual_process = record_queue.dequeue()
                actual_process._join_time = time
                manager.manage_queue(actual_process)
            manager.execute_process(record_queue, time)                
            

'''
for i in range(len(manager.cpu_short)):
    manager.cpu_short.dequeue().print()
print(" ")
for i in range(len(manager.cpu_long)):
    manager.cpu_long.dequeue().print()
print(" ")
for i in range(len(manager.gpu_short)):
    manager.gpu_short.dequeue().print()
print(" ")
for i in range(len(manager.gpu_long)):
    manager.gpu_long.dequeue().print()
print(" ")
print(manager.print_all())
'''    
if __name__ == "__main__":
    main()