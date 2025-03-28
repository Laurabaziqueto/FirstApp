import flet as ft

def main(page: ft.Page):
    # configaração da pagína
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK OU LIGHT
    page.window.width = 375
    page.window.height = 667


    # Definição de funções
    def mostrar_par_impar(e):
        txt_resultado.value = input_numero1.value
        num = int(input_numero1.value)
        resultado = num % 2
        if resultado == 0:
            txt_resultado.value = 'Par'
        else:
            txt_resultado.value = f'Impar'
        page.update()


    # Criaçãode componentes
    input_numero1 = ft.TextField(label="Número", hint_text="Digite um número: ")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_par_impar,
    )
    txt_resultado = ft.Text(value="")



    # Construir o layout
    page.add(
        ft.Column(
            [
                input_numero1,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)
