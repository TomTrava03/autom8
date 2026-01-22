 

import os
import json
from pathlib import Path

#class NodeType(enum):
#    START_TRIGGER = 0 # mh
#    DATE_TIME_TRIGGER = 1
#    IF = 1


class NodeManager:
    _BASE_DIR = Path(__file__).resolve().parent
    _DATA_DIR = _BASE_DIR / "data/nodes"

    def __init__(self, wf_id):
        self._nodes = dict()
        self._FILE_PATH = self._DATA_DIR / f"{wf_id}.json"

    def add_node(self, parent_id, node_type, params):
        n = Node()
        parent_id.add_to_children(n.get_id())
        from_node_id.add_next_node(to_node)

    def delete_node(self, node_id): # 1 -> 2 -> 3 : 1 -> 3
        node = self._nodes[node_id]
        child_id = node.get_child_id()

        parent_id = node.get_parent_id()
        parent_node = nodes[parent_id]
        parent_node.add_to_childre_ids(next_node.get_id())

        self.nodes.pop(node_id)

    def empty_workflow(self):
        self._nodes.clear()
        os.remove(self._path)

    def list_nodes(self, node_id):
        spaces = 0
        print(" "*spaces)
        print(f"└─{node_id}")
        if self._nodes[node_id].get_children_ids is not None:
            spaces += 1
            for node_id in start_node_id.get_children_ids():
                self.print_nodes(parent_id)
        
    def load_nodes(self):
        with open(self._path) as f:
            data = f.read()
            f.close()

    def save_nodes(self):
        data = json.dumps(self._nodes)
        with self._FILE_PATH.open("w") as f:
            f.write(data)   
            f.close()

