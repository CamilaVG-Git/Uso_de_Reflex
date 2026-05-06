import reflex as rx

class State(rx.State):
    texto = "Haz clic en el botón"

    def cambiar(self):
        self.texto = "¡Bienvenido! Has hecho clic, muchas gracias :D"


def index():
    return rx.center(
        rx.vstack(
            rx.heading("Hola mundo", size="8"),
            rx.text("Bienvenido a mi aplicación creada con Reflex"),
            rx.text(State.texto),
            rx.button("Haz clic aquí", on_click=State.cambiar),
            spacing="5",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)