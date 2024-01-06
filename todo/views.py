from django.shortcuts import render
from rest_framework import generics,status,mixins
from rest_framework.response import Response
from todo.models import TodoTaskModel
from todo import serializers as todo_serializer
from datetime import datetime


class TodoTaskListView(generics.ListAPIView):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_authenticated:
            queryset = TodoTaskModel.objects.filter(user=current_user)
        else:
            queryset = TodoTaskModel.objects.all()        
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response_data = {"success": True,"data": serializer.data}
        return Response(response_data,status=status.HTTP_200_OK)


class TodoTaskCreateView(generics.CreateAPIView):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskSerializer

    def get_serializer_context(self):
        return {
            "request":self.request,
            "args" : self.args,
            "kwargs" : self.kwargs
        }
    def perform_create(self, serializer):
        current_user = self.request.user
        if current_user.is_authenticated:
            # Set the current user as the creator of the task before saving
            serializer.save(user=self.request.user)

class TodoTaskUpdateView(generics.UpdateAPIView,mixins.RetrieveModelMixin):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class TodoTaskDeleteView(generics.DestroyAPIView):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"success": True,'message': 'Record deleted successfully.'},status=status.HTTP_200_OK)
    
class TodoTaskCompletedUpdateView(generics.UpdateAPIView,mixins.RetrieveModelMixin):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskCompletedSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

class TodoTaskRescheduleUpdateView(generics.UpdateAPIView,mixins.RetrieveModelMixin):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskRescheduleSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  

class TodoTaskSearchbyTitleView(generics.ListAPIView):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskSerializer

    def get_queryset(self):
        title = self.request.query_params.get('title','')
        queryset = TodoTaskModel.objects.filter(title__icontains=title)
  
        return queryset


class TodoTaskSearchbyDateView(generics.ListAPIView):
    queryset = TodoTaskModel.objects.all()
    serializer_class = todo_serializer.TodoTaskSerializer

    def get_queryset(self):
        start_date = self.request.query_params.get('start_date', '')
        end_date = self.request.query_params.get('end_date', '')

        # Convert start_date and end_date strings to actual datetime objects
        start_datetime = datetime.strptime(start_date, "%d-%m-%Y")
        end_datetime = datetime.strptime(end_date, "%d-%m-%Y")


        queryset = TodoTaskModel.objects.filter(
            scheduled_at__date__range=(start_datetime.date(), end_datetime.date()))
  
        return queryset
