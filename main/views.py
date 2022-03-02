import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class GetQuotesView(APIView):

    def get(self, request):
        quotes_api_url = 'https://api.kanye.rest/'
        counter = 10
        quotes = []

        while counter:
            response = requests.get(url=quotes_api_url).json()
            quote = response.get('quote')

            quotes.append(quote)
            counter -= 1

        return Response({"quotes": quotes}, status=status.HTTP_200_OK)
