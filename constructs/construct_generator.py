from constructs.box.box import Box
from constructs.box.partition import Partition
from managers.container_managers.container_manager import ContainerManager

class ConstructGenerator(object):

    def create_default_box(self, origin=(0, 0), offset=(0, 0), width=100, height=100, container_manager=None, draw_controller=None, resizable=False, parent=None, callback=None, callback_params=[]):
        if draw_controller is None:
            pass
        if container_manager is None:
            container_manager = ContainerManager()
        return Box(origin, offset, width, height, container_manager, draw_controller, resizable, parent, callback, callback_params)

    def create_default_partition(origin=(0, 0), offset=(0, 0), width=100, height=100, containter_manager=None, draw_manager=None, resizable=None, callback=None):
        return Partition(origin, offset, width, height, containter_manager, draw_manager, resizable, callback)