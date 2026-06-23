from playwright.sync_api import Page, expect

def test_login(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_invalid_password(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret")
    page.get_by_role("button", name="Login").click()
    expect(page.locator("[data-test='error']")).to_be_visible()

def test_login_without_credentials(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Username is required")).to_be_visible()
