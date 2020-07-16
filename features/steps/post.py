from behave import *
from arduino import arduino_controller
import time

#com = "COM15"
#commander = arduino_controller.CommandWriter(com)
#time.sleep(2)

@given(u'a powered STM32F412G discovery kit connected via USART')
def step_impl(context):
    pass

@when(u'the system is restarted')
@given(u'the system is restarted')
def step_impl(context):
    commander.send_command("reset")


@when(u'POST is completed (LD2 turns off)')
def step_impl(context):
    commander.send_command("postled")


@then(u'LD2 is on during POST')
def step_impl(context):
    assert commander.check_state("postled") is True

@then(u'\"[POST]: Flash ID verification and RWR cycle passed\" is received via USART')
def step_impl(context):
    pass 