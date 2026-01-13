import pygame
import time


class ImageHandler:
    def __init__(self):
        self.pics = dict()

    def loadFromFile(self, filename, id=None):
        if id is None:
            id = filename
        self.pics[id] = pygame.image.load(filename).convert()

    def render(self, surface, id, position=None, clear=False, size=None):
        if clear:
            surface.fill((5, 2, 23))

        if position is None:
            picX = int(surface.get_width() / 2 - self.pics[id].get_width() / 2)
        else:
            picX, picY = position

        if size is None:
            surface.blit(self.pics[id], (picX, picY))
        else:
            surface.blit(pygame.transform.smoothscale(self.pics[id], size), (picX, picY))


# Initialize Pygame
pygame.init()

# Set the display mode
screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)

# Initialize image handler
handler = ImageHandler()


def display():
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame1.jpg", "1")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame2.jpg", "2")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame3.jpg", "3")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame4.jpg", "4")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame5.jpg", "5")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame6.jpg", "6")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame7.jpg", "7")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame8.jpg", "8")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame9.jpg", "9")
    handler.loadFromFile(r"C:\Users\user\PycharmProjects\JarvisAI\images\frame10.jpg", "10")


display()


def face():
    clock = pygame.time.Clock()

    for i in range(1, 11):
        screen_size = screen.get_size()
        picture = handler.pics[str(i)]
        picture_width, picture_height = picture.get_size()

        scale_factor_width = screen_size[0] / picture_width
        scale_factor_height = screen_size[1] / picture_height
        scale_factor = min(scale_factor_width, scale_factor_height)

        new_width = int(picture_width * scale_factor)
        new_height = int(picture_height * scale_factor)

        A = int(screen_size[0] / 2 - new_width / 2)
        B = int(screen_size[1] / 2 - new_height / 2)

        handler.render(screen, str(i), (A, B), True, (new_width, new_height))
        pygame.display.flip()  # Use pygame.display.flip() instead of pygame.display.update()
        time.sleep(0.2)
        clock.tick(30)  # Adjust the frame rate


def test():
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        face()

    # Quit Pygame
    pygame.quit()
