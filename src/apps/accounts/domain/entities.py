from dataclasses import dataclass
from accounts.infrastructure.models import Profile


@dataclass
class ProfileEntity:
    referred_by: Profile = None
    is_active: bool = True
