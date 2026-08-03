from django.db import models


class UpperCaseCharField(models.CharField):
    """
    A custom CharField that automatically converts input to uppercase.
    """
    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is not None:
            return value.upper()
        return value
      
    def from_db_value(self, value, *args, **kwargs):
        
        return self.to_python(value)
      
    def to_python(self, value):
        value = super().to_python(value)
        if isinstance(value, str):
            return value.upper()
        return value