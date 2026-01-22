from nodemanager import NodeManager

from uuid import UUID

class Workflow:
    def __init__(self, name: str):
        self._name = name
        self._n_manager = NodeManager(f"{name}")

    def set_starting_point(self, node_id):
        self._starting_node_id = node_id

    def start(self):
        self._n_manager.run_node(self._starting_node_id)

    def add_node(self, parent_id, node_type, params):
        n_manager.add_node(parent_id, node_type, params)
        if parent_id is None:
            node = self._n_manager.get_node(1)
            self.set_starting_point(node.get_id())

    def delete_node(self, node_id):
        self._n_manager.delete_node(node_id)

    def __str__():
        self._n_manager.print_nodes()

    def get_id(self) -> UUID:
        return self._wf_id
    
    def empty(self):
        self._n_manager.empty_workflow()

