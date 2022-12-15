from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rank
from .serializer import RankSerializer
from rankapp.funcs import rank as rnk

class RankView(APIView):
    def get(self, request, cols, rows, args):
        rank = Rank(cols, rows, args, rnk(cols, rows, args))
        serializer_for_request = RankSerializer(instance=rank)
        return Response(serializer_for_request.data)