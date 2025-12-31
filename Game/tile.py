class Tile:
    def __init__(self):
        self.resource_type = None
        self.dice_value = None

    def reset(self, resource_type, dice_value):
        self.resource_type = resource_type
        self.dice_value = dice_value
