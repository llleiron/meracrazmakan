from django.urls import path
from Grancum.views import(
    GrancumDetailAPIView,
    GrancumListAPIView
)

urlpatterns = [
    # path('create', 'Grancum.views.create_user'),
    path('list', GrancumListAPIView.as_view()),
    path('detail/<int:pk>', GrancumDetailAPIView.as_view())
]