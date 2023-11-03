from front_end.views import minha_pagina
from django.urls import include, path

urlpatterns = [
    path("", minha_pagina, name="minha_pagina"),
]
