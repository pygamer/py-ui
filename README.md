# py-ui
This is a UI library that interfaces with Pygame.

#Dependencies
Pygame 1.9.1


Currently only tested with Python 2.7


#Current API

Constructs are organized by behavior. Within the contsructs folder you will find folders for "box", "input", "output" and "radial" behaviors.

Box types can have an unlimited amount of children if it is utilizing a container_manager.

Input types inherit from Box type, but cannot have children.

Output types inherit from Box type, but cannot have children.

Radial types do no have container managers, and can only have one child.


#Box
You can access all of the currently working box-like constructs through the constructs.construct_generator.ConstructGenerator static class.

Each box construct has a few parameters you can change:

origin - The position of the parent construct - (x, y) tuple
offset - The position of this element, relative to the given origin - (x, y) tuple
width - The width of this element - Int
height - The height of this element - Int
draw_manager - The class that actually draws using pygame libraries. This class can be overloaded to use different graphics libraries - BoxDrawManager object

Draw managers MUST inherit the class-type are drawing. e.g a BoxDrawManager implements the Box class.

The Box type has some other special parameters you can give it.

container_manager - The class managing this container's children. This can be None for a container with no children and can be added later - ContainerManager object
resizable - A boolean declaring that this Box is resizable. Currently unused - Bool
parent - A reference to the parent container, currently unsued - Box object
callback - A reference to a function that is called when Box.callback() is called - function reference
callback_params - A list of parameters that are given to the callback function when it is called, in order - List
