from __future__ import annotations

import os

import flet


def main(page: flet.Page):
    def add_clicked(event):
        page.add(flet.Checkbox(label=new_task.value))
        new_task.value = ""
        page.update()

    new_task = flet.TextField(value="What needs to be done?", expand=True)

    tasks_view = flet.Column()
    view = flet.Column(
        width=600,
        controls=[
            flet.Row(
                controls=[
                    new_task,
                    flet.FloatingActionButton(
                        icon=flet.icons.ADD,
                        on_click=add_clicked,
                    ),
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = flet.CrossAxisAlignment.CENTER
    page.add(view)


if __name__ == "__main__":
    flet.app(
        target=main,
        port=os.getenv("PORT", "7860"),
        view=flet.AppView.WEB_BROWSER,
    )
