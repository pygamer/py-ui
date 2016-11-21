if __name__ == "__main__":
    import pygame
    import pygame.locals
    from event.click_event import ClickEvent
    from event.mouse_motion_event import MouseMotionEvent
    from managers.container_managers.manager_types.horizontal import Horizontal
    from managers.container_managers.manager_types.vertical import Vertical
    from managers.container_managers.container_manager import ContainerManager
    from managers.draw_managers.box_draw_manager import BoxDrawManager
    from constructs.construct_generator import ConstructGenerator
    d = BoxDrawManager()
    main_cm = ContainerManager(Vertical())


    b = ConstructGenerator.create_box(origin=(50, 50), width=500, height=500, container_manager=main_cm)
    ce = ClickEvent(b)
    me = MouseMotionEvent(b)
    cm1 = ContainerManager(Horizontal())
    hor_box_1 = ConstructGenerator.create_box(container_manager=cm1)
    for _ in range(6):
        bo = ConstructGenerator.create_box()
        bo.set_bordered(False)
        ce1 = ClickEvent(bo)
        me1 = MouseMotionEvent(bo)
        bo.events = [ce1, me1]
        bo.add_container(ConstructGenerator.create_label(text="Hello"))
        hor_box_1.add_container(bo)
    b.add_container(hor_box_1)
    cm2 = ContainerManager(Horizontal())
    hor_box_2 = ConstructGenerator.create_box(container_manager=cm2)
    for _ in range(8):
        bo = ConstructGenerator.create_box()
        bo.set_bordered(False)
        ce1 = ClickEvent(bo)
        me1 = MouseMotionEvent(bo)
        bo.events = [ce1, me1]
        bo.add_container(ConstructGenerator.create_label(text="Hello"))
        hor_box_2.add_container(bo)
    b.add_container(hor_box_2)

    b.build()
    pygame.init()
    s = pygame.display.set_mode((800, 600))
    s.fill((255, 255, 255))
    b.draw(s)
    while True:
        update = False
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
            if b.check_event(event):
                update = True
        if update:
            b.build()
            s.fill((255, 255, 255))
            b.draw(s)
        pygame.display.update()