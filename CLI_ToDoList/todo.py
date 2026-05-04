class toDoList:
    def __init__(self, jsonFile="tasks.json"):
        try:
            with open(jsonFile, "rt") as jf :
                self.tasks = json.load(jf)
        except FileNotFoundError :
            self.tasks = []
            self.globalId = 0
                    

    def add_task(self, name, status='pending', description="",priority ="low"):
        task = {
            'id'   : self.globalId,
            'name' : name, 
            'description' : description,
            'status' : status,
            'priority' : priority
            }

        self.globalId += 1
        self.tasks.append(task)
        print(self.tasks)

    
    def mark_completed(self, task_name, use_id=False):
        if not self.tasks : 
            return 

        keyToLook = 'id' if use_id else 'name'
        for task in self.tasks :
            if task[keyToLook] == task_name :
                task['status'] = 'completed'
                print(f"Task {task_name} marked as completed")
                return

        print(f"Task {task_name} not found")


    def list_tasks(self):
        if not self.tasks :
            print("List is emtpy : no tasks added")
            return 

        print(f"{'id':^5} {'name':^10} {'description':^15} {'status':^10} {'Priority':^5}")
        for task in self.tasks :
            print(f"{task['id']:^5} {task['name']:^10} {task['description']:^15} {task['status']:^10} {task['priority']:^5}")


    def remove_task(self, task_name, use_id=False):
        if not self.tasks : 
            return 
        
        keyToLook = 'id' if use_id else 'name'
        for task in self.tasks:
            if task[keyToLook] == task_name :
                self.tasks.remove(task)
            


if __name__ == "__main__" :
    todolist = toDoList()
    todolist.add_task("task 0", "first task")
    todolist.add_task("task 1", "second task")
    todolist.list_tasks()
    todolist.mark_completed('task 0')
    todolist.list_tasks()
    todolist.mark_completed(1, use_id = True)
    todolist.list_tasks()
    todolist.remove_task('task 0')
    todolist.list_tasks()