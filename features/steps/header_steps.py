from behave import given, when, then


# from target home page search for a product
@when('I search for {product_name}')
def search_product(context, product_name):
    context.app.header.search_product(product_name)


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart()

@when('Click the account button sign in button opens')
def click_account_button(context):
    context.app.header.click_account_btn()


@when('Click on "Target Circle" button')
def click_tar_cir_btn(context):
    context.app.header.target_circle()


@then('Verify header has {expected_amount} links')
def verify_header_link_count(context, expected_amount):
    context.app.header.verify_header_link_count()


@then('Verify page has at least {expected_amount} benefits cells')
def verify_benefits_cells(context, expected_amount):
        context.app.header.circle_benefits(expected_amount)



