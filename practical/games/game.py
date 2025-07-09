import pygame
import random

class PaddleGame:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pong con control de mano")
        self.clock = pygame.time.Clock()

        # Paleta
        self.paddle_x = 20
        self.paddle_y = height // 2
        self.paddle_width = 20
        self.paddle_height = 80

        # Segunda paleta (jugador 2 o IA)
        self.paddle2_x = self.width - 40
        self.paddle2_y = self.height // 2
        self.score_ai = 0

        # Modo jugador 2: "auto" o "hand"
        self.mode_player2 = "auto"  # Cambia a "hand" para control dual

        # Dificultad: "facil", "media", "dificil"
        self.difficulty = "dificil"  # puedes cambiarla luego desde el menú si deseas

        # Velocidad IA según dificultad
        self.ai_speed = {
            "facil": 2,
            "media": 4,
            "dificil": 7
        }[self.difficulty]



        # Pelota
        self.ball_radius = 10
        self.ball_x = width // 2
        self.ball_y = height // 2
        self.base_speed = 20
        self.speed_multiplier = 1.0
        self.ball_vel_x = -self.base_speed
        self.ball_vel_y = random.choice([-5, 5])

        # Puntaje
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 24)

        
        

    def draw(self):
        self.screen.fill((0, 0, 0))
        # Paleta
        pygame.draw.rect(self.screen, (255, 255, 255),
                        (self.paddle_x, self.paddle_y, self.paddle_width, self.paddle_height))
        # Paleta 2
        pygame.draw.rect(self.screen, (255, 255, 255),
            (self.paddle2_x, self.paddle2_y, self.paddle_width, self.paddle_height))

        # Pelota
        pygame.draw.circle(self.screen, (255, 255, 255), (self.ball_x, self.ball_y), self.ball_radius)

        # Puntaje
        score_text = self.font.render(f"Puntos: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Puntaje jugador 2
        score2_text = self.font.render(f"Rival: {self.score_ai}", True, (255, 255, 255))
        self.screen.blit(score2_text, (self.width - 150, 10))


        pygame.display.flip()

    def update_paddle_y(self, new_y):
        new_y = max(0, min(new_y, self.height - self.paddle_height))
        self.paddle_y = new_y

    def tick(self):
        self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update_ball(self):
        self.ball_x += self.ball_vel_x
        self.ball_y += self.ball_vel_y

        # Rebote vertical
        if self.ball_y <= self.ball_radius or self.ball_y >= self.height - self.ball_radius:
            self.ball_vel_y *= -1

        # Rebote con paleta
        # if (
        #     self.paddle_x < self.ball_x - self.ball_radius < self.paddle_x + self.paddle_width
        #     and self.paddle_y < self.ball_y < self.paddle_y + self.paddle_height
        # ):
        #     self.ball_vel_x *= -1

        # Colisión con paleta izquierda (jugador)
        if (
            self.ball_vel_x < 0 and
            self.ball_x - self.ball_radius <= self.paddle_x + self.paddle_width and
            self.paddle_y <= self.ball_y <= self.paddle_y + self.paddle_height
        ):
            self.ball_x = self.paddle_x + self.paddle_width + self.ball_radius  # evitar superposición
            self.ball_vel_x *= -1
            self.increase_speed()



        # Rebote con paleta 2 (auto o control humano)
        # if (
        #     self.paddle2_x < self.ball_x + self.ball_radius < self.paddle2_x + self.paddle_width
        #     and self.paddle2_y < self.ball_y < self.paddle2_y + self.paddle_height
        # ):
        #     self.ball_vel_x *= -1
        #     self.increase_speed()
        # Colisión con paleta derecha (rival)
        if (
            self.ball_vel_x > 0 and
            self.ball_x + self.ball_radius >= self.paddle2_x and
            self.paddle2_y <= self.ball_y <= self.paddle2_y + self.paddle_height
        ):
            self.ball_x = self.paddle2_x - self.ball_radius  # evitar superposición
            self.ball_vel_x *= -1
            self.increase_speed()



        # Reinicio si se va la bola por la derecha
        if self.ball_x > self.width + self.ball_radius:
            self.reset_ball()
            self.score += 1


        # Si la pelota sale por izquierda (pierde jugador)
        if self.ball_x < -self.ball_radius:
            self.reset_ball()
            self.score_ai += 1

    def increase_speed(self):
        self.speed_multiplier += 0.1
        self.ball_vel_x = int(self.base_speed * self.speed_multiplier) * (1 if self.ball_vel_x > 0 else -1)
        self.ball_vel_y = int(self.ball_vel_y * 1.05)

    def reset_ball(self):
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.base_speed = 20
        self.speed_multiplier = 1.0
        self.ball_vel_x = -self.base_speed
        self.ball_vel_y = random.choice([-5, 5])
        # self.score = 0
        # self.score_ai = 0

    def update_ai_paddle(self):
        target_y = self.ball_y
        center_y = self.paddle2_y + self.paddle_height // 2

        # Movimiento automático del paddle 2 para seguir la pelota
        if target_y > center_y:
            self.paddle2_y += self.ai_speed
        elif target_y < center_y:
            self.paddle2_y -= self.ai_speed

        self.paddle2_y = max(0, min(self.paddle2_y, self.height - self.paddle_height))


    def quit(self):
        pygame.quit()
