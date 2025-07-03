from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from Unit_Converter.forms import ConvertLengthForm, ConvertMassForm, ConvertTemperatureForm
from Unit_Converter.models import ConvertLength, ConvertMass, ConvertTemperature
from Unit_Converter.converts import convert_length, convert_mass, convert_temp

def main(request):
    template = loader.get_template('main.html')

    # merge data from all tables
    converts = list(ConvertLength.objects.all().values()) + list(ConvertMass.objects.all().values()) + list(ConvertTemperature.objects.all().values())
    converts.sort(key=lambda x: x['created_at'])

    # check if date is empty
    empty = False
    if converts == []:
        empty = True

    return HttpResponse(template.render(request=request, context={'converts': converts, 'empty': empty}))

def length(request):
    template = loader.get_template('length.html')
    submitted = False

    if request.method == "POST": # saves form to database if it's valid
        form = ConvertLengthForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/length?submitted=True')
    else: # else reenter the from
        form = ConvertLengthForm()
        if 'submitted' in request.GET:
            submitted = True

    if submitted:
        convert = ConvertLength.objects.values().last() # last object added to db is the current convert

        if convert['input_unit'] == '-' or convert['output_unit'] == '-':
            output = 'Input or output unit was not specified'
        elif convert['input_unit'] == convert['output_unit']:
            output = convert['input_value']
            if float(int(output)) == output:
                output = int(output)
        else:
            # if convert_length['input_unit']['output_unit'] doesn't exist, convert_length['output_unit']['input_unit'] exists
            try:
                factor = convert_length[convert['input_unit']][convert['output_unit']]
                output = round(float(convert['input_value']) * factor, 2)
            except KeyError:
                factor = convert_length[convert['output_unit']][convert['input_unit']]
                output = round(float(convert['input_value']) / factor, 2)

            if float(int(output)) == output:
                output = int(output)

        if float(int(convert['input_value'])) == convert['input_value']:
            convert['input_value'] = int(convert['input_value'])
    else: # provide default data in case from wasn't submitted
        output = 'Form was not submitted'
        convert = {
            'input_value': None,
            'input_unit': None,
            'output_unit': None
        }

    return HttpResponse(template.render(request=request, context={'form': form,
                                                                  'submitted': submitted,
                                                                  'output': output,
                                                                  'last': convert}))

def mass(request): # analogicly like in length
    template = loader.get_template('mass.html')
    submitted = False

    if request.method == "POST":
        form = ConvertMassForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/mass?submitted=True')
    else:
        form = ConvertMassForm()
        if 'submitted' in request.GET:
            submitted = True

    if submitted:
        convert = ConvertMass.objects.values().last()

        if convert['input_unit'] == '-' or convert['output_unit'] == '-':
            output = 'Input or output unit was not specified'
        elif convert['input_unit'] == convert['output_unit']:
            output = convert['input_value']
            if float(int(output)) == output:
                output = int(output)
        else:
            try:
                factor = convert_mass[convert['input_unit']][convert['output_unit']]
                output = round(float(convert['input_value']) * factor, 2)
            except KeyError:
                factor = convert_mass[convert['output_unit']][convert['input_unit']]
                output = round(float(convert['input_value']) / factor, 2)

            if float(int(output)) == output:
                output = int(output)

        if float(int(convert['input_value'])) == convert['input_value']:
            convert['input_value'] = int(convert['input_value'])
    else:
        output = 'Form was not submitted'
        convert = {
            'input_value': None,
            'input_unit': None,
            'output_unit': None
        }

    return HttpResponse(template.render(request=request, context={'form': form,
                                                                  'submitted': submitted,
                                                                  'output': output,
                                                                  'last': convert}))

def temperature(request):
    template = loader.get_template('temperature.html')
    submitted = False

    if request.method == "POST":
        form = ConvertTemperatureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/temperature?submitted=True')
    else:
        form = ConvertTemperatureForm()
        if 'submitted' in request.GET:
            submitted = True

    if submitted:
        convert = ConvertTemperature.objects.values().last()

        if convert['input_unit'] == '-' or convert['output_unit'] == '-':
            output = 'Input or output unit was not specified'
        elif convert['input_unit'] == convert['output_unit']:
            output = convert['input_value']
            if float(int(output)) == output:
                output = int(output)
        else: # explicitly defining what is being converted
            if convert['input_unit'] == 'celsius':
                if convert['output_unit'] == 'fahrenheit':
                    output = (float(convert['input_value']) * convert_temp['celsius']['fahrenheit']) + 32.0
                else:
                    output = float(convert['input_value']) + convert_temp['celsius']['kelvin']
            elif convert['input_unit'] == 'fahrenheit':
                if convert['output_unit'] == 'celsius':
                    output = (float(convert['input_value']) - 32.0) * convert_temp['fahrenheit']['celsius']
                else:
                    output = float(convert['input_value']) + convert_temp['fahrenheit']['kelvin']
            else:
                output = float(convert['input_value']) + convert_temp['kelvin'][convert['output_unit']]

            if float(int(output)) == output:
                output = int(output)

        if float(int(convert['input_value'])) == convert['input_value']:
            convert['input_value'] = int(convert['input_value'])
    else:
        output = 'Form was not submitted'
        convert = {
            'input_value': None,
            'input_unit': None,
            'output_unit': None
        }

    return HttpResponse(template.render(request=request, context={'form': form,
                                                                  'submitted': submitted,
                                                                  'output': output,
                                                                  'last': convert}))