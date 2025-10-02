import os

def get_upload_to(instance, filename):
    titulo_tomo = instance.tomo.titulo
    nro_tomo = instance.tomo.nro_tomo
    tomo = f"{titulo_tomo}_{nro_tomo}"
    gestion = instance.tomo.fecha_apertura.year
    nombre_mes = instance.tomo.fecha_apertura.strftime('%B')

    traduccion_mes = {
        'January': 'enero',
        'February': 'febrero',
        'March': 'marzo',
        'April': 'abril',
        'May': 'mayo',
        'June': 'junio',
        'July': 'julio',
        'August': 'agosto',
        'September': 'septiembre',
        'October': 'octubre',
        'November': 'noviembre',
        'December': 'diciembre'
    }

    nombre_mes_es = traduccion_mes.get(nombre_mes, nombre_mes)

    return os.path.join('archivos', str(gestion), nombre_mes_es, tomo, filename)
