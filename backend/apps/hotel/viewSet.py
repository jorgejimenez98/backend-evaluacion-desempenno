from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import IntegrityError
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import HotelSerializer, Hotel
from backend import utils


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all().order_by('-pk')
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            Hotel.objects.create(
                name=data.get('name'),
                pos_db_name=data.get('pos_db_name'),
                pms_db_name=data.get('pms_db_name'),
                zunPrUnidadOrganizativaId=data.get('zunPrUnidadOrganizativaId'),
            )
            return Response({'Hotel Created Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            message = utils.getUniqueHotelErrorMessage(data['name'])
            return Response({'detail': message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def deleteHotels(self, request):
        try:
            for hotel in request.data:
                Hotel.objects.get(pk=hotel.get('id')).delete()
            return Response({'Hotels Eliminated Successfully'}, status=status.HTTP_200_OK)
        except IntegrityError:
            return Response({'detail': utils.getDeleteErrorMessage('Hotel')}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getHotelsWithOutPermission(request):
    try:
        hotels = Hotel.objects.all()
        return Response(HotelSerializer(hotels, many=True).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getHotelWithOutPermission(request, pk):
    try:
        hotel = Hotel.objects.get(pk=pk)
        return Response(HotelSerializer(hotel, many=False).data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'detail': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
