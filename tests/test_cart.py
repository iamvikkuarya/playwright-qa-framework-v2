from playwright.sync_api import Page, expect

def test_cart(logged_in_page:Page):
    logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack").get_by_role("button").click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")