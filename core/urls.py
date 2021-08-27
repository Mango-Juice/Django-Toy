from django.urls import path, include
import core.views

urlpatterns = [

    path('', core.views.test, name='core'),
    path('parameter/', core.views.get_post, name='invited'),
    path('pc/',  core.views.error, name='pc')

]
