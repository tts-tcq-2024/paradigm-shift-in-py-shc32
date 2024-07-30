def check_measure(measure_name, measure_value, lower_limit, upper_limit):
    results = {}
    status = True
    if measure_value < lower_limit:
        print(measure_name + " is too low!")
        status = False
    elif measure_value > upper_limit:
        print(measure_name + " is too high!")
        status = False
    results["status"] = status
    return results

def battery_is_ok(temperature, soc, charge_rate):
    temp_results = check_measure("Temperature", temperature, 0, 45)
    soc_results = check_measure("State of Charge", soc, 20, 80)
    charge_results = check_measure("Charge Rate", charge_rate, 0, 0.8)
    return temp_results["status"] and soc_results["status"] and charge_results["status"]

if __name__ == "__main__":
    # Test cases
    assert battery_is_ok(25, 70, 0.7) == True
    assert battery_is_ok(50, 85, 0.0) == False
    assert battery_is_ok(-1, 70, 0.7) == False
    assert battery_is_ok(25, 10, 0.7) == False
    assert battery_is_ok(25, 70, 0.9) == False
    print("Some more tests needed")
