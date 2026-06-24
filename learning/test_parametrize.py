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