import django_filters
from rest_framework import  viewsets, status, permissions
from rest_framework.decorators import action
from about.models import WishMessage
from rest_framework.response import Response
from about.api.serializers import WishMessageSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class WishMessageFilter(django_filters.FilterSet):
    class Meta:
        model = WishMessage
        fields = {
            'created_date': ('lte', 'gte'),
            'email': ('exact',),
            'allow_mailing': ('exact',)
        }

class WishMessageViewSet(viewsets.ModelViewSet):
    queryset = WishMessage.objects.all()
    serializer_class = WishMessageSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['allow_mailing', 'email', 'created_date']
    search_fields = ['first_name', 'last_name','email']
    # filter_class = WishMessageFilter # custom filter class

    def list(self, request, *args, **kwargs):  # get
        # serializer = self.serializer_class(self.queryset, many=True)
        # Response(serializer.data)
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None):  # get
        msg_obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(msg_obj)
        return Response(serializer.data)

    def create(self, request):  # post
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#     def perform_create(self, serializer):
#         saved_obj = serializer.save()
#         # send mail to saved_obj.email

    def update(self, request, pk=None):  # put
        msg_obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(data=request.data, instance=msg_obj)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

#     def perform_update(self, serializer):
#         serializer.update()

    def partial_update(self, request, pk=None):  # patch
        msg_obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.get_serializer(
            data=request.data, instance=msg_obj, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    def destroy(self, request, pk=None):  # delete
        instance = get_object_or_404(self.queryset, pk=pk)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

#     def perform_destroy(self, instance):
#         pass

    @action(detail=True, methods=['post'], permission_classes=[permissions.AllowAny], url_path='unsub')
    def unsub_from_mailing(self, request, email):
        wish_msg_obj = WishMessage.objects.get(email=email)
        if wish_msg_obj:
            wish_msg_obj.allow_mailing = False
            wish_msg_obj.save()
            return Response("You unsubscribed successfully!", status=status.HTTP_200_OK)
        else:
            return Response("No data with this email!", status=status.HTTP_400_BAD_REQUEST)
