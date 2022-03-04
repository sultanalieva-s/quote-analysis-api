from rest_framework import serializers

from main.models import Quote, QuoteAnalysis


class QuoteAnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuoteAnalysis
        fields = (
            "total_letters",
            "total_vowels",
            "total_consonants",
            "average_word_length",
            "letter_repetitions",
        )


class QuoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quote
        fields = ("id",
                  "quote",
                  "analysis",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        analysis_pk = representation['analysis']
        representation['analysis'] = QuoteAnalysisSerializer(QuoteAnalysis.objects.get(pk=analysis_pk)).data
        return representation
