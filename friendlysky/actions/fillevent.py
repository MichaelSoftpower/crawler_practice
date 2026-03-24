
def fill_event(page):

    title_input = page.locator(
        "input[placeholder='title']"
    )

    title_input.wait_for()

    title_input.fill(
        "First Parth 2026"
    )
