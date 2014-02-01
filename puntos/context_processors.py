from django.core.urlresolvers import reverse

def menuUser(request):
    menu = {'menuUser': [
    { 'name': 'Dashboard' , 'url': reverse('dashboard')   },
    { 'name': 'Miembros' , 'url': reverse('miembro') },
    { 'name': 'Puntaje' , 'url': reverse('puntaje')    },
    { 'name': 'Reglas' , 'url': reverse('regla')    },
    { 'name': 'Cargos' , 'url': reverse('cargo')    },
    { 'name': 'Historico' , 'url': reverse('historico')    },
    { 'name': 'Recompensas' , 'url': reverse('recompensa')    },
    { 'name': 'Tarjetas' , 'url': reverse('tarjeta')    },
    ]}

    for item in menu['menuUser']:
        if request.path == item['url']:
            item['active'] = True

    return menu
