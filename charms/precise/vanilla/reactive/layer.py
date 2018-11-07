from charms.reactive import when, when_not, set_state

@when_not('example.installed')
def install_example():
    set_flag('example.installed')
