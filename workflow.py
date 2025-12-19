from nodemanager import NodeManager

class Workflow: 
    def __init__(self, wf_id, node_id):
        self.wf_id = wf_id
        self.starting_node_id = node_id # is necessary ?
        self.n_manager = NodeManager(f"{self.wf_id}")

    def new(self, wf_id):
        self.wf_id = wf_id

    def set_starting_point(self, node_id):
        self.starting_node_id = node_id

    def start(self):
        starting_node.run()

    def add_node(self, parent_node, child_node, node_type, params):
        n_manager.add_node() # can i skip this lines? i dont think so.

    

