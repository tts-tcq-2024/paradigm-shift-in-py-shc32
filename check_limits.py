# Global variable to set the language (English or German)
LANGUAGE = 'EN'  # Use 'DE' for German

def translate(message_key):
    """Translate messages based on the selected language."""
    translations = {
        'EN': {
            'too_low': "{} is too low!",
            'too_high': "{} is too high!",
            'approaching_low': "{} is approaching discharge!",
            'approaching_high': "{} is approaching charge-peak!",
        },
        'DE': {
            'too_low': "{} ist zu niedrig!",
            'too_high': "{} ist zu hoch!",
            'approaching_low': "{} nähert sich der Entladung!",
            'approaching_high': "{} nähert sich dem Ladevorgang!",
        }
    }
    return translations[LANGUAGE].get(message_key, "{}")

def check_measure(measure_name, measure_value, lower_limit, upper_limit):
    """Check if a measurement is within the specified limits and provide warnings."""
    warning_tolerance = 0.05 * upper_limit
    results = {}
    
    # Determine if a warning is needed
    if lower_limit <= measure_value < lower_limit + warning_tolerance:
        print(translate('approaching_low').format(measure_name))
    
    if upper_limit - warning_tolerance < measure_value <= upper_limit:
        print(translate('approaching_high').format(measure_name))
    
    # Check if the value is within the acceptable range
    if measure_value < lower_limit:
        print(translate('too_low').format(measure_name))
        results["status"] = False
    elif measure_value > upper_limit:
        print(translate('too_high').format(measure_name))
        results["status"] = False
    else:
        results["status"] = True

    return results

def battery_is_ok(temperature, soc, charge_rate):
    """Check if the battery is within acceptable parameters and issue warnings."""
    temp_results = check_measure("Temperature", temperature, 0, 45)
    soc_results = check_measure("State of Charge", soc, 20, 80)
    charge_results = check_measure("Charge Rate", charge_rate, 0, 0.8)

    # Return whether all measurements are within acceptable limits
    return temp_results["status"] and soc_results["status"] and charge_results["status"]

if __name__ == "__main__":
    # Test cases
    assert battery_is_ok(25, 70, 0.7) == True
    assert battery_is_ok(50, 85, 0.0) == False
    assert battery_is_ok(-1, 70, 0.7) == False
    assert battery_is_ok(25, 10, 0.7) == False
    assert battery_is_ok(25, 70, 0.9) == False


