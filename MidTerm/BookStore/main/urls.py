# from django.urls import path
#
# from .views import BookList,BookDetail
# urlpatterns = [
#     path('books/',BookList.as_view()),
#     path('books/<int:id>', BookDetail.as_view())
# ]
#

from .views import BookListViewSet,JournalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'journals', JournalViewSet)
router.register(r'books', BookListViewSet)

urlpatterns = router.urls
