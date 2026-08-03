from rest_framework import serializers
from accounts.models import ProfileAsset, ProfileAssetType, Profile
from utilities.round_numbers import clean_decimal



class ProfileAssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAssetType


class AssetSerializer(serializers.ModelSerializer):
    
    type = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    
    
    def get_type(self, obj):
        return obj.type.type if obj.type else None
    
    def get_amount(self, obj):
        return clean_decimal(obj.amount)
    class Meta:
        model = ProfileAsset
        fields = ["type" , "amount", "assets"]
        
        
class ProfileSerializer(serializers.ModelSerializer):
    # assets = AssetSerializer(many=True, read_only=True)
    assets = serializers.SerializerMethodField()

    
    referred_by = serializers.SerializerMethodField()
    
    
    
    def get_referred_by(self, obj):
        if obj.referred_by:
            return obj.referred_by.telegram_id
        return None

    def get_assets(self, obj):
        assets_list = obj.assets.all()
        return {item.type.type: item.amount for item in assets_list}
    
    
    class Meta:
        model = Profile
        fields = ["id",
                  "username",
                  "telegram_id",
                  "wallet_bnb",
                  "referred_by", 
                  "assets","first_name"]
        
    def update(self, instance, validated_data):
        # اگر آدرس قبلاً ثبت شده باشه، و کاربر دوباره بخواد مقدار بده
        if instance.wallet_bnb:
            raise serializers.ValidationError("Can't change the wallet address")
        
        return super().update(instance, validated_data)





class AssetTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAssetType
        fields = ["id", "type"]
        read_only_fields = ["id", "type"]