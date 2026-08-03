from rest_framework_simplejwt.authentication import JWTAuthentication

class HybridJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # اول از هدر بخونه (مثل قبل)
        header_result = super().authenticate(request)
        if header_result is not None:
            return header_result

        # بعد از کوکی بخونه (برای رندر سمت سرور)
        raw_token = request.COOKIES.get("access_token")
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token
