import pytest
from tasks.models import Task

@pytest.mark.django_db
def test_crear_tarea(tarea):
    assert tarea.id is not None
    assert tarea.titulo == "Tarea de prueba"
    assert tarea.descripcion == "Descripción de prueba"

@pytest.mark.django_db
def test_actualizar_tarea(tarea):
    tarea.titulo = "Título actualizado"
    tarea.save()

    t_actualizada = Task.objects.get(id=tarea.id)
    assert t_actualizada.titulo == "Título actualizado"
