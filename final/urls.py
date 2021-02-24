from django.urls import path, include
from rest_framework import routers
from final.app import views
from django.contrib import admin

# NOTE: Routers are used with ViewSets in django rest framework to auto config the urls. 
# Routers provides a simple, quick and consistent way of wiring ViewSet logic to a set of URLs. 
# Router automatically maps the incoming request to proper viewset action based on the request method type(i.e GET, POST, etc).
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'customers',views.CustomersViewSet)
router.register(r'employeeprivileges',views.EmployeePrivilegesViewSet)
router.register(r'employees',views.EmployeesViewSet)
router.register(r'inventorytransationtypes',views.InventoryTransactionTypesViewSet)
router.register(r'inventorytransactions',views.InventoryTransactionsViewSet)
router.register(r'invoices',views.InvoicesViewSet)
router.register(r'orderdetails',views.OrderDetailsViewSet)
router.register(r'orderdetailsstatus',views.OrderDetailsStatusViewSet)
router.register(r'orders',views.OrdersViewSet)
router.register(r'ordersstatus',views.OrdersStatusViewSet)
router.register(r'orderstaxstatus',views.OrdersTaxStatusViewSet)
router.register(r'privileges',views.PrivilegesViewSet)
router.register(r'products',views.ProductsViewSet)
router.register(r'purchaseorderdetails',views.PurchaseOrderDetailsViewSet)
router.register(r'purchaseorderstatus',views.PurchaseOrderStatusViewSet)
router.register(r'purchaseorders',views.PurchaseOrdersViewSet)
router.register(r'salesreports',views.SalesReportsViewSet)
router.register(r'shippers',views.ShippersViewSet)
router.register(r'strings',views.StringsViewSet)
router.register(r'suppliers',views.SuppliersViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]