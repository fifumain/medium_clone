from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # source mean that we can get info from related object
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    email = serializers.EmailField(source="user.email")
    # Methods for fields below
    full_name = serializers.SerializerMethodField(read_only=True)
    profile_photo = serializers.SerializerMethodField()
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            "id",
            "first_name",
            "last_name",
            "full_name",
            "email",
            "profile_photo",
            "country",
            "phone_number",
            "gender",
            "twitter_handle",
            "about_me",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    def get_profile_photo(self, obj):
        return obj.profile_photo.url


# For patch requests in profile object
class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "country",
            "city",
            "twitter_handle",
        ]


# Serializer to show our following list
class FollowingSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")

    class Meta:
        model = Profile
        # All required fields to make it look good, like in X(twitter)
        fields = [
            "first_name",
            "last_name",
            "profile_photo",
            "about_me",
            "twitter_handle",
        ]
