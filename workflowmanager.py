import Workflow from workflow

import json
import uuid

class WorkflowManager:
    def __init__(self):
        self.workflows = dict() # wf_id : wf
        self.path = "/data/workflows.json"

    def add_workflow(self): # empty workflow
        wf_id = uuid.uuid4()

        temp = Workflow.new(wf_id)
        self.workflows[wf_id] = temp

    def delete_workflow(self):
        pass

    def set_workflow_starting_point(self, wf_id, node_id):
        self.workflows[wf_id].set_starting_point(node_id)

    def start_workflow(self, wf_id):
        self.workflows[wf_id].start()
    
    def save_workflows(self):
        data = json.dumps(workflows) # since workflows is a dict!
        with open(path, "w") as f:
            f.write(data)           
            f.close()

    def load_workflows(self):
        with open(path, "r") as f:
            data = f.read()
            f.close()
    
        workflows = json.loads(data)

    def get_workflow_by_index(self):
        pass

    def get_workflow_by_id(self, wf_id):

    
    def list_workflows(self):
        text = ""
        num = 1
        for _id in workflows:
            text += f"{num}. "
        return text        

