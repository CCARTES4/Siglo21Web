from django.conf import settings
from django.shortcuts import render, redirect
from django.db import connection
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from datetime import date
from django.contrib import messages
import cx_Oracle
import base64


# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def carta(request):
    categoria = 1
    datos_platos = listar_platos(categoria)

    arreglo = []

    for i in datos_platos:
        data = {
            'data': i,
            'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
        }
        arreglo.append(data)

    data = {
        'carta': arreglo


    }
    

    if request.POST:
        menu = request.POST.get("BOTON_MENU", "")
        
        if menu == "1":
            categoria = 1
            datos_platos = listar_platos(categoria)
            arreglo = []

            for i in datos_platos:
                data = {
                    'data': i,
                    'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
                }
                arreglo.append(data)

            data = {
                'carta': arreglo


            }
            return render(request, 'core/carta.html', data)

        if menu == "2":
            categoria = 2
            datos_platos = listar_platos(categoria)
            arreglo = []

            for i in datos_platos:
                data = {
                    'data': i,
                    'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
                }
                arreglo.append(data)

            data = {
                'carta': arreglo


            }
            return render(request, 'core/carta.html', data)

        if menu == "3":
            categoria = 3
            datos_platos = listar_platos(categoria)
            arreglo = []

            for i in datos_platos:
                data = {
                    'data': i,
                    'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
                }
                arreglo.append(data)

            data = {
                'carta': arreglo


            }
            return render(request, 'core/carta.html', data)
        
        if menu == "4":
            categoria = 4
            datos_platos = listar_platos(categoria)
            arreglo = []

            for i in datos_platos:
                data = {
                    'data': i,
                    'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
                }
                arreglo.append(data)

            data = {
                'carta': arreglo


            }
            return render(request, 'core/carta.html', data)
        
        if menu == "5":
            categoria = 5
            datos_platos = listar_platos(categoria)
            arreglo = []

            for i in datos_platos:
                data = {
                    'data': i,
                    'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
                }
                arreglo.append(data)

            data = {
                'carta': arreglo


            }
            return render(request, 'core/carta.html', data)
        
        if menu == "6":
            categoria = 6
            datos_platos = listar_platos(categoria)
            arreglo = []

            for i in datos_platos:
                data = {
                    'data': i,
                    'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
                }
                arreglo.append(data)

            data = {
                'carta': arreglo


            }
            return render(request, 'core/carta.html', data)

        if menu == "7":
            categoria = 7
            datos_platos = listar_platos(categoria)
            arreglo = []

            for i in datos_platos:
                data = {
                    'data': i,
                    'imagen': str(base64.b64encode(i[0].read()), 'utf-8')
                }
                arreglo.append(data)

            data = {
                'carta': arreglo


            }
            return render(request, 'core/carta.html', data)

    return render(request, 'core/carta.html',data)


def send_email(salida, correo, nombre, aPaterno, aMaterno, Fecha_reserva, Hora):
    salida = darID()
    context = {'salida': int(salida), 'nombre': nombre, 'aPaterno':aPaterno,'aMaterno':aMaterno, 'fecha_reserva':Fecha_reserva, 'hora':Hora}
    template = get_template('core/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'SOLICITUD DE RESERVA RECIBIDA',
        'Reserva',
        settings.EMAIL_HOST_USER,
        [correo]
    )
    email.attach_alternative(content, 'text/html')
    email.send()


def reservar(request):
    data = {

    }

    if request.method == 'POST':
        rut_cli = request.POST.get('rut_cli')
        nombre = request.POST.get('nombre')
        aPaterno = request.POST.get('aPaterno')
        aMaterno = request.POST.get('aMaterno')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        fecha_reserva = request.POST.get('Fecha_reserva')
        cant_personas = request.POST.get('cant_personas')
        hora = request.POST.get('Hora')
        comentario = request.POST.get('comentario')
        salida = agregar_reserva(rut_cli, nombre, aPaterno, aMaterno, correo,telefono,fecha_reserva,cant_personas,hora,comentario)

        if salida == 1:
            data['mensaje'] = 'Reserva agendada correctamente. Todos los datos han sido enviados a su correo.'
            messages.success(
                request, "Reserva agendada correctamente. Todos los datos han sido enviados a su correo.")
        else:
            data['mensaje'] = 'No hemos podido agendar su reserva. Por favor, inténtelo nuevamente.'
            messages.warning(
                request, 'No hemos podido agendar su reserva. Por favor, inténtelo nuevamente.')
        send_email(salida, correo, nombre, aPaterno,
                   aMaterno, fecha_reserva, hora)
    return render(request, 'core/reservar.html', data)


def nosotros(request):
    return render(request, 'core/nosotros.html')


def darID():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_DAR_ID_RESERVA', [salida])
    return salida.getvalue()


def consReserva(request):
    resEliminar = {

    }
    if request.POST:
        xd = request.POST.get("BOTON", "")
        if xd == "CONSULTAR":
            S_RUT_CLI = request.POST.get('rut_cli')
            S_FECHA = request.POST.get('Fecha_reserva')
            S_HORA = request.POST.get('Hora')
            S_N_RESERVA = request.POST.get('N_reserva')
            data = {
                'consReserva': consultar_reserva(S_RUT_CLI, S_FECHA, S_HORA, S_N_RESERVA),

            }

            return render(request, 'core/consReserva.html', data)

        if xd == "ELIMINAR":

            S_ID_RESERVA = request.POST.get('txtId')
            salida = eliminar_reserva(S_ID_RESERVA)

            if salida == 1:
                resEliminar['mensaje'] = 'Su reserva ha sido anulada correctamente.'
                messages.success(
                    request, "Su reserva ha sido anulada correctamente.")
            else:
                resEliminar['mensaje'] = 'Su reserva no ha podido ser anulada. Por favor, intentelo nuevamente'
                messages.warning(
                    request, "Su reserva no ha podido ser anulada. Por favor, intentelo nuevamente")
            return render(request, 'core/consReserva.html', resEliminar)
    return render(request, 'core/consReserva.html')


def consultar_reserva(S_RUT_CLI, S_FECHA, S_HORA, S_N_RESERVA):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('SP_CONSULTAR_RESERVA', [S_RUT_CLI, S_FECHA, S_HORA, S_N_RESERVA,out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)
    return lista


def agregar_reserva(rut_cli, nombre, apaterno, amaterno, correo, telefono, fecha_reserva, cant_personas, hora, comentario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA', [rut_cli, nombre, apaterno, amaterno,
                                           correo, telefono, fecha_reserva, cant_personas, hora, comentario, salida])
    return salida.getvalue()


def listar_platos(categoria):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('LISTAR_PLATOS_WEB', [categoria, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista


def eliminar_reserva(S_ID_RESERVA):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RESERVA', [S_ID_RESERVA, salida])
    return salida.getvalue()
