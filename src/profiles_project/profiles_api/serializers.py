from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializers a name firld for testing our APIView"""

    name = serializers.CharField(max_length=10)

    
