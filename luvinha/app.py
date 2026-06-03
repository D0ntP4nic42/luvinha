from textual.app import App

from luvinha.screens.main_menu import MainMenu


class LuvinhaApp(App[None]):
    """The Luvinha word puzzle game."""

    TITLE = "Luvinha"
    CSS_PATH = "styles.tcss"

    SCREENS = {"main_menu": MainMenu}

    def on_mount(self) -> None:
        self.push_screen("main_menu")