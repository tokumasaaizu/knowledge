from django.contrib import admin
from django.urls import path,include
from knowledgeapp.views import FirstLogin,TopPage,KnowledgeList,Login,signup,Create,Add,Edit,UpdateData,DeleteData,Detail,MemberList

urlpatterns = [
    path('', FirstLogin, name='first'),
    path('top', TopPage, name='top_page'),
    path('list/', KnowledgeList, name="List"),
    path('login/', Login, name='Login'),
    path('signup/', signup, name='signup'),
    path('create/', Create, name='create'),
    path('add/', Add, name='add'),
    path('edit/<int:pk>', Edit, name='edit'),
    path('update/<int:pk>',UpdateData, name='update'),
    path('delete/<int:pk>',DeleteData, name='delete'),
    path('detail/<int:pk>', Detail, name='detail'),
    path('mem/',MemberList,name='mem'),
]
