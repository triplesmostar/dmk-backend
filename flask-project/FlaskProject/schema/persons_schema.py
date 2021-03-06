from marshmallow import Schema, fields, validate


class PersonSchema(Schema):

    id = fields.UUID(required=True,
                     error_messages={
                         "invalid_uuid": "Invalid data for UUID",
                         "required": "Field is required",
                         "null": "Field can not be null"})
    first_name = fields.Str(required=True,
                            error_messages={"required": "Field is required"},
                            validate=[
                              validate.Length(min=2, max=50,
                                              error=
                                              'Field must be between 2 '
                                              'and 50 characters long')])
    last_name = fields.Str(required=True,
                           error_messages={"required": "Field is required"},
                           validate=[
                              validate.Length(min=2, max=50,
                                              error=
                                              'Field must be between 2 '
                                              'and 50 characters long')])
    maiden_name = fields.Str(required=False)
    birth_date = fields.Date(required=True,
                             error_messages={"required": "Field is required"})

    birth_place = fields.Nested(
        'CitySchema', only=['id'], required=True)

    identity_number = fields.Str(required=True,
                                 error_messages={"required": "Field is required"},
                                 validate=[
                                   validate.Length(min=10, max=20,
                                                   error=
                                                   'Field must be between 10'
                                                   'and 20 characters long')])
    domicile = fields.Str(required=False)
    father = fields.Nested(
        'PersonSchema', only=['id'], required=False)

    mother = fields.Nested(
        'PersonSchema', only=['id'], required=False)

    district = fields.Nested(
        'DistrictSchema', only=['id'], required=True)

    religion = fields.Nested(
        'ListItemSchema', only=['id'], required=True)

