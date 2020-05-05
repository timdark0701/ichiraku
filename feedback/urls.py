from django.urls import path
from .views import FeedBackView
from .views import FeedbackDetails
# from .views import FeedbackAPIView
from . import views

urlpatterns = [
    path('', FeedBackView.as_view(), name='feedback_view'),
    path('<int:id>/', FeedbackDetails.as_view())
]
