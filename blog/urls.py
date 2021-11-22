"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main.views import index
from about.views import about
from article.views import article_create, article_delete, article_edit, article_get
from comment.views import create_comment
from blog import settings
from django.conf.urls.static import static
from user.views import login, registration, logout
from rest_framework import routers, permissions
from about.api.urls import wish_message_router
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from about.api.views_mixin import WishMessageCreateListView, WishMessageView


router = routers.DefaultRouter()
router.registry.extend(wish_message_router.registry)

urlpatterns = [
    path('api/wish_message/<int:id>/', WishMessageView.as_view(), name='WishMessage'),
    path('api/wish_message/', WishMessageCreateListView.as_view(), name='WishMessage'),
    # path('api/', include(router.urls)),
    path('login/', login, name='user_login'),
    path('logout/', logout, name='user_logout'),
    path('registration/', registration, name='user_registration'),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('<int:page>', index, name='index'),
    path('article/create/', article_create, name='article_create'),
    path('article/get/<int:id>/', article_get, name='article_get'),
    path('article/edit/<int:id>/', article_edit, name='article_edit'),
    path('article/delete/<int:id>/', article_delete, name='article_delete'),
    path('article/<int:article_id>/comment/create/',
         create_comment, name='article_comment'),
    path('about/', about, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


schema_view = get_schema_view(
    openapi.Info(
        title="Blog",
        default_version='v1',
        url='localhost:8000',
        description="Blog",
        terms_of_service="",
        contact=openapi.Contact(email="www.librain@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = urlpatterns + [
    path(r'api/swagger/', schema_view.with_ui('swagger',
         cache_timeout=5), name='schema-swagger-ui'),
    path(r'api/redoc/', schema_view.with_ui('redoc',
         cache_timeout=5), name='schema-redoc-ui'),

]
