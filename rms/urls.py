from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryModelViewSet, basename='category')
# router.register('category', CategoryDetailViewSet, basename='category-detail')

# Viewset:
urlpatterns = [
    # path('category/', CategoryViewSet.as_view({'get':'list','post':'create'})),
    # path('category/<pk>/', CategoryDetailViewSet.as_view({'get':'retrieve','put':'update','patch':'partial_update','delete':'destroy'})),
] + router.urls

# ---------------------------------------------------------------------------------

# Mixins:
# urlpatterns = [
#     path('category/', CategoryGenericAPIView.as_view()),
#     path('category/<pk>/', CategoryDetail.as_view())
# ]

# ---------------------------------------------------------------------------------

# class based 
# urlpatterns = [
#     path('category/', CategoryAPIView.as_view()),
#     path('category/<id>/', CategoryDetail.as_view()),
# ]

# ---------------------------------------------------------------------------------

# function based 
# urlpatterns = [
#     path('category/', category),
#     path('category/<id>/', category_detail),
#     path('table/', table),
#     path('table/<id>/', table_detail),
# ]