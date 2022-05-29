from django.urls import path
from . import views

urlpatterns =[

	path('', views.apiOverview, name = "api-overview"),
	path('birthday-list', views.BirthdayList, name = "birthday-list"),
	path('birthday-detail/<str:pk>', views.BirthdayDetail, name = "birthday-detail"),
	path('birthday-create', views.BirthdayCreate, name = "birthday-create"),
	path('birthday-update/<str:pk>/', views.BirthdayUpdate, name = "birthday-update"),
	path('birthday-delete/<str:pk>/', views.BirthdayDelete, name = "birthday-delete"),



	path('mothersday-list', views.MothersDayList, name = "mothersday-list"),
	path('mothersday-detail/<str:pk>', views.MothersDayDetail, name = "mothersday-detail"),
	path('mothersday-create', views.MothersDayCreate, name = "mothersday-create"),
	path('mothersday-update/<str:pk>/', views.MothersDayUpdate, name = "mothersday-update"),
	path('mothersday-delete/<str:pk>/', views.MothersDayDelete, name = "mothersday-delete"),

	
	path('relanni-list', views.RelationshipAnniversaryList, name = "relanni-list"),
	path('relanni-detail/<str:pk>', views.RelationshipAnniversaryDetail, name = "relanni-detail"),
	path('relanni-create', views.RelationshipAnniversaryCreate, name = "relanni-create"),
	path('relanni-update/<str:pk>/', views.RelationshipAnniversaryUpdate, name = "relanni-update"),
	path('relanni-delete/<str:pk>/', views.RelationshipAnniversaryDelete, name = "relanni-delete"),



	path('marranni-list', views.MarriageAnniversaryList, name = "marranni-list"),
	path('marranni-detail/<str:pk>', views.MarriageAnniversaryDetail, name = "marranni-detail"),
	path('marranni-create', views.MarriageAnniversaryCreate, name = "marranni-create"),
	path('marranni-update/<str:pk>/', views.MarriageAnniversaryUpdate, name = "marranni-update"),
	path('marranni-delete/<str:pk>/', views.MarriageAnniversaryDelete, name = "marranni-delete"),
]