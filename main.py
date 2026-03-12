import flet as ft

def main(page : ft.Page):
    page.title="Inicio de sesion"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.padding=30
    page.bgcolor = '#9DCCFF'
    USUARIO_VALIDO="admin"
    CONTRASEñA_VALIDA = "123456"
    
    def login_click(e):
        usuario = txt_usuario.value
        contrasena = password.value
        
        if usuario == USUARIO_VALIDO and contrasena == CONTRASEñA_VALIDA:
            page.show_dialog(ft.SnackBar(ft.Text("Inicio de sesion exitoso.")))
        else:
            page.show_dialog(ft.SnackBar(ft.Text("Usuario o contraseña erronea.")))
        
    def forgot_click(e):
        page.show_dialog(ft.SnackBar(ft.Text("Se han enviado instrucciones a tu correo.")))
    
    txt_usuario = ft.TextField(
        label="Nombre usuario",
        hint_text="Escriba su usuario",
        value="",
        autofocus=True,
        suffix_icon=(ft.Icon(ft.Icons.PERSON, color=ft.Colors.PRIMARY, size=25)),
        height = 50
    )
    password = ft.TextField(
        label="Contraseña",
        hint_text="Escriba su contraseña",
        value="",
        suffix_icon=(ft.Icon(ft.Icons.PASSWORD, color=ft.Colors.PRIMARY, size=25)),
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
                ft.Text(value="Inicio Sesion", weight=ft.FontWeight.BOLD, size=25),
                ft.Icon(ft.Icons.LOGIN, color=ft.Colors.PRIMARY, size=100),
                txt_usuario,
                password,
                btn_login,
                link_forgot
                ],
            )
        )
    
ft.run(main)