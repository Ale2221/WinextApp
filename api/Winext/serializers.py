from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id_user', 'role', 'id_profile', 'nickname', 'password', 'email', 'created_at', 'updated_at', 'deleted_at']

        
"""
este es un ejemplo de como hacerlas mas personalizadas, arreglar todo eso asi
fields = ['id', 
            'name', 
            'description', 
            'created_at',
            'updated_at',
            'deleted_at',  ]

ademas, se debe colocar validacion de cada uno de los modelos (ver que no se repitan los nombres,
que sean unicos), ademas seguriad.

ejemplo de codigo de valentina: 

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 
                  'name', 
                  'description', 
                  'created_at',
                  'updated_at',
                  'deleted_at',  ]
    def validate_name(self, value):

        if Role.objects.filter(name=value).exists():
            raise serializers.ValidationError("Ya existe un rol con este nombre.")
        return value

    def create(self, validated_data):

        return Role.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    role_id = serializers.IntegerField(write_only=True)  # Asegúrate de agregar este campo write_only

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in value) or not any(char.isalpha() for char in value):
            raise serializers.ValidationError("La contraseña debe ser alfanumérica.")
        return value
    
    def create(self, validated_data):
        role_id = validated_data.pop('role_id')
        validated_data['password'] = make_password(validated_data['password']) 
        user = super().create(validated_data)
        role = Role.objects.get(pk=role_id)
        user.role = role
        user.save()
        return user

    class Meta:
        model = User
        fields = ['id', 
                  'username', 
                  'password', 
                  'email', 
                  'name', 
                  'last_name', 
                  'role_id',
                  'image', 
                  'document', 
                  'address',
                  'phone_number',
                  'is_active',
                  'is_staff',
                  'created_at',
                  'updated_at',
                  'deleted_at',  
                  'role', ]

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 
                  'password', 
                  'email', 
                  'name', 
                  'last_name', 
                  'document', 
                  'address',
                  'phone_number', ]

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not any(char.isdigit() for char in value) or not any(char.isalpha() for char in value):
            raise serializers.ValidationError("La contraseña debe ser alfanumérica.")
        return value

    def create(self, validated_data):
        default_role = Role.objects.get(id=3)
        validated_data['role'] = default_role
        validated_data['password'] = make_password(validated_data['password']) 
        return super(UserRegisterSerializer, self).create(validated_data)
    
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 
                  'name', 
                  'description', 
                  'created_at',
                  'updated_at',
                  'deleted_at',  ]

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Ya existe una categoría con este nombre.")
        return value

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = ['id', 
                  'name', 
                  'description', 
                  'abbreviation', 
                  'created_at',
                  'updated_at',
                  'deleted_at']

    def validate_name(self, value):
        if Units.objects.filter(name=value).exists():
            raise serializers.ValidationError("Ya existe una unidad con este nombre.")
        return value

    def create(self, validated_data):
        return Units.objects.create(**validated_data)
    
class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ['id', 'name', 'description', 'symbol', 'abbreviation', 'created_at', 'updated_at', 'deleted_at']

    def validate_name(self, value):
        if Coin.objects.filter(name=value).exists():
            raise serializers.ValidationError("Ya existe una moneda con este nombre.")
        return value

    def create(self, validated_data):
        return Coin.objects.create(**validated_data)


"""