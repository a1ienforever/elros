from rest_framework import serializers

from Car.models import Car, Manufacturer, Country, Comment


class CommentSerializer(serializers.ModelSerializer):
    car_name = serializers.CharField(source="car.name", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "email", "car", "car_name", "comment")

    @staticmethod
    def validate_text(value):
        if len(value) < 5:
            raise serializers.ValidationError("Комментарий слишком короткий")
        if len(value) > 255:
            raise serializers.ValidationError("Комментарий слишком длинный")
        return value


class CarDetailSerializer(serializers.ModelSerializer):
    manufacturer_name = serializers.CharField(
        source="manufacturer.name", read_only=True
    )
    comments = CommentSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "manufacturer",
            "manufacturer_name",
            "date_created",
            "date_finished",
            "comments_count",
            "comments",
        )

    @staticmethod
    def get_comments_count(obj):
        return obj.comments.count()


class CarsSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ("name", "comments_count")

    @staticmethod
    def get_comments_count(obj):
        return obj.comments.count()


class ManufacturerSerializer(serializers.ModelSerializer):
    country_name = serializers.CharField(source="country.name", read_only=True)
    cars = CarsSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = (
            "id",
            "name",
            "country",
            "country_name",
            "cars",
        )


class CountrySerializer(serializers.ModelSerializer):
    manufacturers = ManufacturerSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ("id", "name", "manufacturers")


class ExportCarSerializer(serializers.ModelSerializer):
    manufacturer_name = serializers.CharField(
        source="manufacturer.name", read_only=True
    )
    comments_count = serializers.SerializerMethodField()
    country_name = serializers.CharField(source="country.name", read_only=True)


    class Meta:
        model = Car
        fields = (
            "id",
            "name",
            "manufacturer_name",
            "country_name",
            "date_created",
            "date_finished",
            "comments_count",
        )

    @staticmethod
    def get_comments_count(obj):
        return obj.comments.count()
