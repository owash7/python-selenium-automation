from behave import given, when, then


@then("Verify 'Your cart is empty' message is shown")
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_cart_empty()


@then("Open the cart page")
def open_cart(context):
    context.app.cart_page.open_cart()


@then("Verify cart has {product}")
def verify_product_name(context,product):
    context.app.cart_page.verify_cart_has_products(product)


@then("Verify my cart has {amount} item(s)")
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_product_amount(amount)
