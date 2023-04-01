from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "o Cpf não é valido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "nao inclua números neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': " o RG deve conter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': " o celular deve seguir esse modelo 11 9999-9999"})
        return data
