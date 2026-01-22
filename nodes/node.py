class Node:
    def __init__(self, workflow_id, node_id):
        self._wf_id = workflow_id
        self._id = node_id
        self._parent_id = None
        self._children_ids = set()

    def set_parent_id(self, parent_id):
        self._parent_id = parent_id
    
    # param:
    # - child_id
    # - set(child_id)
    #
    def add_to_children(self, param): 
        if isinstance(param, set):
            self._children_ids.update(param)
        else:
            self._children_ids.add(param)

    def get_children_ids(self):
        return self._children_ids

    def run(self, _input):
        for 


# CUSTOM NODES

class If(Node):
    def __init__(self, workflow_id, _id):
        self().__init__(workflow_id, _id)
        self.true_node_id = true_node_id
    
    def modify(self, choice, new_node):
        if choice:
            self.true_node_id = new_node
        else:
            self.false_node_id = new_node


class Script(Node):
    def __init__(self, path, language):
        pass


class API(Node):
    def __init__(self, URL, method):
        pass

# TRIGGERS

class DateTimeTrigger(Trigger):
    def __init__(self, datetime, repetition):
        pass

