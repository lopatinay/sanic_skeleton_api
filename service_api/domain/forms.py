import arrow
from marshmallow import Schema, fields, ValidationError


class ArrowField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return value.format()

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return arrow.get(value)
        except ValueError as error:
            raise ValidationError("Pin codes must contain only digits.") from error


class BaseDeserializer(Schema):
    pass


class BaseSerializer(Schema):
    pass
