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


@pytest.mark.parametrize("firstname,lastname,zipcode,error", [
    ("","Kumar","263139","Error: First Name is required"),
    ("Vivek","","263139","Error: Last Name is required"),
    ("Vivek","Kumar","","Error: Postal Code is required")
])
def test_checkout_user(logged_in_page:Page,firstname:str,lastname:str,zipcode:str,error:str):
    logged_in_page.goto("https://www.saucedemo.com/checkout-step-one.html")
    logged_in_page.get_by_placeholder("First Name").fill(firstname)
    logged_in_page.get_by_placeholder("Last Name").fill(lastname)
    logged_in_page.get_by_placeholder("Zip/Postal Code").fill(zipcode)
    logged_in_page.get_by_role("button", name="Continue").click()
    expect(logged_in_page.get_by_text(error)).to_be_visible()


@pytest.mark.parametrize("products", [
    ("Sauce Labs Backpack"),
    ("Sauce Labs Bike Light"),
    ("Sauce Labs Bolt T-Shirt")
])
def test_check_cart(logged_in_page:Page,products:str):
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")
    logged_in_page.locator(".inventory_item").filter(has_text=products).get_by_role("button").click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")
    logged_in_page.locator("[data-test='shopping-cart-link']").click()
    logged_in_page.get_by_role("button", name="Remove").click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_be_hidden()


@pytest.mark.parametrize("sorttype,firstproduct", [
    ("az","Sauce Labs Backpack"),
    ("za","Test.allTheThings() T-Shirt (Red)"),
    ("lohi","Sauce Labs Onesie"),
    ("hilo","Sauce Labs Fleece Jacket"),
])
def test_check_first_product(logged_in_page:Page,sorttype:str,firstproduct:str):
    logged_in_page.locator("[data-test='product-sort-container']").select_option(sorttype)
    expect(logged_in_page.locator("[data-test='product-sort-container']")).to_have_value(sorttype)
    expect(logged_in_page.locator("[data-test='inventory-item-name']").first).to_have_text(firstproduct)