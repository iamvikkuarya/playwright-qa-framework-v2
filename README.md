# 🎭 Learning Playwright with pytest

A personal learning repo documenting my journey into **browser test automation** using Playwright and pytest. Each test file represents a step forward — from basic navigation to reusable fixtures and clean test design.

> 🌱 This is a work in progress. Every commit is a lesson learned.

---

## 🧠 What I'm Learning

- Writing end-to-end tests with **Playwright's Python API**
- Using **pytest** as a test runner
- Applying **semantic locators** (by role, placeholder, text) instead of fragile CSS selectors
- Creating **shared fixtures** in `conftest.py` to avoid repeated setup code
- Structuring a clean, readable test project from scratch

---

## 🛠️ Tech Stack

| Tool | Version |
|------|---------|
| [Playwright](https://playwright.dev/python/) | 1.60.0 |
| [pytest](https://docs.pytest.org/) | 9.1.0 |
| [pytest-playwright](https://playwright.dev/python/docs/test-runners) | 0.8.0 |
| Python | 3.x |

The app being tested: **[Sauce Demo](https://www.saucedemo.com/)** — a publicly available demo e-commerce site, perfect for practising QA automation.

---

## 📁 Project Structure

```
playwright-qa-framework-v2/
│
├── conftest.py               # Shared fixtures (e.g. logged_in_page)
├── requirements.txt          # All Python dependencies
├── .gitignore
│
└── tests/
    ├── test_login.py         # Step 1 – Login flows
    ├── test_practice.py      # Step 2 – Sorting, cart counts, button states
    └── test_cart.py          # Step 3 – Cart using the logged_in_page fixture
```

---

## 🪜 Learning Steps

### Step 1 — Login Tests (`test_login.py`)
My first set of tests. Covers the login page: valid login, wrong password, and empty form submission.

```
✅ test_login                    → valid credentials land on inventory page
✅ test_login_invalid_password   → wrong password shows error banner
✅ test_login_without_credentials → empty form shows "Username is required"
```

---

### Step 2 — Practice Tests (`test_practice.py`)
Expanded into more interactions: sorting a product list, checking cart badge counts, and verifying button state changes.

```
✅ test_locked_out_user    → locked account shows the right error message
✅ test_sort_functionality → sort by price (low → high) works correctly
✅ test_2products_incart   → adding 2 items updates badge to "2"
✅ test_addtocart_button   → button text changes to "Remove" after click
```

---

### Step 3 — Fixtures & DRY Code (`conftest.py` + `test_cart.py`)
The biggest conceptual leap — using `conftest.py` to create a **shared fixture** that handles login once, so tests don't repeat the same setup over and over.

**Before (repetitive):**
```python
def test_cart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    # ... actual test logic
```

**After (clean, reusable):**
```python
# conftest.py
@pytest.fixture
def logged_in_page(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    return page

# test_cart.py
def test_cart(logged_in_page: Page):
    logged_in_page.locator(".inventory_item") \
        .filter(has_text="Sauce Labs Backpack") \
        .get_by_role("button").click()
    expect(logged_in_page.locator(".shopping_cart_badge")).to_have_text("1")
```

---

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/iamvikkuarya/playwright-qa-framework-v2.git
cd playwright-qa-framework-v2

# 2. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install
```

---

## ▶️ Running the Tests

```bash
pytest                          # run everything
pytest tests/test_login.py      # run a specific file
pytest --headed                 # watch the browser
pytest -v                       # verbose output
pytest --browser firefox        # use a different browser
```

---

## 📌 Notes to Self

- Prefer **role-based locators** (`get_by_role`, `get_by_placeholder`) — they're more resilient than CSS selectors
- `conftest.py` fixtures are automatically discovered by pytest — no imports needed in test files
- `expect()` from Playwright has built-in auto-waiting — no manual `sleep()` needed