from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from final.app.serializers import *
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    
    
class EmployeePrivilegesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows EmployeePrivileges to be viewed or edited.
    """
    queryset = EmployeePrivileges.objects.all()
    serializer_class = EmployeePrivilegesSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Employees to be viewed or edited.
    """
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class InventoryTransactionTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows InventoryTransactionTypes to be viewed or edited.
    """
    queryset = InventoryTransactionTypes.objects.all()
    serializer_class = InventoryTransactionTypesSerializer


class InventoryTransactionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows InventoryTransactions to be viewed or edited.
    """
    queryset = InventoryTransactions.objects.all()
    serializer_class = InventoryTransactionsSerializer


class InvoicesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Invoices to be viewed or edited.
    """
    queryset = Invoices.objects.all()
    serializer_class = InvoicesSerializer


class OrderDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderDetails to be viewed or edited.
    """
    queryset = OrderDetails.objects.all()
    serializer_class = OrderDetailsSerializer


class OrderDetailsStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrderDetailsStatus to be viewed or edited.
    """
    queryset = OrderDetailsStatus.objects.all()
    serializer_class = OrderDetailsStatusSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Orders to be viewed or edited.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrdersStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrdersStatus to be viewed or edited.
    """
    queryset = OrdersStatus.objects.all()
    serializer_class = OrdersStatusSerializer


class OrdersTaxStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows OrdersTaxStatus to be viewed or edited.
    """
    queryset = OrdersTaxStatus.objects.all()
    serializer_class = OrdersTaxStatusSerializer


class PrivilegesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Privileges to be viewed or edited.
    """
    queryset = Privileges.objects.all()
    serializer_class = PrivilegesSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Products to be viewed or edited.
    """
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer


class PurchaseOrderDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PurchaseOrderDetails to be viewed or edited.
    """
    queryset = PurchaseOrderDetails.objects.all()
    serializer_class = PurchaseOrderDetailsSerializer


class PurchaseOrderStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PurchaseOrderStatus to be viewed or edited.
    """
    queryset = PurchaseOrderStatus.objects.all()
    serializer_class = PurchaseOrderStatusSerializer


class PurchaseOrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows PurchaseOrders to be viewed or edited.
    """
    queryset = PurchaseOrders.objects.all()
    serializer_class = PurchaseOrdersSerializer


class SalesReportsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SalesReports to be viewed or edited.
    """
    queryset = SalesReports.objects.all()
    serializer_class = SalesReportsSerializer


class ShippersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Shippers to be viewed or edited.
    """
    queryset = Shippers.objects.all()
    serializer_class = ShippersSerializer

class StringsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Strings to be viewed or edited.
    """
    queryset = Strings.objects.all()
    serializer_class = StringsSerializer


class SuppliersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Suppliers to be viewed or edited.
    """
    queryset = Suppliers.objects.all()
    serializer_class = SuppliersSerializer
    
    

