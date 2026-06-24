    # Playwright + pytest — SDET Learning Syllabus

**Goal:** Build a portfolio-ready Playwright automation framework and land an SDET role.  
**Stack:** Python · Playwright · pytest  
**Target app:** [Sauce Demo](https://www.saucedemo.com/) → [OrangeHRM](https://opensource-demo.orangehrmlive.com/)

---

## Week 1 — Foundation (Jun 15–21)

### Concepts
- [x] Virtual environments and why they exist
- [x] Installing Playwright and pytest-playwright
- [x] How pytest discovers tests (`test_` prefix)
- [x] The three steps of every test: Find → Act → Assert
- [x] Writing basic tests with `page: Page`
- [x] Semantic locators — `get_by_placeholder`, `get_by_role`, `get_by_text`
- [x] CSS attribute selectors — `page.locator("[data-test='...']")`
- [x] Assertions with `expect()` — `to_be_visible`, `to_have_text`, `to_have_url`
- [x] Selector stability — why `data-test` beats class, why class beats CSS
- [x] Chaining locators — `.filter(has_text=)` to scope inside a card
- [x] `conftest.py` — what it is and why fixtures live there
- [x] Writing a shared fixture — `logged_in_page`
- [x] Fixture injection — how pytest matches parameter names to fixtures
- [x] `@pytest.mark.parametrize` — data-driven tests

### Project structure introduced
```
playwright_learn/
├── conftest.py
├── requirements.txt
├── .gitignore
├── learning/       ← concept experiments
└── tests/          ← growing test suite
```

---

## Week 2 — Structure (Jun 22–28)

- [ ] Page Object Model (POM) — what it is and why it exists
- [ ] `BasePage` class — shared methods across all pages
- [ ] `LoginPage`, `InventoryPage`, `CartPage` classes
- [ ] Separating test logic from page interaction logic
- [ ] Fixture scopes — `function`, `session`, `module`
- [ ] Setup and teardown with `yield` in fixtures
- [ ] Organising a real framework folder structure

---

## Week 3 — Advanced (Jun 29 – Jul 5)

- [ ] API testing with `playwright.request.new_context()`
- [ ] GET and POST requests — status codes, JSON assertions
- [ ] Running API and UI tests in the same suite
- [ ] Network interception — `page.route()` to mock responses
- [ ] Testing UI behaviour against mocked backend errors
- [ ] Parallel test execution — `pytest -n auto`
- [ ] HTML reporting — `pytest-html`
- [ ] Reading traces — `playwright show-trace`
- [ ] GitHub Actions CI — running tests on every push

---

## Week 4 — Portfolio (Jul 6–12)

- [ ] Full test suite on OrangeHRM — auth, CRUD, API, negative cases
- [ ] Clean POM structure throughout
- [ ] README — coverage table, architecture, how to run
- [ ] Interview prep — top 20 SDET questions
- [ ] Mock walkthrough — explain every file and decision out loud

---

## Reference

### Locator priority (most to least stable)
1. `data-testid` → `get_by_test_id()`
2. `data-test` → `page.locator("[data-test='...']")`
3. Role + visible text → `get_by_role()`
4. Placeholder → `get_by_placeholder()`
5. Visible text → `get_by_text()`
6. CSS class → `page.locator(".classname")` — last resort

### Commands
```bash
pytest                          # run all tests
pytest -v                       # verbose
pytest --headed                 # watch the browser
pytest -n auto                  # parallel (Week 3)
pytest tests/test_login.py      # specific file
pip freeze > requirements.txt   # update dependencies
```