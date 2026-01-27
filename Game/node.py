class Node:
    def __init__(self, index):
        """
        Create a new Node. The node is the spaces on the tiles that contain
        settlements and cities.

        :param index: The index (id) of the node
        """
        self.index = index
        self.edges = [] # Edges the node is touching
        self.owned_by = None # Reference to the player that owns this edge
        self.city = False # True if city, false otherwise


    def reset(self):
        """
        Resets the node for a new game.

        :return: None
        """
        self.owned_by = None
        self.city = False


    def get_unowned_edges(self):
        """
        Gets all unowned surrounding edges.

        :return: Unowned surrounding edges.
        """
        unowned_edges = []
        for edge in self.edges:
            if edge.owned_by is None:
                unowned_edges.append(edge)

        return unowned_edges