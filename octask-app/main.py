import flet as ft


def pageSetup(page: ft.Page):
    # setup basic stuff
    page.title = "Octask"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # events
    page.on_resized = on_resize(page=page)
    # global ui
    bs = ft.BottomSheet(
        ft.Container(
            ft.Column(
                [
                    ft.Text("Commands"),
                    ft.ElevatedButton("Dismiss", on_click=lambda _: page.close(bs)),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
            ),
            width=500,
            height=500,
            margin=ft.margin.only(top=20),
        ),
        open=False,
    )

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=lambda e: page.open(bs)
    )
    page.update()


def breakpoint(page: ft.Page):
    w = page.window.width if page.window.width else 1000
    if w < 600:
        return "xs"
    elif w < 900:
        return "sm"
    elif w < 1200:
        return "md"
    else:
        return "lg"


def on_resize(page: ft.Page):
    bp = breakpoint(page)
    match bp:
        case "xs":
            pass  # set content size
        case "sm":
            pass
        case "md":
            pass
        case "lg":
            pass

    page.update()


def main(page: ft.Page):
    pageSetup(page)


if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
