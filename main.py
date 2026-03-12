import flet as ft

def main(page : ft.Page):
    page.theme_mode=ft.ThemeMode.LIGHT
    page.title="Inicio de sesion"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.scroll = "auto"
    
    page.add(ft.Text(value="Inicio Sesion", weight=ft.FontWeight.BOLD, size=25))
    
    
    email = ft.TextField(
        label="Email",
        hint_text="Escriba su correo electronico",
        value="",
        autofocus=True,
        suffix_icon=(ft.Icon(ft.Icons.PERSON, color=ft.Colors.PRIMARY, size=25)),
        weight = 16
    )
    password = ft.TextField(
        label="Contraseña",
        hint_text="Escriba su contraseña",
        value="",
        password=True

    )
    page.add(ft.Column(
        width=220,
        spacing=12,
        controls=[
            ft.Icon(ft.Icons.LOGIN, color=ft.Colors.PRIMARY, size=100),
            email,
            password,
        ],
    ))
    page.add(ft.Button(content="Iniciar sesion"))

    
ft.run(main)