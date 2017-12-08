from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
import csv
import urllib

class CSVParserViewSet(viewsets.ViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  permission_classes = (AllowAny,)
  
  def create(self, request):
    csvFile = urllib.request.urlopen(request.data['CSVUrl'])
    csvData = csv.reader(csvFile)
    for row in csvData:
      print(row)

    return JsonResponse({'hello': 'bye'})