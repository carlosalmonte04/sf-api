from rest_framework import viewsets
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
import csv
import urllib
import ssl

class CSVParserViewSet(viewsets.ViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  permission_classes = (AllowAny,)
  
  def create(self, request):
    print(request.data)
    csvFile = urllib.request.urlopen(request.data['CSVUrl'])
    csvRawData = csvFile.read()
    parsedCsv = self.csv_parser(csvRawData, request.data['CSVType'])


    return JsonResponse(parsedCsv)

  # helpers
  def csv_parser(self, csvRawData, csvType): # type: 'companies || score-records'

    csvRows = csvRawData.decode().splitlines()

    hashedCsv = {}
    attributes = []
    i = 0

    if csvType == 'companies':
      for row in csvRows:
        if i == 0:
          pass
        else:
          cells = row.split(",")
          key = cells[0]
          value = cells[1]
          hashedCsv[key] = {
            'fractalIndex': value
          }
        i += 1
    if csvType == 'score-records':
      for row in csvRows:
        if i == 0:
          pass
        else:
          cells = row.split(",")
          key = cells[0]
          hashedCsv[key] = {
            'communicationScore': cells[1],
            'codingScore': cells[2],
            'title': cells[3],
            'companyId': cells[4]
          }
        i += 1
    return hashedCsv




