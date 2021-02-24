from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name'] 


class CustomersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customers
        fields =  '__all__'
        extra_fields = ['url']
        
class EmployeePrivilegesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EmployeePrivileges
        fields =  '__all__'
        extra_fields = ['url']


class InventoryTransactionTypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryTransactionTypes
        fields =  '__all__'
        extra_fields = ['url']
        
        
class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields =  '__all__'
        extra_fields = ['url']


class InventoryTransactionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InventoryTransactions
        fields =  '__all__'
        extra_fields = ['url']


class InvoicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoices
        fields =  '__all__'
        extra_fields = ['url']


class OrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetails
        fields =  '__all__'
        extra_fields = ['url']


class OrderDetailsStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetailsStatus
        fields =  '__all__'
        extra_fields = ['url']


class OrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields =  '__all__'
        extra_fields = ['url']
        
        
class OrdersStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdersStatus
        fields =  '__all__'
        extra_fields = ['url']
        
        
class OrdersTaxStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdersTaxStatus
        fields =  '__all__'
        extra_fields = ['url']
        
        
class PrivilegesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Privileges
        fields =  '__all__'
        extra_fields = ['url']
        
        
class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields =  '__all__'
        extra_fields = ['url']
        
        
class PurchaseOrderDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrderDetails
        fields =  '__all__'
        extra_fields = ['url']                                                        
        
        
class PurchaseOrderStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrderStatus
        fields =  '__all__'
        extra_fields = ['url']
        
        
class PurchaseOrdersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseOrders
        fields =  '__all__'
        extra_fields = ['url'] 
        

class ShippersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shippers
        fields = '__all__' 
        extra_fields = ['url'] 
        
        
class StringsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Strings
        fields = '__all__' 
        extra_fields = ['url'] 
        
        
class SuppliersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Suppliers
        fields = '__all__' 
        extra_fields = ['url'] 
        

class SalesReportsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SalesReports
        fields = '__all__' 
        extra_fields = ['url'] 