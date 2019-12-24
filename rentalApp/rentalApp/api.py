from rest_framework import routers
from rental.views import BelongingViewset, FriendViewset, BorrowedViewset
# from product.views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'friends', FriendViewset)
router.register(r'belongings', BelongingViewset)
router.register(r'borrowings', BorrowedViewset)