from textual.app import ComposeResult
from textual.containers import Center, Middle, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Label


class HowToPlay(ModalScreen[None]):
    """Modal explaining how to play."""

    BINDINGS = [("escape", "close", "Close")]

    def compose(self) -> ComposeResult:
        with Center():
            with Middle():
                with Vertical(id="how-to-play-dialog"):
                    yield Label("How to Play")
                    yield Label(
                        "Coming soon!"
                    )
                    yield Button("Got it!", id="close-btn", variant="primary")

    def action_close(self) -> None:
        self.dismiss(None)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "close-btn":
            self.dismiss(None)