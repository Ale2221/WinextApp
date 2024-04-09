from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from .serializers import *
from .models import User, Role

class UserIndexAPIView(APIView):
    def get(self, request):
        try:
            users = User.objects.all()
            if not users:
                return Response({"error": "No se encontraron usuarios"}, status=404)
            serializer = UserSerializer(users, many=True)
            return Response({"users": serializer.data})
        except ObjectDoesNotExist:
            return Response({"error": "No se encontró el usuario"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)


class RoleIndexAPIView(APIView):
    def get(self, request):
        role = Role.objects.all()
        serializer = RoleSerializer(role, many=True)
        return Response({"Role": serializer.data})
    
# ya tengo index en posmant, necesito crear los post (envios de info), show (mostrar por id = pk, es un get), update (actualizar datos), delete (borrar), restore (recuperar), de cada una de las apis
# ademas, hacer el login register, y log out, 
# hacer validacaion con try y except en el back (api.py)
