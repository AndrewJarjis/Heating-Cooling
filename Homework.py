actualtemp = 75
desiredtemp = 77


def status(actualTemp, desiredtemp):
    if actualTemp > desiredtemp:
        print('Run A/C')
    elif actualTemp < desiredtemp:
        print('Run the heat')
    if actualTemp == desiredtemp:
        print('Stand by')


status(actualtemp, desiredtemp)


def convert_temperature(tempCelsius, targetUnit):
    if targetUnit == 'C':
        print(f'{tempCelsius} C')
    elif targetUnit == 'F':
        tempFahrenheit = (tempCelsius * 9 / 5) + 32
        print(f'{tempFahrenheit} F')
    elif targetUnit == 'K':
        tempKelvin = tempCelsius + 273.15
        print(f'{tempKelvin} K')
    else:
        print(f'{tempCelsius} {targetUnit}')


convert_temperature(25, 'C')
convert_temperature(25, 'F')
convert_temperature(25, 'K')
convert_temperature(25, 'X')
