from django.http import JsonResponse
from .service import upgrade_grid
from .models import Cells
from .serializers import CellSerializer


def update(request):
    if request.method == 'GET':
        upgrade_grid()
        cells = Cells.objects.all()
        serializer = CellSerializer(cells, many=True)
        return JsonResponse(serializer.data, safe=False)

