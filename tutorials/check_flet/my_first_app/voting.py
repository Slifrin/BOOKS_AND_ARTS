import flet as ft


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    headline = ft.Text("Vote for color", size=30, weight=ft.FontWeight.BOLD)
    blue = ft.Text("0", size=30, weight=ft.FontWeight.BOLD)
    green = ft.Text("0", size=30, weight=ft.FontWeight.BOLD)

    def vote_for_blue(e):
        page.pubsub.send_all("vote_for_blue")
        page.update()

    def vote_for_green(e):
        page.pubsub.send_all("vote_for_green")
        page.update()

    def listener(result):
        print(f"{page.session_id}   ")
        if result == "vote_for_blue":
            blue.value = str(int(blue.value) + 1)
        elif result == "vote_for_green":
            green.value = str(int(green.value) + 1)
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
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                            width=150,
                        ),
                        ft.Container(
                            bgcolor=ft.colors.GREEN,
                            padding=20,
                            content=ft.Column(
                                [
                                    ft.Text(
                                        "GREEN",
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    green,
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
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
