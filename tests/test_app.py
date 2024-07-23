from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("please login:")


"""
Test form can be filled out and submitted
"""

def test_create_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    page.goto(f"http://{test_web_address}/spaces/new")

    # This time we click the link with the text 'Add a new space'
    # page.click("text=List a space")

    # Then we fill out the field with the name attribute 'Property Name'
    page.fill("input[name='Property Name']", "Air BnB 1")

    # And the field with the name attribute 'description'
    page.fill("input[name='Description']", "One bed")

    # And the field with the name attribute 'price per night (£)'
    page.fill("input[name='Price per Night (£)']", "777") #LOOK INTO POUND SIGN

    # And the field with the name attribute 'available from'
    page.fill("input[name='Available From (dd-mm-yyyy)']", "2024-07-10")

    # And the field with the name attribute 'available to'
    page.fill("input[name='Available To (dd-mm-yyyy)']", "2026-07-10")

    # Finally we click the button with the text 'List my Space'
    page.click("text=List My Space")

    # # Just as before, the virtual browser acts just like a normal browser and
    # # goes to the next page without us having to tell it to.

    # title_element = page.locator(".t-title")
    # expect(title_element).to_have_text("Title: The Hobbit")

    # author_element = page.locator(".t-author-name")
    # expect(author_element).to_have_text("Author: J.R.R. Tolkien")

#create request tests:
def test_click_through_to_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/bedsforbodies_seed.sql")
    page.goto(f"http://{test_web_address}/spaces")
    page.locator("button:has-text('View This Space')").first.click()
    expect(page).to_have_url(f'http://{test_web_address}/spaces/1')

# """
# We can list out all of the spaces / properties
# """
# def test_get_properties(db_connection, page, test_web_address):
#     # We seed our database with the properties seed file
#     db_connection.seed("seeds/bedsforbodies_seed.sql")

#     # We load a virtual browser and navigate to the /spaces page
#     page.goto(f"http://{test_web_address}/spaces")

#     # We look at all the <li> tags
#     list_items = page.locator("li")

#     # We assert that it has the properties in it
#     expect(list_items).to_have_text([
#         "Property(test_property1, This place is nice, test1, 999, 1)",
#         "Property(test_property2, This place is okay, test2, 888, 1)",
#         "Property(test_property3, This place is amazing, test3, 777, 2)",
#         "Property(test_property4, This place is cool, test4, 666, 2)",
#         "Property(test_property5, This place is wicked, test5, 555, 3)",
#         "Property(test_property6, This place is rubbish, test6, 444, 3)",
#     ])

