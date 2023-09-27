import os
import flet


def main(page: flet.Page):
    page.add(flet.Text(value="Hello World!"))


if __name__ == "__main__":
    flet.app(
        target=main, 
        port=os.getenv("PORT", "7860"),
        view=flet.AppView.WEB_BROWSER
    )
