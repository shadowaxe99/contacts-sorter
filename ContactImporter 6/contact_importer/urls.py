urlpatterns = [
    path('admin/', admin.site.urls),
    path('import/', include('contact_app.urls')),
]