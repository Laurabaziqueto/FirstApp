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
                    AppBar(title=Text("Cadastro de Livros"), bgcolor=Colors.PRIMARY),
                    input_titulo,
                    input_descricao,
                    input_categaria,
                    input_autor,

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
                        Text(value= f'O titulo do livro é {input_titulo.value}.'),
                        Text(value= f'Descrição do livro: {input_descricao.value}.'),
                        Text(value= f'Qual é a categoria desse livro? {input_categaria.value}.'),
                        Text(value= f'Nome do autor: {input_autor.value}.')
                    ],
                )
            )

        page.update()

    input_titulo = ft.TextField(label="Titulo", hint_text="Qual é o titulo do livro? ")
    input_descricao = ft.TextField(label="Descrição", hint_text="Digite a descrição do livro: ")
    input_categaria = ft.TextField(label="Categoria", hint_text="Qual é o categoria desse livro:? ")
    input_autor = ft.TextField(label="Autor", hint_text="Digite o autor do livro: ")

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)



