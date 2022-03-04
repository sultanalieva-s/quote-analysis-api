from rest_framework import serializers

from main.models import Quote, QuoteAnalysis


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ("id",
                  "quote",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['analysis'] = QuoteAnalysisSerializer(QuoteAnalysis.objects.get(quote=instance)).data
        return representation


class QuoteAnalysisSerializer(serializers.ModelSerializer):
    quote = serializers.PrimaryKeyRelatedField(write_only=True, queryset=Quote.objects.all())

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
