from rest_framework import serializers

from main.models import Quote, QuoteAnalysis


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ("quote",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['analysis'] = QuoteAnalysisSerializer(QuoteAnalysis.objects.get(quote=instance)).data

        return representation


class QuoteAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteAnalysis
        fields = (
            "quote",
            "total_letters",
            "total_vowels",
            "total_consonants",
            "average_word_length",
            "letter_repetitions",
        )
