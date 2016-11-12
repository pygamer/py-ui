# py-ui
This is a UI library that interfaces with Pygame.

#Dependencies
Pygame 1.9.1


Currently only tested with Python 2.7


#Current API

#Constructs
Constructs are the things that are potentially viewable on the screen. Constructs organized by behavior. Within the contsructs folder you will find folders for "box", "input", "output" and "radial" behaviors.

Box types can have an unlimited amount of children (containers) if it is utilizing a container_manager. Children of a box type are always box types.

Input types inherit from Box type, are interactible, but cannot have children.

Output types inherit from Box type, are NOT interactible, but cannot have children.

Radial types do no have container managers, and can only have one child. Children of a radial type are always Box types.

All constructs have several methods in common:

build() - Calls the build() method on all managers attached to this construct

update() - Calls the update() method on all managers attached to this construct

draw() - Calls the draw() method on all managers attached to this construct

#Managers
Managers control the children and drawing procedures of a construct. Managers are always of the type they are managing, so a BoxDrawManager inherits fomr the Box type. Every construct will have at most two managers. One for handling it's children, the other for drawing itself. Some constructs cannot have children (e.g. a checkbox), but all constructs can be drawn.

Managers have a few common methods that are called when the same method is called on the object they are attached to.
e.g if you call the method Box.draw(), this calls the draw() function on that box's container manager and draw manager.

These common methods are:

build() - In the case of container managers, this calls build() on all child containers. In the case of draw managers this creates and populates a pygame.Surface object for use in the draw() method.

update(dt) - In the case of container managers this calls update() on all child containers. In the case of draw managers this method handles color changes, graphics changes, and positional movement, and is overloadable to do whatever you like. returns False if there doesnt need to be a redraw, True if there does need to be a redraw. Takes a parameter dt for the time since last frame.

draw(surface) - In the case of container managers, this calls the draw() method on all child containers. In the case of draw managers, this function blits the surface made by build() to the given surface parameter




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
