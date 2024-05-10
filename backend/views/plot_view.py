import io
import json

from rest_framework.decorators import api_view
from django.http import HttpResponse
from matplotlib import pyplot as plt
from numpy import linspace
from rest_framework.response import Response
from rest_framework.views import APIView


def generate_plot(data):
    m = float(data['m'])
    b = float(data['b'])
    a = float(data['range']['a'])
    b_range = float(data['range']['b'])

    x = linspace(a, b_range, 400)
    y = m * x + b

    plt.plot(x, y)
    plt.xlim(a, b_range)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return buffer.getvalue()


@api_view(['POST'])
def plot_function(request):
    try:
        data = json.loads(request.body)
        return HttpResponse(generate_plot(data), content_type='image/png')

    except Exception as e:
        return HttpResponse(str(e), status=400)


class PlotFunctionView(APIView):
    last_plot = None

    def post(self, request):
        data = json.loads(request.body)
        PlotFunctionView.last_plot = generate_plot(data)
        return HttpResponse(self.last_plot, content_type='image/png')

    def get(self, request):
        if PlotFunctionView.last_plot is not None:
            return HttpResponse(self.last_plot, content_type='image/png')
        else:
            return Response('No plot has been created yet', status=404)
