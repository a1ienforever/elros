import csv
from io import BytesIO, StringIO

from openpyxl import Workbook
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Car, Country, Manufacturer, Comment
from .permissions import UpdateDeleteOrCreateRead
from .serializers import (
    CarDetailSerializer,
    CountrySerializer,
    ManufacturerSerializer,
    ExportCarSerializer, CommentSerializer, )


# Create your views here.


class CarApiViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CountryApiViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ManufacturerApiViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentApiViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = (UpdateDeleteOrCreateRead,)


class ExportView(APIView):
    def get(self, request, file_format):
        cars = Car.objects.all()
        serializer = ExportCarSerializer(cars, many=True)

        if file_format == "xlsx":
            buffer = BytesIO()
            wb = Workbook()
            ws = wb.active
            ws.title = "Cars"
            ws.append(list(serializer.data[0].keys()))
            for car in serializer.data:
                ws.append(list(car.values()))
            wb.save(buffer)
            buffer.seek(0)
            content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            filename = "cars.xlsx"
        else:
            buffer = StringIO()
            writer = csv.writer(buffer)
            writer.writerow(list(serializer.data[0].keys()))
            for car in serializer.data:
                writer.writerow(list(car.values()))
            content_type = 'text/csv'
            filename = "cars.csv"

        response = HttpResponse(buffer.getvalue(), content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        return response

