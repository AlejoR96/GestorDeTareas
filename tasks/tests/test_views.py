import pytest
from django.urls import reverse
from tasks.models import Task

@pytest.mark.django_db
def test_lista_tasks_view(client, user, tarea):
    client.force_login(user)

    url = reverse("lista_tasks")  # Ajusta el nombre real de tu URL
    response = client.get(url)

    assert response.status_code == 200
    assert b"Tarea de prueba" in response.content


@pytest.mark.django_db
def test_crear_tarea_view(client, user):
    client.force_login(user)

    url = reverse("crear_tarea")  # Ajusta el nombre real
    data = {
        "titulo": "Nueva tarea",
        "descripcion": "Descripción de prueba",
        "completada": False
    }

    response = client.post(url, data)

    assert response.status_code in (200, 302)
    assert Task.objects.filter(titulo="Nueva tarea").exists()
