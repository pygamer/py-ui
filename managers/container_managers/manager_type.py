
class ManagerType(object):


    class GRID(object):

        max__container_width = 100
        max_container_height = 100
        min_container_width = 50
        min_container_height = 50

        def __init__(self,
                     max_container_width=100,
                     max_container_height=100,
                     min_container_width=50,
                     min_container_height=50):
            self.max_container_height = max_container_height
            self.max_container_width = max_container_width
            self.min_container_width = min_container_width
            self.min_container_height = min_container_height

        def build(self, containers):
            grid_dimensions = ceil(sqrt(len(containers)))


        def __eq__(self, other):
            return isinstance(other, ManagerType.GRID)