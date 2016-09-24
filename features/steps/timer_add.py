from time_adder import time_add

@given('a working time add function')
def step_impl(context):
    assert time_add

@when('no time is entered')
def step_impl(context):
    context.no_time = []

@then('a time of 0:00 is returned')
def step_impl(context):
    assert time_add(context.no_time) == '0:00'
