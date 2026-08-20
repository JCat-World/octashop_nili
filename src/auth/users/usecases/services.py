from accounts.infrastructure.models import  Profile
from accounts.domain.entities import  ProfileEntity

def get_or_create_profile(profile_entity: ProfileEntity):
    profile , profile_created = Profile.objects.get_or_create(
        telegram_id=profile_entity.telegram_id,
        
        defaults={
            'username': profile_entity.username,
            'first_name': profile_entity.first_name,
            'last_name': profile_entity.last_name,
            'phone_number':profile_entity.phone_number,
            'referred_by': Profile.objects.get(telegram_id=profile_entity.referred_by) if profile_entity.referred_by else None,
        }
    )
    return profile, profile_created









# def get_or_create_telegram_profile(user_entity: TelegramProfileEntity):
#     user , created = TelegramProfile.objects.get_or_create(
#         telegram_id=user_entity.telegram_id,
#         profile =user_entity.profile,
#         defaults={
#             'telegram_username': user_entity.telegram_username,
#             'referred_by': user_entity.referred_by,
#         }
#     )
#     return user, created