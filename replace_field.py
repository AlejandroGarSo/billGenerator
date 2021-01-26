import string
from ast import literal_eval
import random, time
from decimal import Decimal, ROUND_UP
import math


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    stime = time.mktime(time.strptime(start, "%d/%m/%Y"))
    etime = time.mktime(time.strptime(end, "%d/%m/%Y"))

    ptime = stime + random.random() * (etime - stime)

    return ptime


def random_nif():
    """
    This function will return a random NIF with the correct format.
    """
    nif_letter = literal_eval(open("dictionaries/nif_letter.txt").read())
    nif = random.randint(10 ** 7, 10 ** 8 - 1)
    let = nif_letter[str(nif % 23)]
    return str(nif) + let


def label_randomizer():
    data_directory = "dictionaries/"

    nombres = open(data_directory + "spanish_names.txt", encoding="UTF-8").readlines()
    apellidos = open(data_directory + "spanish_surnames.txt", encoding="UTF-8").readlines()
    comercializadoras = [line.replace('\n', '') for line in
                         open(data_directory + "spanish_marketers.txt", encoding="UTF-8").readlines()]
    distribuidoras = open(data_directory + "spanish_distributors.txt", encoding="UTF-8").readlines()
    poblaciones = open(data_directory + "spanish_villages.txt", encoding="UTF-8").readlines()
    calles = open(data_directory + "spanish_streets.txt", encoding="UTF-8").readlines()

    result = {}

    result['Nombre'] = (random.choice(nombres)).replace('\n', '') + ' ' + \
                       (random.choice(apellidos)).replace('\n', '') + ' ' + \
                       (random.choice(apellidos)).replace('\n', '')
    if random.randint(0, 2) == 1:
        result['Nombre'] = result['Nombre'].upper()

    result['NIF'] = random_nif()
    #print(result['NIF'])
    result['Direccion'] = (random.choice(calles)).replace('\n', '')
    com = random.choice(comercializadoras)
    result['Comercializadora'] = com.split(";")[1]
    result['CDir'] = com.split(";")[2]
    result['CCP'] = com.split(";")[3]
    dist = random.choice(distribuidoras)
    result['Distribuidora'] = dist.split(";")[2].replace('\n', '')
    result['CIF'] = dist.split(";")[0]
    poblacion = random.choice(poblaciones).split(";")
    result['CP'] = poblacion[2].replace('"', '').replace('\n', '')
    result['Poblacion'] = poblacion[1].replace('"', '')
    result['Provincia'] = poblacion[0].replace('"', '')
    result['CUPS'] = 'ES' + str(random.randint(10 ** 15, 10 ** 16 - 1))
    letters = string.ascii_uppercase
    result['CUPS'] += ''.join(random.choice(letters) for i in range(4))
    result['NumeroContrato'] = str(random.randint(10 ** 12, 10 ** 13 - 1))
    result['PotenciaContratada'] = random.choice([2.00, 2.50, 3.00, 3.50, 4.00, 4.50, 5.00, 5.50, 6.00, 6.50])
    result['PeajeAcceso'] = random.choice(['2.0A', '20DHA'])


    fechainicio = random_date("01/01/1990", "31/12/2020")
    month_time = 2592000
    day_time = 86400
    months = random.randint(1, 2)
    days = 30 * months

    lectura_anterior = random.randint(0, 100000)
    consumo_anterior = random.randint(0, 7000)

    result['LecturaAnterior'] = lectura_anterior
    result['LecturaActual'] = lectura_anterior + random.randint(0, 1000)
    result['ConsumoAnterior'] = consumo_anterior
    result['ConsumoActual'] = result['LecturaActual'] - lectura_anterior
    result['ConsumoEnergia'] = result['ConsumoActual']
    result['ConsumoValle'] = int(result['ConsumoEnergia'] * 0.45)
    result['ConsumoPunta'] = int(result['ConsumoEnergia'] * 0.55)

    format = '%d/%m/%Y'
    result['FechaInicio'] = \
        time.strftime(format, time.localtime(fechainicio))
    result['FechaFin'] = \
        time.strftime(format, time.localtime(fechainicio + months * month_time))
    result['FinContrato'] = \
        time.strftime(format, time.localtime(fechainicio + months * month_time))
    result['FechaEmision'] = \
        time.strftime(format, time.localtime(fechainicio + months * month_time + 2 * day_time))
    result['FechaCargo'] = \
        time.strftime(format, time.localtime(fechainicio + months * month_time + 5 * day_time))
    result['NumeroFactura'] = \
        'FI' + str(random.randint(10 ** 9, 10 ** 10 - 1))
    result['Days'] = days

    fechainicio += months * month_time

    ImporteKwContratado = Decimal(random.uniform(0.12, 0.16)).quantize(Decimal('.000001'), rounding=ROUND_UP)
    result['PrecioPotencia'] =str(ImporteKwContratado).replace('.', ',')
    ImportePotenciaContratada = Decimal(ImporteKwContratado * Decimal(result['PotenciaContratada'] * days)).quantize(Decimal('.01'), rounding=ROUND_UP)
    result['ImportePotencia'] = str(ImportePotenciaContratada).replace('.', ',')
    ImporteKw = Decimal(random.uniform(0.14, 0.20)).quantize(Decimal('.000001'), rounding=ROUND_UP)
    result['PrecioKwh'] = str(ImporteKw).replace('.', ',')
    ImporteEnergiaConsumida = Decimal(ImporteKw * Decimal(result['ConsumoEnergia'])).quantize(Decimal('.01'), rounding=ROUND_UP)
    result['ImporteEnergia'] = str(ImporteEnergiaConsumida).replace('.', ',')
    subtotalE = ImportePotenciaContratada + ImporteEnergiaConsumida
    result['ImporteSubTotal'] = str(Decimal(subtotalE).quantize(Decimal('.01'), rounding=ROUND_UP)).replace('.', ',')
    PrecioAlquiler = Decimal(random.uniform(0.02, 0.04)).quantize(Decimal('.000001'), rounding=ROUND_UP)
    result['PrecioAlquiler'] = str(PrecioAlquiler).replace('.', ',')
    ImporteAlquiler = Decimal(PrecioAlquiler * Decimal(PrecioAlquiler * days)).quantize(Decimal('.01'), rounding=ROUND_UP)
    result['ImporteAlquiler'] = str(ImporteAlquiler).replace('.', ',')
    ImpuestoElectP = Decimal(random.uniform(0.05, 0.06)).quantize(Decimal('.000001'), rounding=ROUND_UP)
    result['ImpuestoElectP'] = str(ImpuestoElectP*100).replace('.', ',')
    ImpuestoElect = ImpuestoElectP * subtotalE
    result['ImpuestoElectrico'] = str(Decimal(ImpuestoElect).quantize(Decimal('.01'), rounding=ROUND_UP)).replace('.', ',')
    subtotalO = ImporteAlquiler + ImpuestoElect
    result['ImporteSubTotalOtros'] = str(Decimal(subtotalO).quantize(Decimal('.01'), rounding=ROUND_UP)).replace('.',',')
    subtotal = subtotalE + subtotalO
    result['ImportePreImpuestos'] = str(Decimal(subtotal).quantize(Decimal('.01'), rounding=ROUND_UP)).replace('.', ',')
    impuesto = subtotal * Decimal(random.choice([0.02, 0.03, 0.07, 0.1]))
    ImporteImpuestos = Decimal(impuesto).quantize(Decimal('.01'), rounding=ROUND_UP)
    result['ImporteImpuestos'] = str(ImporteImpuestos).replace('.', ',')
    result['ImporteTotal'] = \
        str(Decimal(subtotal + ImporteImpuestos).quantize(Decimal('.01'), rounding=ROUND_UP)).replace('.', ',')

    return result

import json
import os

def gen_json(num_bills, templates):
    numdigits = math.floor(math.log10(num_bills) + 1)
    for tmp in templates:
        datadir = "bills//data//" + tmp
        if not os.path.exists(datadir):
            os.makedirs(datadir)
        for i in range(num_bills):
            result = label_randomizer()
            with open(datadir+'//Invoice'+str(i+1).zfill(numdigits)+'.json','w') as json_file:
                json.dump(result, json_file)