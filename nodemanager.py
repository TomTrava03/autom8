class NodeType(enum):
    START_TRIGGER = 0 # mh
    DATE_TIME_TRIGGER = 1
    IF = 1


class NodeManager:
    def __init__(self, path, wf_id):
        self.nodes = dict()
        self.path = f"/data/nodes/${wf_id}.json"

    def add_node(self, node_type, from_node_id, params):
        from_node.add_next_node(to_node)

    def delete_node(self, node_id):

        # 1 -> 2 -> 3 : 1 -> 3

        node = self.nodes[node_id]
        child_id = node.get_child_id()

        parent_id = node.get_parent_id()
        parent_node = nodes[parent_id]
        parent_node.add_to_childre_ids(next_node.get_id())

        self.nodes.pop(node_id)

    def print_nodes(self, parent_id):
        spaces = 0
        if self.nodes[parent_id].get_children_ids is not None:
            spaces += 1
            for nodes_id in start_node_id.get_children_ids():
                print(" "*spaces)
                print(f"└─${nodes_id}\n")
                self.print_nodes(parent_id)
                

