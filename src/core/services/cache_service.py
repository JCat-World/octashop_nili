# core/services/cache_service.py
class CacheService:
    def set(self, key: str, value: str, timeout: int):
        raise NotImplementedError

    def get(self, key: str):
        raise NotImplementedError

    def delete(self, key: str):
        raise NotImplementedError
