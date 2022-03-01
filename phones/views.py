from django.db.models import Q
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from phones.models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = "__all__"


class PhoneViewSet(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    def list(self, request, *args, **kwargs):
        """Добавлены функции для поиска по имени, телефону и сортировка"""

        query = Q()
        # for searching in field name
        if name := request.GET.get('name'):
            query = query | Q(name__iregex=name)

        # for searching in field phone_number
        if phone_number := request.GET.get('phone_number'):
            query = query & Q(phone_number__icontains=phone_number)

        self.queryset = self.queryset.filter(query)

        # ordering
        if order := request.GET.get('ordering'):  # for sorting records retrieved
            self.queryset = self.queryset.order_by(order)

        # if paginated
        if request.GET.get('page'):
            page = self.paginate_queryset(self.queryset)
            serialized = self.serializer_class(page, many=True)
            return Response(serialized.data)

        return Response(self.serializer_class(self.queryset, many=True).data)
