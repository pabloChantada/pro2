'''
Pablo Chantada Saborido | pablo.chantada@udc.es
Pablo Verdes Sánchez | p.verdess@udc.es
'''

from array_queue import ArrayQueue

class Process():
    def __init__(self, id_process: str, id_user: str, resource_type: str, time_to_process: str, exec_time: int):
        '''
        Crea una instancia de la clase Process.

        Arguments
        ----------
            id_process (str): El ID del proceso.
            id_user (str): El ID del usuario asociado al proceso.
            resource_type (str): El tipo de recurso asociado al proceso.
            time_to_process (str): El tiempo necesario para procesar el recurso.
            exec_time (int): El tiempo de ejecución del proceso.

        Attributes
        ----------
            _id_process (str): El ID del proceso.
            _id_user (str): El ID del usuario asociado al proceso.
            resource_type (str): El tipo de recurso asociado al proceso.
            time_to_process (str): El tiempo necesario para procesar el recurso.
            exec_time (int): El tiempo de ejecución del proceso.
            join_time (int): El tiempo de unión del proceso.
            start_execution (int): El tiempo de inicio de ejecución del proceso.
        '''
        self._id_process = id_process
        self._id_user = id_user
        self.resource_type = resource_type
        self.time_to_process = time_to_process
        self.exec_time = exec_time
        self.join_time = 0
        self.start_execution = 0

    @property
    def id_process(self):
        return self._id_process

    @id_process.setter
    def id_process(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._id_process = value
        else:
            raise ValueError("ID must be a non-empty string")

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._id_user = value
        else:
            raise ValueError("ID must be a non-empty string")

    @property
    def resource_type(self):
        return self._resource_type

    @resource_type.setter
    def resource_type(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._resource_type = value
        else:
            raise ValueError("Resource Type must be a non-empty string")

    @property
    def exec_time(self):
        return self._exec_time

    @exec_time.setter
    def exec_time(self, value):
        if isinstance(value, int) and value >= 0:
            self._exec_time = value
        else:
            raise ValueError("Execution time must be a non-negative integer")
    
    @property
    def join_time(self):
        return self._join_time
    @join_time.setter
    def join_time(self, value):
        if isinstance(value, int) and value >= 0:
            self._join_time = value
        else:
            raise ValueError("Join time must be a non-negative integer")
        
    @property
    def start_execution(self):
        return self._start_execution
    @start_execution.setter
    def start_execution(self, value):
        if isinstance(value, int) and value >= 0:
            self._start_execution = value
        else:
            raise ValueError("Start execution time must be a non-negative integer")
        
    def print(self):
        '''
        Imprime los detalles del proceso.
        '''
        print(f"ID: {self._id_process}, User: {self._id_user}, Resource: {self.resource_type}, Exc Time: {self.exec_time}, Starting Time: {self.start_execution}")


class ManagerQueue():
    '''
    Clase que representa un administrador de colas de procesos.

    Attributes
    ----------
    - queues(dict): Diccionario que almacena las colas de procesos por tipo de recurso y duración.
    - penalties(list): Lista que almacena los usuarios penalizados.
    - active_process(list): Lista que almacena los procesos activos.
    - stats_penalties(list): Lista que almacena las estadísticas de penalizaciones por usuario.
    - stats_process(list): Lista que almacena las estadísticas de procesos ejecutados.

    Methods
    -------
    - all_empty(): Verifica si todas las colas están vacías.
    - all_processes_finished(): Verifica si todos los procesos han finalizado.
    - add_penalty(process, time): Agrega una penalización a un usuario.
    - execute_panalty(process, time): Ejecuta una penalización y mueve el proceso a la cola de larga duración.
    - manage_queue(process, time): Administra la cola de ejecución de procesos.
    - check_process(time): Verifica si los procesos activos han terminado.
    - process_queues(time): Procesa las colas de procesos y ejecuta los procesos correspondientes.
    - is_active_process_of_type(queue_type): Verifica si hay un proceso activo del mismo tipo.
    '''
    def __init__(self):
        self.queues = {"cpu_short": ArrayQueue(),
                       "cpu_long": ArrayQueue(),
                       "gpu_short": ArrayQueue(),
                       "gpu_long": ArrayQueue()}
        self.penalties = []
        self.active_process = []
        self.stats_penalties = []
        self.stats_process = []
            
    def all_empty(self):
        '''
        Verifica si todas las colas están vacías.

        Returns
        -------
        - True si todas las colas están vacías.
        - False si al menos una cola no está vacía.
        '''
        # Recorremos todas las colas y verificamos si están vacías
        return all(queue.is_empty() for queue in self.queues.values())

    def all_processes_finished(self):
        '''
        Verifica si todos los procesos han finalizado.

        Returns
        -------
        - True si no hay procesos activos.
        - False si hay al menos un proceso activo.
        '''
        # Si es None, devuelve True, si no, False
        return not self.active_process

    def add_penalty(self, process: Process, time: int):
        '''
        Agrega una penalización a un usuario.

        Returns
        -------
        - process (Process): proceso penalizado.
        - time (int): tiempo en el que se aplica la penalización.
        '''
        # Lo agregamos a la lista de penalizados
        self.penalties.append(process._id_user)
        print(f"Penalización activa: <{time}><{process._id_user}>")

    def execute_panalty(self, process: Process, time: int):
        '''
        Ejecuta una penalización y mueve el proceso a la cola de larga duración correspondiente.

        Parameters
        ----------
        - process (Process): proceso penalizado.
        - time (int): tiempo en el que se ejecuta la penalización.
        '''
        # Obtenemos el tipo de cola a la que pertenece el proceso
        type = f"{process.resource_type}_{process.time_to_process}"
        # Extraemos el proceso de la cola y lo movemos a la cola de larga duración
        tmp = self.queues[type].dequeue()
        self.queues[f"{process.resource_type}_long"].enqueue(tmp)
        # Eliminamos la penalización
        self.penalties.remove(process._id_user)  # Desactivar penalización
        print(f"Penalización aplicada: <{time}><{process._id_process}><{process._id_user}>")
        
        # Actualizar estadísticas de penalizaciones
        if process._id_user not in [x[0] for x in self.stats_penalties]:
            self.stats_penalties.append([process._id_user, 1])  # Si no se encuentra en la lista
        else:
            for penalty in self.stats_penalties:
                if penalty[0] == process._id_user:
                    penalty[1] += 1  # Incrementar el conteo de penalizaciones
                    break
            
    def manage_queue(self, process: Process, time: int):
        '''
        Administra la cola de ejecución de procesos.

        Parameters
        ----------
        - process (Process): proceso a agregar a la cola.
        - time (int): momento en el que se añade el proceso a una cola.
        '''
        # Obtenemos a que cola pertenece el proceso y lo añadimos a la cola correspondiente
        queue_key = f"{process.resource_type}_{process.time_to_process}"
        self.queues[queue_key].enqueue(process)
        # Actualizamos el tiempo de unión del proceso
        process._join_time = time
        print(f"Proceso añadido a cola de ejecución: <{time}><{process._id_process}><{process._id_user}><{process.resource_type}><{process.exec_time}>")

    def check_process(self, time: int):
        '''
        Verifica si los procesos activos han terminado.

        Parameters
        ----------
        - time (int): tiempo actual.
        '''
        # Almacenamos los procesos a eliminar
        remove_process = []
        # Recorremos los procesos activos
        for acutual_process in self.active_process:
            process_time = acutual_process.start_execution + acutual_process.exec_time
            if time >= process_time:
                print(f"Proceso terminado: <{time}><{acutual_process._id_process}><{acutual_process._id_user}>")
                # Eliminamos el proceso de la lista de activos
                remove_process.append(acutual_process)
                # Almacenar estadísticas de procesos
                queue_type = f"{acutual_process.resource_type}_{acutual_process.time_to_process}"
                self.stats_process.append([queue_type, time - acutual_process._join_time])
                # Comprobamos si el proceso debe ser penalizado
                if acutual_process.time_to_process == "short" and process_time > 5:
                    self.add_penalty(acutual_process, time)
        # Eliminamos los procesos terminados
        for process in remove_process:
            self.active_process.remove(process)
            
    def process_queues(self, time):
        '''
        Procesa las colas de procesos y ejecuta los procesos correspondientes.

        Parameters
        ----------
        - time(int): tiempo actual.
        '''
        # Recorremos las colas
        for queue_type, queue in self.queues.items():
            # Verificar si la cola no está vacía y no hay un proceso activo del mismo tipo
            if not queue.is_empty() and not self.is_active_process_of_type(queue_type):
                process = queue.first()  # Mirar el primer elemento sin desencolarlo
                # Si el proceso pertenece a un usuario penalizado y es de tipo short
                if process.id_user in self.penalties and 'short' in queue_type:
                    # Ejecutamos la penalizacion
                    self.execute_panalty(process, time)
                else:
                    # Iniciar ejecución del proceso
                    process = queue.dequeue()
                    # Actualizar tiempo de inicio de ejecución
                    process._start_execution = time
                    # Agregar a los procesos activos
                    self.active_process.append(process)

    def is_active_process_of_type(self, queue_type):
        '''
        Verifica si hay un proceso activo del mismo tipo (cpu/gpu y short/long).

        Parameters
        ----------
        - queue_type(str): tipo de cola a verificar.

        Returns
        -------- 
        - True si hay un proceso activo del mismo tipo.
        - False si no hay un proceso activo del mismo tipo.
        '''
        # Extraemos el tipo de recurso y duración
        resource_type, duration_type = queue_type.split('_')
        # Recorremos los procesos activos
        for process in self.active_process:
            # Si hay un proceso del mismo tipo en la lista de activos retornamos True
            if resource_type in process.resource_type and duration_type in process.time_to_process:
                return True
        return False