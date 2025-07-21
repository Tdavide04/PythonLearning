from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

class ImageButton(ButtonBehavior, Image):
    pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Crea il layout principale
        layout = FloatLayout()

        # Pulsante immagine per andare alla schermata successiva
        image_button = ImageButton(
            source="./images/logo_pokeball.webp",
            size_hint=(0.13, 0.13),
            pos_hint={"center_x": 0.6, "top": 0.97}
        )
        image_button.bind(on_press=lambda x: setattr(self.manager, 'current', "second_screen"))
        layout.add_widget(image_button)

        # Crea lo ScrollView
        scroll_view = ScrollView(size_hint=(1, None), height=Window.height - 100)  # Spazio per il bottone immagine

        # Crea il GridLayout che contiene le celle
        grid_layout = GridLayout(cols=1, size_hint_y=None)
        grid_layout.bind(minimum_height=grid_layout.setter('height'))

        # Elenco delle immagini
        images = [
            "./images/Bulbasaur.png",  # Immagine 1
            "./images/Ivysaur.png",  # Immagine 2
            "./images/Venusaur.png",  # Immagine 3
            "./images/Squirtle.png",  # Immagine 4
            "./images/Wartortle.png",  # Immagine 5
            "./images/Blastoise.png"   # Immagine 6
        ]

        for img_path in images:
            # Crea il bottone per ogni immagine
            button = Button(size_hint_y=None, height=60, width=Window.width)

            # Crea l'immagine per il bottone
            image = Image(
                source=img_path,  # Percorso dell'immagine
                size_hint=(None, 1),  # Impostare width=40 per la larghezza
                width=40  # Larghezza dell'immagine
            )

            # Aggiungi l'immagine al bottone
            button.add_widget(image)

            # Aggiungi il bottone al GridLayout
            grid_layout.add_widget(button)

        # Aggiungi il GridLayout allo ScrollView
        scroll_view.add_widget(grid_layout)

        # Aggiungi lo ScrollView al layout principale
        layout.add_widget(scroll_view)

        # Aggiungi il layout alla schermata
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
