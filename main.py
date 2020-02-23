import helpers
import atu

try:
    while True:
        atu.measure_level()
        atu.maybe_act()
        helpers.sleep(minutes=0.1, print_=True)


except KeyboardInterrupt:
    print("Exit ATU script")
