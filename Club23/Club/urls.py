from django.urls import path, include
from .views import Home, Bookclub_view, Gallery, Person_grid, Contact_us, checkout, faq, all_news, birthdate, marriage, farewell, reception, party, wedding
app_name='Club'

urlpatterns = [
    path('', Home, name="home"),
    path('bookclub', Bookclub_view, name="bookclub"),
    path('gallery', Gallery, name="gallery"),
    path('person', Person_grid, name="person"),
    path('contact_us', Contact_us, name="contact_us"),
    path('checkout', checkout, name="checkout"),
    path('faq', faq, name="faq"),
    path('news', all_news, name="news"),
    path('birthdate', birthdate, name="birthdate"),
    path('marriage', marriage, name="marriage"),
    path('farewell', farewell , name="farewell"),
    path('reception', reception, name="reception"),
    path('party', party, name="party"),
    path('wedding', wedding, name="wedding"),
]
