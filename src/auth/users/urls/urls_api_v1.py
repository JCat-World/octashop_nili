from django.urls import path

from accounts.interface.api.v1.views_api_v1 import AssetTypeView, TelBotV1Start , WalletAddressRegisterFromTelegram

urlpatterns = [
    path('tel-bot-v1/start/', TelBotV1Start.as_view(), name='tel_bot_v1_start'),
    path('tel-bot-v1/asset-types/', AssetTypeView.as_view(), name='tel_bot_v1_asset_types'),
    path('tel-bot-v1/wallet-bnb-set/', WalletAddressRegisterFromTelegram.as_view(), name='wallet-bnb-set'),
]