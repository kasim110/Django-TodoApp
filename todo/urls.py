from django.urls import path,include
from todo import views
app_name = "todo"

urlpatterns = [
    path("todo-list/",views.TodoTaskListView.as_view(),name="todo-list"),
    path("create-todo/",views.TodoTaskCreateView.as_view(),name="todo-create"),
    path("update-todo/<int:pk>/",views.TodoTaskUpdateView.as_view(),name="todo-update"),
    path("<int:pk>/complete/",views.TodoTaskCompletedUpdateView.as_view(),name="todo-completed"),
    path("<int:pk>/reschedule/",views.TodoTaskRescheduleUpdateView.as_view(),name="todo-completed"),
    path("delete-todo/<int:pk>/",views.TodoTaskDeleteView.as_view(),name="todo-delete"),
    path('searchByTitle/', views.TodoTaskSearchbyTitleView.as_view(), name='search-by-title'),
    path('searchByDate/', views.TodoTaskSearchbyDateView.as_view(), name='search-by-date'),
]