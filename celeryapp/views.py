from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from celeryapp.task import testing_task
# Create your views here.


class HomeView(TemplateView):
    template_name='celeryapp/home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:

        context=super().get_context_data(**kwargs)
        
        # result=testing_task.delay(3,6)
        # or
        result=testing_task.apply_async(args=[3,6],kwargs={},queue='celeryapp')
        
        context['celery_task_result']=result.status

        return context
