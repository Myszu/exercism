class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    if not records:
        return None
    
    records.sort(key=lambda x: x.record_id)
    root = Node(records[0].record_id)

    if any([root.node_id != 0, records[-1].record_id != len(records)-1]):
        raise ValueError('Record id is invalid or out of order.')
    if any(record.parent_id > record.record_id for record in records):
        raise ValueError("Node parent_id should be smaller than it's record_id.")

    nodes = {
        0: root
    }
    
    for record in records[1:]:
        if record.record_id == record.parent_id:
            raise ValueError("Only root should have equal record and parent id.")
        if record.record_id < record.parent_id:
            raise ValueError("Node parent_id should be smaller than it's record_id.")

        node = Node(record.record_id)
        if node.node_id in nodes:
            raise ValueError("Record id is invalid or out of order.")
        nodes[node.node_id] = node

        try:
            nodes[record.parent_id].children.append(node)
        except KeyError:
            raise ValueError( "Record id is invalid or out of order.")
    
    return root
