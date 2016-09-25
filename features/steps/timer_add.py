from time_adder import time_add

#timesets and timetotals for the scenario outline test
tester_dict = {
    'test1': ['3:30','4:45','15:27'],
    'test2': ['4:30','30:45','23:17','45:06'],
    'test3': ['5:30','0:00'],
    'test4': ['6:30','59:59','0:32','34:48','50:12'],
    'total1': '23:42',
    'total2': '1:43:38',
    'total3': '5:30',
    'total4': '2:32:01'
}

def val_grabber(timeval):
    for key, value in tester_dict.iteritems():
        if key == str(timeval):
            return value

@given('a working time add function')
def step_impl(context):
    assert time_add

@when('no time is entered')
def step_impl(context):
    context.no_time = []

@then('a time of 0:00 is returned')
def step_impl(context):
    assert time_add(context.no_time) == '0:00'

@when('one time length is entered')
def step_impl(context):
    context.one_time = ['3:35']

@then('that time is returned')
def step_impl(context):
    assert time_add(context.one_time) == '3:35'

@when('a {timeset} is entered')
def step_impl(context, timeset):
    context.timeset = val_grabber(timeset)

@then('the correct {timetotal} is returned')
def step_impl(context, timetotal):
    assert time_add(context.timeset) == val_grabber(timetotal)
