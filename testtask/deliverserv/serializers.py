from rest_framework import serializers
from deliverserv.models import Product, MyUser, Package


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ( 'url','article', 'manufacturer', 'title', 'barcode',  'price', 'weight')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ('url', 'id', 'username', 'real_name')

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('url', 'id', 'owner', 'products', 'handed', 'price' )
