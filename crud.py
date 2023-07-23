class Task():

    def __init__(self, id_task = "default", dt_created = "yyyy-mm-dd", title = "title", task_description = "description", dt_deliver = "yyyy-mm-dd"):

        self.__id_task = id_task
        self._dt_created = dt_created
        self._title = title
        self._task_description = task_description
        self._dt_deliver = dt_deliver

    def getTask(self):
        listagem = [f'id_task: {self.__id_task}', 
                    f'dt_created: {self._dt_created}', 
                    f'title: {self._title}', 
                    f'task_description: {self._task_description}', 
                    f'dt_deliver: {self._dt_deliver}']
        return listagem

    def setDate(self, date):
        self._dt_created = date
    
    def setTitle(self, text):
        self._title = text
    
    def setTaskDescription(self, description):
        self._task_description = description
    
    def setDeliverDate(self, date):
        self._dt_deliver = date
    
    def setId(self, id):
        self.__id_task = str(id)
    
    def getTaskId(self):
        return self.__id_task
    
    
    
    def __str__(self):
        return f'{self.__id_task}, {self._dt_created}, {self._title}, {self._task_description}, {self._dt_deliver}'
    
    



class Data():
    def __init__(self):
        self._tasks = {}
    
    def addTask(self, task):
        self._tasks[task.getTaskId()] = task
    
    def getData(self):
        for id, values in self._tasks.items():
            print(values)
        #return self._tasks
    
    def existId(self, id):
        isKey = False
        for key in self._tasks.keys():
            if id == key:
                isKey = True
                break
        return isKey

    def getTaskById(self, id):

        if self.existId(id):
            return self._tasks[id]
        else:
            print('Não existe essa Task')
            return False
    
    def removeTaksById(self, id):
        if self.existId(id):
            self._tasks.pop(id)
            print(f'Task {id} removida com sucesso')
        else:
            print('Não existe essa Task')
    
    # def alterTaskById(self, id):
    #     #{self._dt_created}, {self._title}, {self._task_description}, {self._dt_deliver}

    #     if self.existId(id):
    #         task = self.getTaskById(id)
    #         print(task)
        
        

    def __str__(self):
        return f'{self._tasks}'


