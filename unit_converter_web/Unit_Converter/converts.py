convert_length = {
    'millimeter': {
        'centimeter': 0.1,
        'meter': 0.001,
        'kilometer': 0.000001,
        'inch': 0.03937007874,
        'foot': 0.00328084,
        'yard': 0.001094,
        'mile': 0.00000062137,
    },
    'centimeter': {
        'meter': 0.01,
        'kilometer': 0.0001,
        'inch': 0.3937007874,
        'foot': 0.0328084,
        'yard': 0.01094,
        'mile': 0.0000062137,
    },
    'meter': {
        'kilometer': 0.001,
        'inch': 3.937007874,
        'foot': 0.328084,
        'yard': 0.1094,
        'mile': 0.000062137,
    },
    'kilometer': {
        'inch': 3.937007874,
        'foot': 0.328084,
        'yard': 0.1094,
        'mile': 0.000062137,
    },
    'inch': {
        'foot': 0.0833333333,
        'yard': 0.0277777778,
        'mile': 0.00001578283,
    },
    'foot': {
        'yard': 0.0277777778,
        'mile': 0.00001578283,
    },
    'yard': {
        'mile': 0.000568181818,
    },
    'mile': {}
}

convert_mass = {
    'milligram': {
        'gram': 0.001,
        'kilogram': 0.000001,
        'ounce': 3.5274E-5,
        'pound': 2.2046226218488E-6,
    },
    'gram': {
        'kilogram': 1000,
        'ounce': 0.03527396195,
        'pound': 0.0022046226218488,
    },
    'kilogram': {
        'ounce': 35.2739619,
        'pound': 2.20462262,
    },
    'ounce': {
        'pound': 0.0625,
    },
    'pound': {}
}

convert_temp = {
    'celsius': {
        'fahrenheit': 1.8,
        'kelvin': 273.15
    },
    'fahrenheit': {
        'celsius': 0.5555555555556,
        'kelvin': 458.85
    },
    'kelvin': {
        'celsius': -273.15,
        'fahrenheit': -458.85
    }
}