import io

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view
from django.http import HttpResponse
from matplotlib import pyplot as plt
from numpy import linspace
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.dto.plot_request import PlotRequest
from server.security.basic_auth import BasicAuth


def generate_plot(data: PlotRequest):
    x = linspace(data.range.a, data.range.b, 400)
    y = data.m * x + data.b

    plt.plot(x, y)
    plt.xlim(data.range.a, data.range.b)

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return buffer.getvalue()


@api_view(['POST'])
def plot_function(request):
    try:
        data = PlotRequest.parse_raw(request.body)
        return HttpResponse(generate_plot(data), content_type='image/png')

    except Exception as e:
        return HttpResponse(str(e), status=400)


class PlotFunctionView(APIView):
    last_plot = None
    authentication_classes = [SessionAuthentication, BasicAuth]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = PlotRequest.parse_raw(request.body)
        PlotFunctionView.last_plot = generate_plot(data)
        return HttpResponse(self.last_plot, content_type='image/png')

    def get(self, request):
        if PlotFunctionView.last_plot is not None:
            return HttpResponse(self.last_plot, content_type='image/png')
        else:
            return Response('No plot has been created yet', status=404)
