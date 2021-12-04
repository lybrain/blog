from django.http.response import Http404
from rest_framework import status, mixins, generics
from rest_framework.views import APIView
from about.models import WishMessage
from rest_framework.response import Response
from about.api.serializers import WishMessageSerializer


class WishMessageCreateListView(mixins.ListModelMixin,
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):
    queryset = WishMessage.objects.all()
    serializer_class = WishMessageSerializer

    def get(self, request):
        serializer = WishMessageSerializer(WishMessage.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):  # post
        serializer = self.get_serializer(data=request.data,context={'request_method': request.method})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class WishMessageView(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    queryset = WishMessage.objects.all()
    serializer_class = WishMessageSerializer

    def get_object(self, id):
        try:
            return WishMessage.objects.get(id=id)
        except WishMessage.DoesNotExist:
            raise Http404

    def get(self, request, id):
        wish_msg = self.get_object(id)
        serializer = WishMessageSerializer(wish_msg)
        return Response(serializer.data)

    def put(self, request, id):
        wish_msg = self.get_object(id)
        serializer = WishMessageSerializer(wish_msg, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        wish_msg = self.get_object(id)
        serializer = WishMessageSerializer(
            wish_msg, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        wish_msg = self.get_object(id)
        wish_msg.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
