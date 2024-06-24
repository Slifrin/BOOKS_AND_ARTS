import asyncio
import itertools
import math
import time
import random

import flet as ft
import flet.canvas as cv


class Countdown(ft.Text):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    def did_mount(self):
        self.running = True
        self.page.run_task(self.update_timer)

    def will_unmount(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:

            mins, secs = divmod(self.seconds, 60)
            self.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            await asyncio.sleep(1)
            self.seconds -= 1


def main(page: ft.Page):
    page.scroll = "adaptive"
    page.add(ft.Row(controls=[Countdown(120), Countdown(60)]))

    def element_clicked(e):
        print(e)
        if isinstance(e, ft.ControlEvent):
            page.add(ft.Text("Clicked"))

    c1 = ft.Container(
        ft.Text(
            "Hello",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        ),
        alignment=ft.alignment.center_left,
        border_radius=10,
        width=200,
        height=200,
        bgcolor=ft.colors.GREEN_400,
        on_click=element_clicked,
    )

    c2 = ft.Container(
        ft.Text("Bey!", size=50),
        alignment=ft.alignment.center_right,
        border_radius=10,
        width=200,
        height=200,
        bgcolor=ft.colors.YELLOW_700,
        on_click=element_clicked,
    )

    c = ft.AnimatedSwitcher(
        c1,
        transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,
    )

    def animate(e):
        print(e, type(e))
        c.content = c2 if c.content == c1 else c1
        c.update()

    page.add(c, ft.ElevatedButton("Animate!", on_click=animate))

    number_of_people = 6

    wheel = ft.Container(
        ft.Text(
            "Fortune wheel!",
            style=ft.TextThemeStyle.LABEL_LARGE,
            color=ft.colors.GREEN_ACCENT_400,
            rotate=ft.transform.Rotate(
                0,
                alignment=ft.alignment.center,
            ),
        ),
        alignment=ft.alignment.center,
        shape=ft.BoxShape.CIRCLE,
        height=300,
        border_radius=10,
        bgcolor=ft.colors.YELLOW_500,
        rotate=ft.transform.Rotate(
            math.pi / number_of_people,
            alignment=ft.alignment.center,
        ),
    )
    def wheel_animation(e):
        number_of_rotations = random.randint(60, 100)
        for i in range(number_of_rotations):
            wheel.rotate.angle += math.pi / number_of_people
            print(wheel.rotate.angle)
            page.update()
            time.sleep(0.05)

    wheel.on_click = wheel_animation


    page.bgcolor = ft.colors.WHITE10
    cp = cv.Canvas(
        [
            cv.Circle(100, 100, radius=200, paint=ft.Paint(color=ft.colors.BLUE_500)),
            cv.Text(100, 100, text="     Jurek", alignment=ft.alignment.center_left, rotate=math.pi * 2 * 0 / number_of_people),
            cv.Text(100, 100, text="     Jan", alignment=ft.alignment.center_left, rotate=math.pi * 2 * 1 / number_of_people),
            cv.Text(100, 100, text="     Bob", alignment=ft.alignment.center_left, rotate=math.pi * 2 * 2 / number_of_people),
            cv.Text(100, 100, text="     Tom", alignment=ft.alignment.center_left, rotate=math.pi * 2 * 3 / number_of_people),
        ],
        width=float("inf"),
        expand=True,
    )

    page.add(
        wheel,
        cp,
    )


ft.app(main)
