from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Pulsante per andare alla schermata successiva
        button = Button(text="Vai alla schermata 2")
        button.bind(on_press=lambda x: self.manager.current == "second_screen")  # Cambiato per confronto
        layout.add_widget(button)

        self.add_widget(layout)


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Pulsante per tornare alla schermata principale
        button = Button(text="Torna alla schermata principale")
        button.bind(on_press=lambda x: self.manager.current == "home_screen")


class PokemonApp(App):
    def build(self):
        screemanager = ScreenManager()
        screemanager.add_widget(HomeScreen(name="home_screen"))
        screemanager.add_widget(SecondScreen(name="second_screen"))
        Window.size = (360, 640)

        return screemanager


if __name__ == "__main__":
    PokemonApp().run()
