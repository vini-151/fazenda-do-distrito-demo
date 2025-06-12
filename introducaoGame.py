import arcade

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 1024
SCREEN_TITLE = "Fazendinha no Distrito"

class TelaInicio(arcade.View):

    def __init__(self):
        super().__init__()

        self.sprite_list = arcade.SpriteList()

        # Cria sprite de fundo
        self.background_sprite = arcade.Sprite("titulo.png", scale=0.5)
        self.background_sprite.center_x = SCREEN_WIDTH / 2
        self.background_sprite.center_y = SCREEN_HEIGHT / 2
        self.sprite_list.append(self.background_sprite)


        # parametros do botao 
        self.botao_x = SCREEN_WIDTH / 2
        self.botao_y = SCREEN_HEIGHT / 2 - 218
        self.botao_largura = 404
        self.botao_altura = 126

        


    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    

    def on_draw(self):
        self.clear()
        self.sprite_list.draw() 

        # Desenha o botão
        arcade.draw_rect_filled(arcade.rect.XYWH(self.botao_x, self.botao_y, self.botao_largura, self.botao_altura), arcade.color.YELLOW)
        arcade.draw_text("JOGAR", self.botao_x, self.botao_y, arcade.color.BLACK, 24, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.botao_x - self.botao_largura / 2 < x < self.botao_x + self.botao_largura / 2 and
            self.botao_y - self.botao_altura / 2 < y < self.botao_y + self.botao_altura / 2):
            self.window.show_view(TelaTeclas())




class TelaTeclas(arcade.View):

    def __init__(self):
        super().__init__()
        self.sprite_list = arcade.SpriteList()

        # Cria sprite de fundo
        self.background_sprite = arcade.Sprite("teclas.png", scale=1)
        self.background_sprite.center_x = SCREEN_WIDTH / 2
        self.background_sprite.center_y = SCREEN_HEIGHT / 2
        self.sprite_list.append(self.background_sprite)

        #parâmetros do botão
        self.botao_x = SCREEN_WIDTH / 2
        self.botao_y = SCREEN_HEIGHT / 2 - 260
        self.botao_largura = 404
        self.botao_altura = 80

        


    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    

    def on_draw(self):
        self.clear()
        self.sprite_list.draw() 

        # Desenha o botão
        arcade.draw_rect_filled(arcade.rect.XYWH(self.botao_x, self.botao_y, self.botao_largura, self.botao_altura), arcade.color.YELLOW)
        arcade.draw_text("Continuar", self.botao_x, self.botao_y, arcade.color.BLACK, 24, anchor_x="center", anchor_y="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.botao_x - self.botao_largura / 2 < x < self.botao_x + self.botao_largura / 2 and
            self.botao_y - self.botao_altura / 2 < y < self.botao_y + self.botao_altura / 2):
            self.window.show_view(TelaHistoriaUm())






class TelaHistoriaUm(arcade.View):

    def __init__(self):
        super().__init__()

        self.sprite_list = arcade.SpriteList()

        # o sprite de fundo
        self.background_sprite = arcade.Sprite("historia1.png", scale=1)
        self.background_sprite.center_x = SCREEN_WIDTH / 2
        self.background_sprite.center_y = SCREEN_HEIGHT / 2
        self.sprite_list.append(self.background_sprite)

        #parâmetros do botão
        self.botao_x = SCREEN_WIDTH / 2
        self.botao_y = SCREEN_HEIGHT / 2 - 218
        self.botao_largura = 404
        self.botao_altura = 126

        


    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()  

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(TelaHistoriaDois())









class TelaHistoriaDois(arcade.View):

    def __init__(self):
        super().__init__()

        self.sprite_list = arcade.SpriteList()

        # Cria sprite de fundo
        self.background_sprite = arcade.Sprite("historia2.png", scale=1)
        self.background_sprite.center_x = SCREEN_WIDTH / 2
        self.background_sprite.center_y = SCREEN_HEIGHT / 2
        self.sprite_list.append(self.background_sprite)

        #parâmetros do botão
        self.botao_x = SCREEN_WIDTH / 2
        self.botao_y = SCREEN_HEIGHT / 2 - 218
        self.botao_largura = 404
        self.botao_altura = 126

        


    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw() 

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(TelaHistoriaTres())












class TelaHistoriaTres(arcade.View):

    def __init__(self):
        super().__init__()

        self.sprite_list = arcade.SpriteList()

        # sprite de fundo
        self.background_sprite = arcade.Sprite("historia3.png", scale=1)
        self.background_sprite.center_x = SCREEN_WIDTH / 2
        self.background_sprite.center_y = SCREEN_HEIGHT / 2
        self.sprite_list.append(self.background_sprite)


        #parâmetros do botão
        self.botao_x = SCREEN_WIDTH / 2
        self.botao_y = SCREEN_HEIGHT / 2 - 218
        self.botao_largura = 404
        self.botao_altura = 126


    def on_show(self):
        arcade.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

    def on_draw(self):
        self.clear()
        self.sprite_list.draw() 

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            self.window.show_view(TelaJogo())














class TelaJogo(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_BLUE_GRAY)

    def on_draw(self):
        self.clear()
        arcade.draw_text("Jogo iniciado", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=25, anchor_x="center")
        



def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.show_view(TelaInicio())
    arcade.run()

if __name__ == "__main__":
    main()
