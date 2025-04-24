import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from flet.core.dropdown import Option
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
                    AppBar(title=Text("Simulador de Aposentadoria"), bgcolor=Colors.PRIMARY),
                    ElevatedButton(text="Simulador", on_click=lambda _: page.go("/simulador")),
                    ElevatedButton(text="Regras", on_click=lambda _: page.go("/regras"))
                ],
            )
        )
        if page.route == "/simulador":
            page.views.append(
                View(
                    "/simulador",
                    [
                        AppBar(title=Text("Simulador"), bgcolor=Colors.PRIMARY),
                        Text(value= f'BEM VINDO AO SIMULADOR DE APOSENTADORIA!\n '),
                        input_idade_atual,
                        menu,
                        input_tempo_contribuicao,
                        input_media_salarial,
                        categoria

                    ],
                )
            )

        if page.route == "/regras":
            page.views.append(
                View(
                    "/regras",
                    [
                        AppBar(title=Text("Regras"), bgcolor=Colors.PRIMARY),
                        Text(value= f'REGRAS BÁSICAS DE APOSENTADORIA!\n'),
                        Text(value= f' Aposentadoria por idade:'),
                        Text(value= f'   Homens: 65 anos de idade e pelo menos 15 anos de contribuição.'),
                        Text(value= f'   Mulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n '),
                        Text(value=f' Aposentadoria por tempo de contribuição:'),
                        Text(value=f'   Homens: 35 anos de contribuição. '),
                        Text(value=f'   Mulheres: 30 anos de contribuição.\n '),
                        Text(value=f' Valor Estimado do Benefício: : O valor da aposentadoria será uma média de 60% da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo de contribuição. '),
                    ],
                )
            )

        page.update()

    input_idade_atual = ft.TextField(label="Idade atual", hint_text="Idade: ")
    menu = ft.Dropdown(
        label="Menu",
        width=page.window.width,
        fill_color=Colors.PINK,
        options=[Option(key="Masc", text="Masculino"), Option(key="Fem", text="Femenino")],
    )
    input_tempo_contribuicao = ft.TextField(label="Quanto tempo de contribuição?", hint_text="Tempo de contribuição: ")
    input_media_salarial = ft.TextField(label="Qual é a media salarial?", hint_text="Media salarial: ")
    categoria = ft.Dropdown(
        label="Categoria de Aposentadoria",
        width=page.window.width,
        fill_color=Colors.PINK,
        options=[Option(key="cat", text="Aposentadoria por tempo de contribuição"),
                 Option(key="Idade", text="Aposentadoria por idade"),],
    )

    def mostrar_idade(input_idade_atual,menu):
        print('')



    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)


