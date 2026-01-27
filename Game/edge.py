class Edge:
    def __init__(self, index):
        """
        Create a new Edge. The edge is the spaces on the tiles that contain
        the roads.

        :param index: The index (id) of the road.
        """
        self.index = index
        self.nodes = [] # Nodes the edge is touching
        self.owned_by = None # Reference to the player that owns this edge


    def reset(self):
        """
        Resets the edge for a new game.

        :return: None
        """
        self.owned_by = None


    def get_neighbour(self, node):
        """
        Gets the node neighbouring the specified node. I.e. gets the other
        node touching this edge, that isn't the specified node.

        :param node: The node to get its neighbour.
        :return: The neighbour of the specified node.
        """
        for neighbouring_node in self.nodes:
            if neighbouring_node != node:
                return neighbouring_node
