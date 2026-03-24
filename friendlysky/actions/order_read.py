def get_order_summary(page):

    summary = page.locator(
        "ordersummary"
    )

    summary.wait_for()

    return summary.inner_text()