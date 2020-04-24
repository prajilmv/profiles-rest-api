from rest_framework import serializers

class HelloSerilizers(serializers.Serializer):
    """serializers a name field for testing api view"""
    name = serializers.CharField(max_length=10)
        
