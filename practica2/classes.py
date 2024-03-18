from materiales.array_queue import ArrayQueue

class Process():
    def __init__(self, id_process: str, id_user: str, resource_type: str, time_to_process: str, exec_time: int):
        self._id_process = id_process
        self._id_user = id_user
        self._resource_type = resource_type
        self._time_to_process = time_to_process
        self._exec_time = exec_time
        self._join_time = 0
        self._start_execution = 0
        
    @property
    def id_process(self):
        return self._id_process
    @id_process.setter
    def id_process(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
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
    def exc_time(self):
        return self._exc_time
    @exc_time.setter
    def exc_time(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._exc_time = value
        else:
            raise ValueError("Execution time must be a non-negative integer")
    
    @property
    def starting_time(self):
        return self._starting_time
    @starting_time.setter
    def starting_time(self, value):
        if isinstance(value, int) and value >= 0:
            self._starting_time = value
        else:
            raise ValueError("Starting time must be a non-negative integer")
    
    def print(self):
        if self is not None:
            print(f"ID: {self.id_process}, User: {self.id_user}, Resource: {self.resource_type}, Exc Time: {self.exc_time}, Starting Time: {self.starting_time}")

    
class ManagerQueue():
    def __init__(self):
        self.cpu_short = ArrayQueue()
        self.cpu_long = ArrayQueue()
        self.gpu_short = ArrayQueue()
        self.gpu_long = ArrayQueue()
        self.penalties = []
        
    def all_empty(self):
        return self.cpu_short.is_empty() and self.cpu_long.is_empty() and self.gpu_short.is_empty() and self.gpu_long.is_empty()
    
    def manage_queue(self, process: Process):
        match (process.resource_type, process.exc_time):
            case ("cpu", "short"):
                self.cpu_short.enqueue(process)
            case ("cpu", "long"):
                self.cpu_long.enqueue(process)
            case ("gpu", "short"):
                self.gpu_short.enqueue(process)
            case ("gpu", "long"):
                self.gpu_long.enqueue(process)
            case (_, _):
                raise Exception("Resource type not found")    
    
    
    # Seguir desde el c del 3
    def execute_process(self, process_queue: ArrayQueue, time: int):
        if self.cpu_short.first() not in process_queue:
            if self.cpu_short.first().id_user in self.penalties:
                process = self.cpu_short.dequeue()
                self.cpu_long.enqueue(process)
                self.penalties.pop(self.penalties.index(process.id_user))
                
            pc_short = self.cpu_short.enqueue(process_queue.dequeue())
            pc_short._start_execution = time
            
        if self.cpu_long.first() not in process_queue:
            pc_long = self.cpu_long.enqueue(process_queue.dequeue())
            pc_long._start_execution = time
            
        if self.gpu_short.first() not in process_queue:
            if self.gpu_short.first().id_user in self.penalties:
                process = self.gpu_short.dequeue()
                self.gpu_long.enqueue(process)
                self.penalties.pop(self.penalties.index(process.id_user))
            pg_short = self.gpu_short.enqueue(process_queue.dequeue())
            pg_short._start_execution = time
            
        if self.gpu_long.first() not in process_queue:
            pg_long = self.gpu_long.enqueue(process_queue.dequeue())
            pg_long._start_execution = time
        

        
        
        
    
    def check_process(self, process: Process, time: int):
        pass
    
    def add_panalty(self, process: Process):
        # mejor con penalty (id_user, 1)
        self.penalties.append(process.id_user)