from django.urls import path
import core.views

urlpatterns = [

    path('', core.views.test, name='core'),
    path('parameter/', core.views.get_post, name='invited'),
    path('result/',  core.views.result, name='result'),
    path('pc/',  core.views.pc, name='pc'),
    path('unknown/',  core.views.unknown, name='unknown'),
    path('create/',  core.views.create, name='create'),
    path('submit/',  core.views.submit, name='submit'),

]
