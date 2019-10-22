from django.urls import path

from . import views

urlpatterns = [
    path('', views.PlanAList.as_view(), name='PlanA_list'),
    path('view/<int:pk>', views.PlanAView.as_view(), name='PlanA_view'),
    path('new', views.PlanACreate.as_view(), name='PlanA_new'),
    path('view/<int:pk>', views.PlanAView.as_view(), name='PlanA_view'),
    path('edit/<int:pk>', views.PlanAUpdate.as_view(), name='PlanA_edit'),
    path('delete/<int:pk>', views.PlanADelete.as_view(), name='PlanA_delete'),
    path('item/', views.Item_planList.as_view(), name='Item_plan_list'),
    path('item/view/<int:pk>', views.Item_planView.as_view(), name='Item_plan_view'),
    path('item/new', views.Item_planCreate.as_view(), name='Item_plan_new'),
    path('item/view/<int:pk>', views.Item_planView.as_view(), name='Item_plan_view'),
    path('item/edit/<int:pk>', views.Item_planUpdate.as_view(), name='Item_plan_edit'),
    path('item/delete/<int:pk>', views.Item_planDelete.as_view(), name='Item_plan_delete'),
]