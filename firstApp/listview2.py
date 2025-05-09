import flet as ft
from django.template.defaultfilters import title
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.snack_bar import SnackBar



class user():
    def __init__(self, titulo, descricao, categoria, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.autor = autor

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções
    lista = []
    def salvar_titulo(e):
        if input_titulo.value == "":
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()

        else:
            obj_livro = user(
                titulo=input_titulo.value,
                descricao=input_descricao.value,
                categoria=input_categoria.value,
                autor=input_autor.value,
            )
            lista.append(obj_livro)
            input_titulo.value = ""
            input_descricao.value = ""
            input_categoria.value = ""
            input_autor.value = ""
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def exibir_lista(e):
        lv_nome.controls.clear()
        for livro in lista:
            lv_nome.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(f"Titulo - {livro.titulo}"),
                    subtitle=ft.Text(f"Autor - {livro.autor}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MODE_ROUNDED,
                        on_open=lambda _: exibir_detalhes(livro.titulo, livro.autor, livro.categoria, livro.descricao),
                    )
                )
            )
        page.update()

    def exibir_detalhes(titulo, autor, categoria, descricao):



    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Biblioteca"), bgcolor=Colors.PRIMARY_CONTAINER),
                    input_titulo,
                    input_autor,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_titulo(e)
                    ),
                    ft.Button(
                        text="Exibir lista",
                        on_click=lambda _: page.go("/segunda"),
                    )
                ],
            )
        )
        if page.route == "/segunda" or page.route == "/terceira":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_nome,+


                    ],
                )
            )
        if page.route == "/terceira":
            exibir_detalhes(e)
            page.views.append(
                View(
                    "/terceira",
                    [
                    AppBar(title=Text("terceira tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        input_descricao,
                        input_categoria,

                    ],
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes
    msg_sucesso = SnackBar(
        content=ft.Text("Nome salvo com sucesso!"),
        bgcolor=Colors.GREEN
    )
    msg_error = SnackBar(
            content=ft.Text("ERROR!"),
            bgcolor=Colors.RED
        )
    input_titulo = ft.TextField(label="Título")
    input_descricao = ft.TextField(label="Descrição")
    input_categoria = ft.TextField(label="Categoria")
    input_autor = ft.TextField(label="Autor")

    lv_nome = ft.ListView(
        height=500)

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)

