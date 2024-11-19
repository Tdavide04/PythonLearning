from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

class ImageButton(ButtonBehavior, Image):
    pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Pulsante immagine per andare alla schermata successiva
        image_button = ImageButton(
            source="./images/logo_pokeball.webp",
            size_hint=(0.13, 0.13), 
            pos_hint={"center_x": 0.6, "top": 0.97}  
        )
        image_button.bind(on_press=lambda x: setattr(self.manager, 'current', "second_screen"))
        layout.add_widget(image_button)

        self.add_widget(layout)

class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Pulsante per tornare alla schermata principale
        button = Button(
            text="Torna alla schermata principale",
            size_hint=(0.6, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        button.bind(on_press=lambda x: setattr(self.manager, 'current', "home_screen"))
        layout.add_widget(button)

        self.add_widget(layout)

class PokemonApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name="home_screen"))
        screen_manager.add_widget(SecondScreen(name="second_screen"))
        Window.size = (360, 640)

        return screen_manager

if __name__ == "__main__":
    PokemonApp().run()
