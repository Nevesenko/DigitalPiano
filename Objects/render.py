import pygame
import random
from Data import constants as c

import pygame
import random
from Data import constants as c



class Render:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.particles = []

        pygame.init()
        self.screen = pygame.display.set_mode(c.WIDTH_AND_HEIGHT)
        while True:
            for event in pygame.event.get():
                print('1 ', event)
                #screen.fill(c.BACKGROUND)
                pygame.display.update()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # создаём новые частицы
            self.smoke()


    def choose_the_color(self, dissonans_measure):
        '''Return a list of to tuples
        which contain appropriate color choose
        the colors depend on the amount of dissonance'''
        color1 = (255, 20, 147)
        color2 = (255, 39, 42)

        return [color1, color2]

    @staticmethod
    def create_particle( x, y):
        return {
            "pos": [x, y],
            "vel": [random.uniform(-0.5, 0.5), random.uniform(-2, -0.5)],
            "radius": random.randint(5, 10),
            "alpha": 180
        }


    def smoke(self):
        for _ in range(3):
            self.particles.append(Render.create_particle(c.WIDTH_AND_HEIGHT[0] / 2 , c.WIDTH_AND_HEIGHT[1] / 2 + 130))

        self.screen.fill(c.BACKGROUND)
        # Moving the particles
        for p in self.particles[:]:
            p["pos"][0] += p["vel"][0]
            p["pos"][1] += p["vel"][1]
            p["radius"] += 0
            p["alpha"] -= 0.2

            if p["alpha"] <= 0:
                self.particles.remove(p)
                continue

            surf = pygame.Surface((p["radius"] * 2, p["radius"] * 2), pygame.SRCALPHA)
            color = random.choice(self.choose_the_color(1))
            pygame.draw.circle(
                surf,
                 color +(p["alpha"],),
                (p["radius"], p["radius"]),
                int(p["radius"])
            )
            self.screen.blit(surf, (p["pos"][0] - p["radius"], p["pos"][1] - p["radius"]))

        pygame.display.flip()
        self.clock.tick(60)

