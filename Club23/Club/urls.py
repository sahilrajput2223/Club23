from django.urls import path, include
from .views import Home, Bookclub_view, Gallery, Person_grid, Contact_us
app_name='Club'

urlpatterns = [
    path('', Home, name="home"),
    path('bookclub', Bookclub_view, name="bookclub"),
    path('gallery', Gallery, name="gallery"),
    path('person', Person_grid, name="person"),
    path('contact_us', Contact_us, name="contact_us"),

]
