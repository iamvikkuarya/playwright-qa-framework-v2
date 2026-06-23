from playwright.sync_api import Page,expect

def test_locked_out_user(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Sorry, this user has been locked out.")).to_be_visible()

def test_sort_functionality(logged_in_page:Page):
    logged_in_page.locator("[data-test='product-sort-container']").select_option("lohi")
    expect(logged_in_page.locator("[data-test='active-option']")).to_have_text("Price (low to high)")

def test_2products_incart(logged_in_page:Page):
    logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack").get_by_role("button").click()
    logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Bike Light").get_by_role("button").click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("2")

def test_addtocart_button(logged_in_page:Page):
    logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack").get_by_role("button").click()
    expect(logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack").get_by_role("button")).to_have_text("Remove")