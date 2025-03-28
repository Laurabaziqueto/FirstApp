import flet as ft
from flet import AppBar, Text, Page, View, colors
from flet.core import page
from flet.core.colors import Colors
from flet.core.elevated_button import ElevatedButton


def main(page: ft.Page):
    # configaração da pagína
    page.title = "Exemplos de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK OU LIGHT
    page.window.width = 375
    page.window.height = 667

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY),
                    input_nome,
                    ElevatedButton(text="Navegar", on_click=lambda _: page.go("/segunda"))
                ],
            )
        )
        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.PRIMARY),
                        Text(value= f'Bem vindo {input_nome.value}')
                    ],
                )
            )

        page.update()

    input_nome = ft.TextField(label="Nome", hint_text="Digite seu nome: ")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)




