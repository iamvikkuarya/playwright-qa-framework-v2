import pytest
from playwright.sync_api import Page, expect

@pytest.mark.parametrize("username,password", [
    ("wrong_user", "wrong_secret"),
    ("user1", "secret1"),
    ("wrong_user", "secret"),
])
def test_invalid_credentials(page:Page,username:str,password:str):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Epic sadface: Username and password do not match")).to_be_visible()
    

@pytest.mark.parametrize("sorttype", [
    ("az"),
    ("za"),
    ("lohi"),
    ("hilo"),
])
def test_sort(logged_in_page:Page,sorttype:str):
    logged_in_page.locator("[data-test='product-sort-container']").select_option(sorttype)
    expect(logged_in_page.locator("[data-test='product-sort-container']")).to_have_value(sorttype)


@pytest.mark.parametrize("username,password", [
    ("standard_user","secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user","secret_sauce")
])
def test_users(page:Page,username:str,password:str):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


@pytest.mark.parametrize("products", [
    ("Sauce Labs Backpack"),
    ("Sauce Labs Bike Light"),
    ("Sauce Labs Bolt T-Shirt")
])
def test_products(logged_in_page:Page,products:str):
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
    logged_in_page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack").get_by_role("button").click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")


@pytest.mark.parametrize("username,password,login_errors", [
    ("","","Epic sadface: Username is required"),
    ("standard_user","","Epic sadface: Password is required"),
    ("locked_out_user","secret_sauce","Epic sadface: Sorry, this user has been locked out.")
])
def test_login_errors(page:Page,username:str,password:str,login_errors:str):
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text(login_errors)).to_be_visible()