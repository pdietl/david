# file:features/steps/step_tutorial01.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False
    try:
        1 / 0
    except ZeroDivisionError as e:
        print('Division by zero!')
        print(e)
        context.error = 'yes'

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
    print("Value of context.error: '" + context.error + "'")
