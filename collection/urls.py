from django.urls import path
from . import views

urlpatterns = [
    path( '', views.render_page )    
]

htmx_urlpatterns = [
    path( 'positive/', views.positive, name='positive' ),
    path( 'negative/', views.negative, name='negative' ),
    path( 'neutral/', views.neutral, name='neutral' ),
    path( 'dontknow/', views.dontknow, name='dontknow' )
]

urlpatterns += htmx_urlpatterns