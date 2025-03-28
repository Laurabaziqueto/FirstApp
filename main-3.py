import flet as ft

def main(page: ft.Page):
    # configaração da pagína
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK OU LIGHT
    page.window.width = 375
    page.window.height = 667


    # Definição de funções

    def somar(e):
        soma = int(input_numero1.value) + int(input_numero2.value)
        txt_resultado.value = f"{soma}"
        page.update()

    def subtrair(e):
        subtracao = int(input_numero1.value) - int(input_numero2.value)
        txt_resultado.value = f"{subtracao}"
        page.update()

    def multiplicar(e):
        mutiplicacao = int(input_numero1.value) * int(input_numero2.value)
        txt_resultado.value = f"{mutiplicacao}"
        page.update()

    def dividir(e):
        divisao = int(input_numero1.value) / int(input_numero2.value)
        txt_resultado.value = f"{divisao}"
        page.update()

    # Criaçãode componentes
    input_numero1 = ft.TextField(label="Número", hint_text="Digite um número: ")
    input_numero2 = ft.TextField(label="Número", hint_text="Digite um número: ")
    btn_enviar1 = ft.FilledButton(
        text="Somar",
        width=page.window.width,
        on_click=somar,
    )
    txt_resultado = ft.Text(value="")

    btn_enviar2 = ft.FilledButton(
        text="Subtrair",
        width=page.window.width,
        on_click=subtrair,
    )

    btn_enviar3 = ft.FilledButton(
        text="Multiplicar",
        width=page.window.width,
        on_click=multiplicar,
    )
    btn_enviar4 = ft.FilledButton(
        text="Dividir",
        width=page.window.width,
        on_click=dividir,
    )





    # Construir o layout
    page.add(
        ft.Column(
            [
                input_numero1,
                input_numero2,
                btn_enviar1,
                btn_enviar2,
                btn_enviar3,
                btn_enviar4,
                txt_resultado,
            ]
        )
    )


ft.app(main)
