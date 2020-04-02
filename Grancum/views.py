from rest_framework import generics
from Grancum.models import Գրանցում
from django.shortcuts import render
from django.http import HttpResponse
from Grancum.serializers import(
    GrancumCreateSerializer,
    GrancumListSerializer,
    GrancumDetailSerializer
)
# Create your views here.

# class GrancumCreateAPIView(generics.CreateAPIView):
#     serializer_class = GrancumCreateSerializer
#     queryset = Գրանցում.objects.all()
def index(request):
    template = '../templates/Grancum.html'
    return render(request, template)

def create_user(request):
    if request.method == 'POST':
        Ազգանուն = request.POST['Ազգանուն']
        Հայրանուն = request.POST['Հայրանուն']
        Անուն = request.POST['Անուն']

        Գրանցում.objects.create(
            Անուն = Անուն,
            Ազգանուն = Ազգանուն,
            Հայրանուն = Հայրանուն
        )
        return HttpResponse('')
class GrancumListAPIView(generics.ListAPIView):
    serializer_class = GrancumListSerializer
    queryset = Գրանցում.objects.all()

class GrancumDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GrancumDetailSerializer
    queryset = Գրանցում.objects.all()