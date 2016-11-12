from constructs.box.box import Box


class Partition(Box):

    """
    This class is used for creating a partition of the screen that can
    be resized independent of other partitions.

    It takes the same arguments as a Box construct,
    seeing as it is a box construct.

    """

    def __init__(self,
                 origin,
                 offset,
                 width,
                 height,
                 containter_manager,
                 draw_manager,
                 resizable):
        super(Partition, self).__init__(origin, offset, width, height, containter_manager, draw_manager, resizable)

