import pytest
from tasks.forms import Task_form

def test_formulario_valido():
    form = Task_form(data={
        "titulo": "Tarea válida",
        "descripcion": "Testing form",
        "estado": "pendiente"
    })

    assert form.is_valid() is True


def test_formulario_invalido_campo_vacio():
    form = Task_form(data={
        "titulo": "",
        "descripcion": "Sin título",
        "estado": "pendiente"
    })

    assert form.is_valid() is False
    assert "titulo" in form.errors
