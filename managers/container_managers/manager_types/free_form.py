from managers.container_managers.manager_types.manager_type import ManagerTypeInterface


class Freeform(ManagerTypeInterface):
    """
    Use this class within a container manager to allow freeform movement of children.
    This means that each child's position will not be set  automatically.
    """
    def __init__(self):
        pass

    def build(self, master, containers):
        pass

    def __eq__(self, other):
        return isinstance(other, Freeform)