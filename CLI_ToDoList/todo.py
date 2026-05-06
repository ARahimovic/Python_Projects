import os
import json
import argparse
from enum import Enum


class Priority(Enum):
    LOW="low"
    Medium="medium"
    HIGH="high"
    URGENT="urgent"

    def __str__(self):
        return self.value

    
class toDoList:
    def __init__(self, jsonFile="tasks.json"):
        self.jsonFile = jsonFile
        self.data = { "metadata" : {"last_used_id" : 0}, "tasks" : []}
        self._load_data()

    def _load_data(self):
        if os.path.exists(self.jsonFile):
            with open(self.jsonFile, "rt") as jf:
                try :
                    self.data = json.load(jf)
                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {self.jsonFile}")
                    self.data = { "metadata" : {"last_used_id" : 0}, "tasks" : []}
                    self._save_tasks()


    def _save_tasks(self):
        with open(self.jsonFile, "wt") as jf:
            json.dump(self.data, jf)

    def add_task(self, name, description="", status='pending',priority ="low"):
        new_id = self.data["metadata"]["last_used_id"] + 1
        task = {
            'id'   :new_id,
            'name' : name, 
            'description' : description,
            'status' : status,
            'priority' : priority
            }

        self.data["tasks"].append(task)
        self.data["metadata"]["last_used_id"] = new_id
        self._save_tasks()

    
    def mark_as_done(self, task_id):
        if not self.data["tasks"] : 
            return 

        for task in self.data["tasks"] :
            if task["id"] == task_id :
                task['status'] = 'Done'
                print(f"Task {task["name"]} with id {task_id} marked as completed")
                self._save_tasks()
                return

        print(f"Task {task_name} not found")


    def list_tasks(self):
        if not self.data["tasks"] :
            print("List is emtpy : no tasks added")
            return 

        print(f"{'id':^5} {'name':^10} {'description':^15} {'status':^10} {'Priority':^5}")
        for task in self.data["tasks"] :
            print(f"{task['id']:^5} {task['name']:^10} {task['description']:^15} {task['status']:^10} {task['priority']:^5}")


    def delete_task(self, task_id):
        if not self.data["tasks"] : 
            return 
        
        newList = [task for task in self.data["tasks"] if task["id"] != task_id]
        
        if len(newList) < len(self.data["tasks"]) :
            print(f"Task with id {task_id} removed")
            self.data["tasks"] = newList
            self._save_tasks()
        else :
            print(f"Task with id {task_id} not found")        


    def set_priority(self, task_id, priority):
        if not self.data["tasks"]:
            print("task list is empty")   
            return 
        
        for task in self.data["tasks"]:
            if task["id"] == task_id :
                task['priority'] = priority
                return

        print(f"Task with id {task_id} not found") 


def main():
    todolist = toDoList()
   
    parser = argparse.ArgumentParser(description = "CLI to do list")
    subparsers = parser.add_subparsers(dest='command', help="commands for CRUD operations for our CLI to dolist")
    

    ### add command ###
    add_parser = subparsers.add_parser('add', help = "add specific task to the list of tasks :\nneed to provide at least name")
    add_parser.add_argument("name", help = "name of the task")
    add_parser.add_argument("--description", "-d", default="", help="description of the task")
    add_parser.add_argument("--priority", "-p", default="low", choices=[p.value for p in Priority], help="set priority of the task")
    add_parser.add_argument("--status", "-st", default="pending", help="initial status of the task")
    #add_parser.set_defaults(func=todolist.add_task)

    ### list command ###
    list_parser = subparsers.add_parser('list', help="list tasks")

    ### remove task command ###
    remove_parser = subparsers.add_parser('delete', help="delete task by id")
    remove_parser.add_argument('id', type=int, help='Id of unique task to delete')

    ### done command ###
    done_parser = subparsers.add_parser('done', help="mark a task as done")
    done_parser.add_argument('id', type=int, help="id of task to be marked as done")


    args = parser.parse_args()
    
    if args.command == 'add' :
        todolist.add_task(args.name, args.description, args.status, args.priority)
    elif args.command == 'list':
        todolist.list_tasks()
    elif args.command == 'delete':
        todolist.delete_task(args.id)
    elif args.command == 'done' :
        todolist.mark_as_done(args.id)
    else :
        parser.print_help()
   
if __name__ == "__main__" :
    main()