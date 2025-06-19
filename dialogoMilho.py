import arcade

# Constantes
SPRITE_SCALING = 0.5
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 725
WINDOW_TITLE = "Player + Caixa de Diálogo"
MOVEMENT_SPEED = 5

class Player(arcade.Sprite):
    """Classe do jogador"""
    def update(self, delta_time: float = 1/60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Mantém o player dentro da janela
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT










class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        self.sprite_list = arcade.SpriteList()



        self.player_list = None
        self.npc_list = None

        self.player_sprite = None
        self.npc = None

        # Variáveis do diálogo
        self.dialog_active = False
        self.dialog_page = 0
        self.dialog_texts = [
            "Aqui é nossa plantação de milho.",
            "Ela é muito importante para a economia da fazenda.",
            "E fazemos pratos deliciosos com eles!"
        ]

        self.background_sprite = arcade.Sprite("milho.png", scale=0.5)
        self.background_sprite.center_x = SCREEN_WIDTH / 2
        self.background_sprite.center_y = SCREEN_HEIGHT / 2
        self.sprite_list.append(self.background_sprite)



    def setup(self):
        # Listas de sprites
        self.player_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()

        # Player
        self.player_sprite = Player("image.png", scale=0.2)
        self.player_sprite.center_x = SCREEN_WIDTH - 200
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        # NPC (quadrado azul)
        self.npc = arcade.SpriteSolidColor(50, 50, arcade.color.TRANSPARENT_BLACK)
        self.npc.center_x = 600
        self.npc.center_y = 350
        self.npc_list.append(self.npc)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw() 
        self.player_list.draw()
        self.npc_list.draw()
        

        # Caixa de diálogo
        if self.dialog_active:
            box_width = 800
            box_height = 100
            x = SCREEN_WIDTH / 2 - box_width / 2
            y = 50

            arcade.draw_rect_filled(arcade.rect.XYWH(100, 100, 10000, 80), arcade.color.BLACK_BEAN)
            arcade.draw_text(
                self.dialog_texts[self.dialog_page],
                x,
                y + 30,
                arcade.color.YELLOW_ORANGE,
                32,
                width=box_width - 40
            )

    def on_update(self, delta_time):
        self.player_list.update(delta_time)

        # Verifica colisão com NPC
        if arcade.check_for_collision(self.player_sprite, self.npc):
            if not self.dialog_active:
                self.dialog_active = True
                self.dialog_page = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_sprite.change_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_sprite.change_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        # Avança nas falas com clique do mouse
        if self.dialog_active and button == arcade.MOUSE_BUTTON_LEFT:
            if self.dialog_page < len(self.dialog_texts) - 1:
                self.dialog_page += 1
            else:
                self.dialog_active = False











def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    game_view = GameView()
    game_view.setup()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()
