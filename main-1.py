import flet as ft

def main(page: ft.Page):
    # configaração da pagína
    page.title = "Minha Aplicação Flet"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK OU LIGHT
    page.window.width = 375
    page.window.height = 667


    # Definição de funções
    def mostrar_nome(e):
        txt_resultado.value = f'{input_nome.value} {input_sobrenome.value}'
        page.update()


    # Criação de componentes
    input_nome = ft.TextField(label="Nome", hint_text="Digite seu nome: ")
    input_sobrenome = ft.TextField(label="Sobrenome", hint_text="Digite seu Sobrenome: ")
    btn_enviar = ft.FilledButton(
        text="Enviar",
        width=page.window.width,
        on_click=mostrar_nome,
    )
    txt_resultado = ft.Text(value="")


    # Construir o layout
    page.add(
        ft.Column(
            [
                input_nome,
                input_sobrenome,
                btn_enviar,
                txt_resultado,
            ]
        )
    )


ft.app(main)
