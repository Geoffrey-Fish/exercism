'''Meltdown by ScyMarshall'''
def is_criticality_balanced(temperature, neutrons_emitted):
    '''nice and short this time'''
    return bool(temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    '''I think I got it.'''
    generated_power = voltage * current
    percent = (generated_power / theoretical_max_power) * 100
    if percent >= 80 :
        return "green"
    elif percent >= 60 :
        return "orange"
    elif percent >= 30 :
        return "red"
    else :
        return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    '''Yet still simple!'''
    balance = temperature * neutrons_produced_per_second
    over = threshold * 1.1
    under = threshold * 0.9
    if balance > over :
        return 'DANGER'
    elif balance >= under :
        return 'NORMAL'
    else :
        return 'LOW'
