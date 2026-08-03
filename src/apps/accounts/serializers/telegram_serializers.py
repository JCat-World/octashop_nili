from rest_framework import serializers

from accounts.infrastructure.models import Profile


class TelegramProfileValidatorSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField()
    username = serializers.CharField(max_length=255, required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    api_key = serializers.CharField(write_only =True)
    # referred_by = serializers.ModelField(
    #     model_field='accounts.Profile',
    #     required=False, allow_null=True
    # )
    referred_by = serializers.IntegerField(required=False, allow_null=True)
    phone_number = serializers.CharField(max_length=20, required=False, allow_blank=True)
    
    # class Meta:
        # model = 'accounts.Profile'
        # fields = ('telegram_id', 'username', 'phone_number')
        # read_only_fields = ('id', 'user')
    
    
    
class ProfileInfoSerializer(serializers.ModelSerializer):
    
    referred_by = serializers.SerializerMethodField()
    
    
    def get_referred_by(self, obj):
        return obj.referred_by.telegram_id
    

    class Meta:
        model = Profile
        fields = ('telegram_id', 'username', 'first_name', 'last_name', 'phone_number','referred_by',)
        # read_only_fields = ('tpt_balance', 'game_ticket', 'wallet_address')


class TelegramProfileSerializer(serializers.Serializer):
    telegram_id = serializers.IntegerField()
    username = serializers.CharField(max_length=255, required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
    api_key = serializers.CharField(write_only =True)
    referred_by_id = serializers.IntegerField(required=False, allow_null=True)
    phone_number = serializers.CharField(max_length=20, required=False, allow_blank=True)
    
    


# class TelegramUserInfoSerializer(serializers.Serializer):
#     telegram_id = serializers.IntegerField()
#     username = serializers.CharField(max_length=255, required=False, allow_blank=True)
#     first_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
#     last_name = serializers.CharField(max_length=255, required=False, allow_blank=True)
#     phone_number = serializers.CharField(max_length=20, required=False, allow_blank=True)
#     tpt_balance = serializers.DecimalField(max_digits=30, decimal_places=18,required=False,)
#     game_ticket = serializers.IntegerField(required=False,)
#     wallet_address = serializers.CharField(max_length=100, required=False, allow_blank=True)
    
    
#     class Meta:
#         model: TelegramUser
#         fields = ('telegram_id', 'username', 'first_name', 'last_name', 'phone_number', 'tpt_balance', 'game_ticket', 'wallet_address')
#         read_only_fields = ('tpt_balance', 'game_ticket', 'wallet_address')