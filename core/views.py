from rest_framework.generics import ListAPIView, RetrieveAPIView
from core.serializer import ProductSerializer
from core.models import Product, Rating
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django.core.exceptions import ObjectDoesNotExist


@permission_classes((AllowAny, ))
class ProductList(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


@permission_classes((AllowAny, ))
class RatingGet(RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        product_id = kwargs.get("id")

        try:
            Product.objects.get(id=product_id)
        except ObjectDoesNotExist as e:
            return Response({"success": False, "status_code": 404, "message": e.__str__()}, status=404)

        ratings = Rating.objects.all().filter(productMap__product_id=product_id)
        rating_sum = 0
        for i in ratings:
            rating_sum += i.rating

        return Response({
             "product_id": product_id,
             "no_of_ratings": len(ratings),
             "avg_rating": rating_sum/len(ratings)
         })

