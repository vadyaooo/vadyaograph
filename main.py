import flet as ft


def main(page: ft.Page):
    u_la = ft.Text('Info')

    def prov(e):
        u_la.value = 'Yes'
        page.update()

    def man(page1: ft.Page):
        page1.title = 'efe'
        page1.bgcolor = 'green'
        page1.add(
            ft.Row([
                ft.Te
            ])
            ft.Row(
                [
                    ft.IconButton(ft.icons.HOME, on_click=prov)
                ]
            )
        )

    def ontablo(e):


    page.add(
        ft.Row(
            [
                u_la
            ]
        ),
        ft.Row([
            ft.OutlinedButton(text="Показать табло", on_click=ontablo)
        ])
    )
    # ft.app(port=8550, target=man, view=ft.AppView.WEB_BROWSER)
    ft.app(target=man)


ft.app(target=main)
