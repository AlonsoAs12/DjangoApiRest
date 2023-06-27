from rest_framework import serializers
from .models import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('id_prestamo','titulo','nombre_usuario','fec_prestamo','fec_devolucion')

    id_prestamo = serializers.IntegerField(read_only=True)
    nombre_usuario  = serializers.CharField()
    titulo = serializers.CharField()
    fec_prestamo = serializers.DateField()
    fec_devolucion = serializers.DateField()

    def create(self, validated_data):

        return Prestamo.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.id_prestamo = validated_data.get('id_prestamo', instance.id_prestamo)
        instance.nombre_usuario = validated_data.get('nombre_usuario', instance.nombre_usuario)
        instance.titulo=validated_data.get('titulo', instance.titulo)
        instance.fec_prestamo = validated_data.get('fec_prestamo',instance.fec_prestamo)
        instance.fec_devolucion = validated_data.get('fec_prestamo',instance.fec_prestamo)
        instance.save()
        return instance
        