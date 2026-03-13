import flet as ft

def main(page : ft.Page):
    page.title="Inicio de sesion"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.padding=30
    page.bgcolor = "#464646"
    USUARIO_VALIDO="admin"
    CONTRASEñA_VALIDA = "123456"
    
    def login_click(e):
        usuario = txt_usuario.value
        contrasena = password.value
        
        if usuario == USUARIO_VALIDO and contrasena == CONTRASEñA_VALIDA:
            page.show_dialog(ft.SnackBar(ft.Text("Inicio de sesion exitoso.")))
            mostrar_pantalla_principal()
        else:
            page.show_dialog(ft.SnackBar(ft.Text("Usuario o contraseña erronea.")))
        
    def forgot_click(e):
        page.show_dialog(ft.SnackBar(ft.Text("Se han enviado instrucciones a tu correo.")))
    
    txt_usuario = ft.TextField(
        label="Nombre usuario",
        hint_text="Escriba su usuario",
        value="",
        autofocus=True,
        color = ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        hint_style=ft.TextStyle(color=ft.Colors.WHITE),
        suffix_icon=(ft.Icon(ft.Icons.PERSON, color=ft.Colors.GREEN, size=25)),
        height = 50,
        can_reveal_password=True
    )
    password = ft.TextField(
        label="Contraseña",
        hint_text="Escriba su contraseña",
        value="",
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
        hint_style=ft.TextStyle(color=ft.Colors.WHITE),
        border_color=ft.Colors.WHITE,
        suffix_icon=(ft.Icon(ft.Icons.PASSWORD, color=ft.Colors.GREEN, size=25)),
        password=True

    )
    btn_login = ft.Button(content="Iniciar sesion", on_click=login_click, bgcolor = ft.Colors.GREEN_400, color = ft.Colors.WHITE)

    link_forgot = ft.TextButton(
        "Olvidaste tu constraseña?",
        on_click=forgot_click,
    )
    
    page.add(
        ft.Column(
            width=220,
            spacing=12,
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(value="Inicio de sesion", weight=ft.FontWeight.BOLD, size=25, color=ft.Colors.WHITE),
                ft.Icon(ft.Icons.FACE, color=ft.Colors.WHITE, size=100),
                txt_usuario,
                password,
                btn_login,
                link_forgot
                ],
            )
        )
    def mostrar_pantalla_principal():
        page.clean()
            
        page.navigation_bar=ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
                ft.NavigationBarDestination(icon=ft.Icons.INFO, label="Informacion"),
                ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Inicio de sesion"),
            ],
            on_change = lambda e: print(f"Seleccionado: {e.control.selected_index}")
        )
        
        page.add(
            ft.AppBar(
                title=ft.Text("Panel principal"),
                bgcolor=ft.Colors.BLUE_900,
                color=ft.Colors.WHITE,
                automatically_imply_leading=False
            ),
            ft.Column(
                [
                    ft.Icon(ft.Icons.BOLT, color=ft.Colors.YELLOW, size=100),
                    ft.Text("Bienvenido al sistema.", color=ft.Colors.WHITE),
                    ft.Text("Has iniciado sesion correctamente.", color=ft.Colors.WHITE)
                ],
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()
        
    ##page.add(layout_login)

    
ft.run(main)