from workflow import Workflow

import json
from pathlib import Path

class WorkflowManager:
    _FILE_PATH = Path(__file__).resolve().parent / "data" / "workflows.json"

    def __init__(self):
        self._workflows = dict() # TODO: entry -> {name : ?}
        self._indexes = dict()

    def add_workflow(self, name): # empty workflow
        new_workflow = Workflow(name)
        self._workflows[wf_id] = new_workflow

    def delete_workflow(self, wf_id):
        _workflows[wf_id].empty()
        self._workflows.pop(wf_id)

    # def set_workflow_starting_point(self, wf_id, node_id):
    #    self._workflows[wf_id].set_starting_point(node_id)

    def start_workflow(self, wf_id):
        self._workflows[wf_id].start()

    def save_workflows(self):
        data = json.dumps(self._workflows) # since workflows is a dict!
        with type(self)._FILE_PATH.open("w") as f: # type(self) -> forcefully looks for the class value, since "private" doesn't exist
            f.write(data)
            f.close()

    def load_workflows(self):
        try:
            with type(self)._FILE_PATH.open("r") as f:
                data = f.read()
                f.close()

            self._workflows = json.loads(data)
        except ValueError: # includes JSONDecodeError
            print("[?]Nothing to load.")

    def list_workflows(self):
        if not bool(self._workflows):
            print("No workflows to show.")
        else:
            self._indexes = enumerate(self._workflows, 1) # starting from 1
            for index, key in self._indexes:
                print(f"{index}. {key}")
            return self._indexes

    def list_workflow_nodes(self, wf_id):
        self._workflows[name].__str__()

