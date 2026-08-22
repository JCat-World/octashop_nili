from django.contrib import admin

from .infrastructure.models import *

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active',)
    search_fields = ('username', 'email')
    list_filter = ('is_active',)
    # ordering = ('-date_joined',)
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('profile')
    



# class InlineProfileAsset(admin.StackedInline):
#     model = ProfileAsset
#     can_delete = False
#     verbose_name_plural = 'Profile Assets'
#     # readonly_fields = ('type',)
#     fk_name = 'user_profile'
#     extra = 1

# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('id','username', 'telegram_id' ,'referred_by__id')
#     inlines = [InlineProfileAsset]
#     readonly_fields = ('id', 'username', 'telegram_id', 'referred_by', 'wallet_bnb')
    # search_fields = ('user__username', 'user__email')
    # list_filter = ('location',)
    
    # def get_queryset(self, request):
    #     return super().get_queryset(request).select_related('user')
    

    
    
    
    
    
# @admin.register(TelegramProfile)
# class TelegramProfileAdmin(admin.ModelAdmin):
#     list_display = ('telegram_id', 'profile', 'referred_by', 'is_active')
#     search_fields = ('telegram_id', 'profile__username', 'referred_by__telegram_id')
#     list_filter = ('is_active',)
    
#     def get_queryset(self, request):
#         return super().get_queryset(request).select_related('profile')
    
# @admin.register(ProfileAsset)
# class ProfileAssetAdmin(admin.ModelAdmin):
#     list_display = ('user_profile__id','user_profile__telegram_id','user_profile', 'type','amount')
#     # search_fields = ('user_profile__user__username', 'type')
#     list_filter = ('type','user_profile__telegram_id')
    
    # def get_queryset(self, request):
    #     return super().get_queryset(request).select_related('user_profile')
    
# @admin.register(ProfileAssetType)
# class ProfileAssetTypeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type')
#     search_fields = ('name',)
    
    # def get_queryset(self, request):
    #     return super().get_queryset(request).select_related('profile_asset')
    


# @admin.register(ProfileAssetHistory)
# class ProfileAssetHistoryAdmin(admin.ModelAdmin):
#     list_display = ('profile_asset', 'change_type', 'change_amount', 'timestamp')
#     search_fields = ('profile_asset__user_profile__telegram_id', 'change_type__name')
#     list_filter = ('change_type',)


# @admin.register(AssetHistoryType)
# class AssetHistoryTypeAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
