from django.urls import path

from todo import views
from todo.views import CreateItem, ItemList, GetPutDeleteView

urlpatterns = [

    path('create', CreateItem.as_view()),
    path('itemlist', ItemList.as_view()),
    path('get_put_delete_view/<int:pk>', GetPutDeleteView.as_view())
    ]