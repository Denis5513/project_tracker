from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    #Function-Based Views
    
    # path('', views.index, name='index'),
    # path('bugs/', views.bug_list, name='bug_list'),
    # path('features/', views.feature_list, name='feature_list'),
    # path('bugs/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('features/<int:feature_id>/', views.feature_detail, name='feature_detail'),
    # path('bugs/new', views.create_bug_report, name='create_bug'),
    # path('features/new', views.create_feature_request, name='create_feature'),
    # path('bugs/<int:bug_id>/update', views.update_bug_report, name='bug_update'),
    # path('features/<int:feature_id>/update', views.update_feature_request, name='feature_update'),
    # path('bugs/<int:bug_id>/delete', views.delete_bug_report, name='bug_delete'),
    # path('feature/<int:feature_id>/delete', views.delete_feature_request, name='feature_delete'),

    #Class-Based Views
    
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugListView.as_view(), name='bug_list'),
    path('features/', views.FeatureListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/new', views.BugCreateView.as_view(), name='create_bug'),
    path('features/new', views.FeatureCreateView.as_view(), name='create_feature'),
    path('bugs/<int:bug_id>/update', views.BugUpdateView.as_view(), name='bug_update'),
    path('features/<int:feature_id>/update', views.FeatureUpdateView.as_view(), name='feature_update'),
    path('bugs/<int:bug_id>/delete', views.BugDeleteView.as_view(), name='bug_delete'),
    path('feature/<int:feature_id>/delete', views.FeatureDeleteView.as_view(), name='feature_delete')
]