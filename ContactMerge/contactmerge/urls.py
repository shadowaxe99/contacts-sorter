urlpatterns = [
    path('admin/', admin.site.urls),
    path('merge/', views.merge_contacts, name='merge_contacts'),
]