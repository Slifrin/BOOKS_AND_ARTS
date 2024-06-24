import flet as ft


blue_global_counter = 0
green_global_counter = 0

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    print(page.session.get_keys())

    if not page.session.get("blue"):
        page.session.set("blue", "0")
    if not page.session.get("green"):
        page.session.set("green", "0")

    print(page.session.get_keys())

    headline = ft.Text("Vote for color", size=30, weight=ft.FontWeight.BOLD)
    blue = ft.Text(page.session.get("blue"), size=30, weight=ft.FontWeight.BOLD)
    green = ft.Text(page.session.get("green"), size=30, weight=ft.FontWeight.BOLD)

    def vote_for_blue(e):
        page.pubsub.send_all("vote_for_blue")

    def vote_for_green(e):
        page.pubsub.send_all("vote_for_green")

    def listener(result):
        print(f"{id(page)} {page.session_id} {blue.value=} {green.value=} {page.session.get_keys()} {page.session.get("blue")=} {page.session.get("green")} {blue_global_counter=} {green_global_counter=}")

        if result == "vote_for_blue":
            blue.value = str(int(page.session.get("blue")) + 1)
            page.session.set("blue", blue.value)

        elif result == "vote_for_green":
            green.value = str(int(page.session.get("green")) + 1)
            page.session.set("green", green.value)

        page.update()

    page.pubsub.subscribe(listener)

    page.add(
        ft.Column(
            [
                ft.Row(
                    [headline],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Container(
                            bgcolor=ft.colors.BLUE,
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Text("BLUE", size=30, weight=ft.FontWeight.BOLD),
                                    blue,
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=150,
                        ),
                        ft.Container(
                            bgcolor=ft.colors.GREEN,
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Text(
                                        "GREEN", size=30, weight=ft.FontWeight.BOLD,
                                    ),
                                    green,
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                            width=150,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                # Row with buttons
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Vote for BLUE",
                            bgcolor=ft.colors.BLUE,
                            color=ft.colors.WHITE,
                            on_click=vote_for_blue,
                            width=150,
                        ),
                        ft.ElevatedButton(
                            "Vote for GREEN",
                            bgcolor=ft.colors.GREEN,
                            color=ft.colors.WHITE,
                            on_click=vote_for_green,
                            width=150,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],  # type: ignore
        )
    )


ft.app(target=main)
