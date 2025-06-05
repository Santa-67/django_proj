from rest_framework import serializers
from .models import Trade


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"

    # Validate ticker (example: only allow uppercase letters and max length of 10)
    def validate_ticker(self, value):
        if not value.isalpha() or not value.isupper():
            raise serializers.ValidationError("Ticker must be uppercase letters only.")
        if len(value) > 10:
            raise serializers.ValidationError(
                "Ticker length must not exceed 10 characters."
            )
        return value

    # Validate price (must be non-negative)
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be non-negative.")
        return value

    # Validate quantity (must be greater than 0)
    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity must be greater than 0.")
        return value

    # Validate side (must be either 'buy' or 'sell')
    def validate_side(self, value):
        if value not in ["buy", "sell"]:
            raise serializers.ValidationError("Side must be either 'buy' or 'sell'.")
        return value
