from marshmallow import Schema, fields, validate


class DistrictSchema(Schema):

    id = fields.UUID(required=True,
                     error_messages={
                         "invalid_uuid": "Invalid data for UUID",
                         "required": "Field is required",
                         "null": "Field can not be null"})

    name = fields.Str(required=True,
                      error_messages={"required": "Field is required"},
                      validate=[
                          validate.Length(min=2, max=100,
                                          error=
                                          'Field must be between 2 '
                                          'and 100 characters long')])

    address = fields.Str(required=True,
                         error_messages={"required": "Field is required"},
                         validate=[
                          validate.Length(min=2, max=100,
                                         error=
                                         'Field must be between 2 '
                                         'and 100 characters long')])

    city = fields.Nested(
        'CitySchema', only=['id'], required=True)

    archdiocese = fields.Nested(
        'ArchdioceseSchema', only=['id'], required=True)