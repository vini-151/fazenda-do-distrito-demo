import arcade

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Interação com Caixa de Diálogo"

PLAYER_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.player_list = arcade.SpriteList()
        self.npc_list = arcade.SpriteList()

        self.player = arcade.SpriteSolidColor(50, 50, arcade.color.RED)
        self.player.center_x = (SCREEN_WIDTH/ 2) - 100
        self.player.center_y = (SCREEN_HEIGHT / 2) - 100
        self.player_list.append(self.player)

        self.npc = arcade.SpriteSolidColor(50, 50, arcade.color.BLUE)
        self.npc.center_x = SCREEN_WIDTH/ 2
        self.npc.center_y = SCREEN_HEIGHT / 2
        self.npc_list.append(self.npc)

        self.player_speed_x = 0
        self.player_speed_y = 0

        self.dialog_active = False
        self.dialog_page = 0
        self.dialog_texts = [
            "Aqui é nossa plantação de milho.",
            "Ela é muito importante para a economia da fazenda.",
            "E fazemos pratos deliciosos com eles!"
        ]

    def on_draw(self):
        self.clear()
        self.player_list.draw()
        self.npc_list.draw()

        if self.dialog_active:
            # Coordenadas da caixa de diálogo
            X = SCREEN_WIDTH / 2 - 300
            Y = SCREEN_HEIGHT / 2 + 300
            width = SCREEN_WIDTH
            bottom = 70

            arcade.draw_rect_filled(arcade.rect.XYWH( X, bottom + 50, width, bottom), arcade.color.WHITE)


            arcade.draw_text(
                self.dialog_texts[self.dialog_page],
                X,
                bottom + 50,
                arcade.color.BLACK,
                16,
                width=Y - X - 40,
                multiline=False
            )

    def on_update(self, delta_time):
        self.player.center_x += self.player_speed_x
        self.player.center_y += self.player_speed_y

        if arcade.check_for_collision(self.player, self.npc):
            if not self.dialog_active:
                self.dialog_active = True
                self.dialog_page = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_speed_y = PLAYER_SPEED
        elif key == arcade.key.DOWN:
            self.player_speed_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player_speed_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player_speed_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player_speed_y = 0
        elif key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player_speed_x = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if self.dialog_active and button == arcade.MOUSE_BUTTON_LEFT:
            if self.dialog_page < len(self.dialog_texts) - 1:
                self.dialog_page += 1
            else:
                self.dialog_active = False

if __name__ == "__main__":
    game = MyGame()
    arcade.run()

