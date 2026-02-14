import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width":1920, "height": 1080})
    page = context.new_page()
    page.set_default_timeout(60000);
    page.goto("http://e08g02t03-lab-prod.centralindia.cloudapp.azure.com:8069/")
    page.wait_for_load_state("networkidle")
    page.get_by_role("menuitem", name="Home").click()
    page.get_by_role("link", name="Get in touch").click()
    page.locator("#wrap").get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Ask us a question").click()
    page.get_by_role("menuitem", name="Shop").click()
    page.get_by_text("Office Lunch Box").click()
    page.get_by_role("link", name="Add one").click()
    page.get_by_role("button", name=" Add to cart").click()
    page.get_by_role("button", name="View cart").click()
    page.get_by_role("menuitem", name="Shop").click()
    page.get_by_text("Diabetic-Friendly Meal Plan").click()
    page.get_by_role("button", name=" Add to cart").click()
    page.get_by_role("link", name="Add one").click()
    page.get_by_role("button", name=" Add to cart").click()
    page.get_by_role("menuitem", name="Services").click()
    page.locator("img").nth(2).click()
    page.locator("img").nth(3).click()
    page.locator("img").nth(4).click()
    page.get_by_text("Quick Meal Prep Replace the").click()
    page.get_by_role("heading", name="Seasonal Specials").click()
    page.get_by_role("heading", name="Fresh Ingredients").click()
    page.get_by_role("menuitem", name="Contact us").click()
    page.get_by_role("textbox", name="Name *").click()
    page.get_by_role("textbox", name="Name *").fill("nicholas")
    page.get_by_role("textbox", name="Phone Number").click()
    page.get_by_role("textbox", name="Name *").fill("nicholass")
    page.get_by_role("textbox", name="Phone Number").fill("oh")
    page.get_by_role("textbox", name="Email *").click()
    page.get_by_role("textbox", name="Email *").fill("nicholassoh@email.com")
    page.get_by_role("textbox", name="Company").click()
    page.get_by_role("textbox", name="Email *").fill("nicholassoh@email.coms")
    page.get_by_role("textbox", name="Company").fill("mu")
    page.get_by_role("textbox", name="Subject *").click()
    page.get_by_role("textbox", name="Subject *").fill("smu")
    page.get_by_role("textbox", name="Question *").click()
    page.get_by_role("textbox", name="Question *").fill("smut")
    page.get_by_role("button", name="Submit").click()
    page.get_by_label("Main").get_by_title("Search").click()
    page.get_by_role("searchbox", name="Search...").fill("hi")
    page.get_by_role("link", name=" Contact Us Contact us").click()
    page.get_by_role("link", name=" +65-").click()
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("link", name="Contact Us", exact=True).click()
    page.get_by_role("menuitem", name="Contact us").click()
    page.get_by_role("menuitem", name="Services").click()
    page.get_by_role("menuitem", name="Shop").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

