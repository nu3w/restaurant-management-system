from django.urls import path
from .views import *

# Mixins:
urlpatterns = [
    path('category/', CategoryGenericAPIView.as_view()),
    path('category/<pk>/', CategoryDetail.as_view())
]

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