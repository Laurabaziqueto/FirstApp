import flet as ft
from flet import ElevatedButton, Text, View, TextField, Dropdown, dropdown, Column, Container, alignment, CrossAxisAlignment, Row
from flet.core.app_bar import AppBar
from flet.core.border_radius import horizontal

from flet.core.colors import Colors


def main(page: ft.Page):
    page.title = "Simulador de Aposentadoria"
    page.bgcolor = "#FFFFF"
    page.window.width = 378
    page.window.height = 667



    input_idade = TextField(label="", width=320, hint_text="Idade", color="Black",
                            hint_style=ft.TextStyle(color="BLACK"))
    input_tempo_contribuicao = TextField(label="", width=320, hint_text="Tempo de Contribuição (anos)", color="BLACK",
                                         hint_style=ft.TextStyle(color="BLACK"))
    input_media_salarial = TextField(label="", width=320, hint_text="Média Salarial", color="BLACK",
                                     hint_style=ft.TextStyle(color="BLACK"))
    input_genero = Dropdown(
        label="",
        hint_text="Gênero",
        options=[dropdown.Option("Masculino"), dropdown.Option("Feminino")],
        width=320,
        color="black",
        hint_style=ft.TextStyle(color="black")
    )
    input_categoria = Dropdown(
        label="",
        hint_text="Categoria de Aposentadoria",
        options=[
            dropdown.Option("Idade"),
            dropdown.Option("Tempo de Contribuição")
        ],

        width=320,
        color="black",
        hint_style=ft.TextStyle(color="black")
    )

    resultado_texto = Text("", size=16, color="BLACK")
    erro_texto = Text("", size=14, color=Colors.RED)

    def navegar_para_simulacao(e):
        from flet.core.types import MainAxisAlignment
        page.views.append(
            View(
                "/simulacao",
                bgcolor="WHITE",
                appbar=AppBar(
                    title=Text("Simulador de Aposentadoria", color="BLACK"),
                    bgcolor="#B6CAFC",
                    actions=[
                        ElevatedButton(
                            text="Voltar",
                            on_click=voltar,
                            bgcolor="#B6CAFC",
                            color="BLACK"
                        )
                    ]
                ),
                controls=[
                    ft.Container(
                        content=ft.Image(src="img.png", width=150, height=150),
                        alignment=alignment.center
                    ),
                    Row([
                        Container(
                            content=Column(
                                controls=[
                                    input_idade,
                                    input_genero,
                                    input_tempo_contribuicao,
                                    input_media_salarial,
                                    input_categoria,
                                    erro_texto,
                                    Container(
                                        content=ElevatedButton(
                                            text="RESULTADO",
                                            on_click=navegar_para_resultado,
                                            bgcolor="#D8D4D4",
                                            color="black",
                                            width=320,
                                            height=40,
                                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                                        ),
                                        alignment=alignment.center,
                                        padding=10
                                    ),

                                ],
                                horizontal_alignment=CrossAxisAlignment.CENTER
                            )
                        )
                    ])
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    def calcular_aposentadoria():
        try:
            idade = int(input_idade.value)
            tempo_contribuicao = int(input_tempo_contribuicao.value)
            media_salarial = float(input_media_salarial.value)
            genero = input_genero.value
            categoria = input_categoria.value
        except (ValueError, TypeError):
            resultado_texto.value = "Por favor, preencha todos os campos corretamente."
            return

        if tempo_contribuicao > idade:
            erro_texto.value = "Erro: O tempo de contribuição não pode ser maior que a idade."
            resultado_texto.value = ""
            return
        else:
            erro_texto.value = ""

        pode_aposentar = False
        anos_faltantes = 0

        if categoria == "Idade":
            if (genero == "Masculino" and idade >= 65 and tempo_contribuicao >= 15) or \
                    (genero == "Feminino" and idade >= 62 and tempo_contribuicao >= 15):
                pode_aposentar = True
            else:
                anos_faltantes = max(0, (65 if genero == "Masculino" else 62) - idade)
        elif categoria == "Tempo de Contribuição":
            if (genero == "Masculino" and tempo_contribuicao >= 35) or \
                    (genero == "Feminino" and tempo_contribuicao >= 30):
                pode_aposentar = True
            else:
                anos_faltantes = max(0, (35 if genero == "Masculino" else 30) - tempo_contribuicao)

        if pode_aposentar:
            tempo_excedente = max(0, tempo_contribuicao - (
                15 if categoria == "Idade" else (35 if genero == "Masculino" else 30)))
            valor_beneficio = media_salarial * (0.6 + (tempo_excedente * 0.02))
            resultado_texto.value = f"Você já pode se aposentar! Benefício estimado: R$ {valor_beneficio:.2f}"
        else:
            resultado_texto.value = f"Você ainda não pode se aposentar. Faltam {anos_faltantes} anos."

    def navegar_para_resultado(e):
        calcular_aposentadoria()
        page.views.append(
            View(
                "/resultado",
                bgcolor="#2F2F2F",
                appbar=AppBar(
                    title=Text("Resultado do Simulador", color="BLACK"),
                    bgcolor="#B6CAFC",
                    actions=[
                        ElevatedButton(
                            text="Voltar",
                            on_click=voltar,
                            bgcolor="#B6CAFC",
                            color="BLACK"
                        )
                    ],

                ),
                controls=[
                    Container(
                        content=Text("RESULTADO", size=18, color="BLACK"),

                    ),
                    Container(
                        content=resultado_texto,

                    ),
                    Container(
                        content=ElevatedButton(
                            text="Voltar",
                            on_click=voltar,
                            bgcolor="#B6CAFC",
                            color="black",
                            width=320,
                            height=40,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                        ),

                    )
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
            )
        )
        page.update()

    def navegar_para_regras(e):
        def texto3(texto):
            return Container(
                content=Text(texto, color="black"),
                bgcolor="white",

                border_radius=5,
                width=320
            )

        page.views.append(
            View(
                "/regras",
                appbar=AppBar(
                    title=Text("Regras de Aposentadoria", color="BLACK"),
                    bgcolor="#B6CAFC",
                    actions=[
                        ElevatedButton(
                            text="Voltar",
                            on_click=voltar,
                            bgcolor="#B6CAFC",
                            color="BLACK"
                        )
                    ]
                ),
                bgcolor="white",
                controls=[
                    Column(
                        controls=[
                            texto3(
                                "APOSENTADORIA POR IDADE (HOMENS)\n"
                                "65 anos de idade e pelo menos 15 anos de contribuição."),
                            texto3(
                                "APOSENTADORIA POR IDADE (MULHERES)\n"
                                "62 anos de idade e pelo menos 15 anos de contribuição."),
                            texto3("APOSENTADORIA POR TEMPO DE CONTRIBUIÇÃO (HOMENS)\n35 anos de contribuição."),
                            texto3("APOSENTADORIA POR TEMPO DE CONTRIBUIÇÃO (MULHERES)\n30 anos de contribuição."),
                            texto3("VALOR ESTIMADO DO BENEFÍCIO\n60% da média salarial, mais 2% por ano extra."),

                        ]
                    )
                ],
            )
        )
        page.update()

    def gerencia_rota(e):
        page.views.clear()

        page.views.append(
            View(
                "/",
                appbar=AppBar(
                    title=Text("", color="BLACK"),
                    bgcolor="#B6CAFC",
                ),
                controls=[
                    ft.Container(
                        width=page.window.width,
                        content=ft.Image(src="img.png", width=150, height=150),
                        alignment=alignment.center,
                    ),
                    Column(
                        [
                            ElevatedButton(
                                text="Simulador",
                                on_click=navegar_para_simulacao,
                                bgcolor="#D8D4D4",
                                color="BLACK",
                                width=150,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                            ),
                            ElevatedButton(
                                text="Regras",
                                on_click=navegar_para_regras,
                                bgcolor="#D8D4D4",
                                color="BLACK",
                                width=150,
                                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=20))
                            ),
                        ],
                        width=page.window.width,
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    )
                ]
            )
        )

        page.update()

    def voltar(e):
        if len(page.views) > 1:
            page.views.pop()
            page.update()

    page.on_route_change = gerencia_rota
    page.on_view_pop = voltar
    page.go(page.route)


ft.app(main)