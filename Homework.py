actualtemp = 75
desiredtemp = 77
if actualtemp > desiredtemp:
    status = 'Run A/C'
elif actualtemp < desiredtemp:
    status = 'Run the heat'
if actualtemp == desiredtemp:
    status = 'Stand by'
print('Heating and cooling system status: ' + status)


def convert_temperature(tempCelsius, targetUnit):
    if targetUnit == 'C':
        print(f'{tempCelsius} C')
    elif targetUnit == 'F':
        tempFahrenheit = (tempCelsius * 9/5) + 32
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


