import requests
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Quote
from main.quote_analysis import (
    count_total_vowels_consonants,
    count_average_word_length,
    get_longest_words,
    count_repetitions,
)
from main.serializers import QuoteSerializer, QuoteAnalysisSerializer


class GetQuotesView(APIView):
    @swagger_auto_schema(responses={200: QuoteSerializer(many=True)})
    def get(self, request):
        quotes_api_url = "https://api.kanye.rest/"
        counter = 10
        quotes = []

        while counter:
            response = requests.get(url=quotes_api_url).json()
            quote = response.get("quote")

            quote_serializer = QuoteSerializer(data=response)

            if quote_serializer.is_valid():
                quote_object = quote_serializer.save()

                total_letters = count_total_vowels_consonants(quote)
                avg = count_average_word_length(quote)
                longest_words = get_longest_words(quote)
                repetitions = count_repetitions(quote)

                quote_analysis_serializer = QuoteAnalysisSerializer(
                    data={
                        "quote": quote_object.id,
                        "total_letters": total_letters["total_letters"],
                        "average_word_length": avg,
                        "total_vowels": total_letters["total_vowels"],
                        "total_consonants": total_letters["total_consonants"],
                        "letter_repetitions": repetitions,
                        "longest_words": longest_words,
                    }
                )

                if quote_analysis_serializer.is_valid(raise_exception=True):
                    quote_analysis_serializer.save()
                    quotes.append(quote_object)
            else:
                quotes.append(Quote.objects.get(quote=quote))

            counter -= 1
        return Response(
            QuoteSerializer(quotes, many=True).data, status=status.HTTP_200_OK
        )
