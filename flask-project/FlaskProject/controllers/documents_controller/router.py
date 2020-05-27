from flask import request, jsonify
from ...flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)
from .controller import DocumentController
from ..persons_controller.controller import PersonController
from ... import bpp, Document, FlaskProjectLogException, Person, User
from ...general import Status, obj_to_dict
from ...general.route_decorators import allow_access
from ...schema import PersonSchema, RegistryOfBaptismsSchema, DocumentSchema


@bpp.route('/document', methods=['GET'])
@jwt_required
#@allow_access
def get_documents():
    start = request.args.get('start', 0, int)
    limit = request.args.get('limit', 10, int)

    document_number = request.args.get('document_number', '', str)
    act_date = request.args.get('act_date', '', str)
    volume = request.args.get('volume', '', str)
    year = request.args.get('year', '', str)
    page = request.args.get('page', '', str)
    number = request.args.get('number', '', str)
    document_type = request.args.get('document_type', None, str)
    person_id = request.args.get('person_id', None, str)
    person2_id = request.args.get('person2_id', None, str)
    act_performed = request.args.get('act_performed', None, str)
    district = request.args.get('district', None, str)

    pagination_result = DocumentController.get_list_pagination(
        start=start, limit=limit, document_number=document_number, act_date=act_date,
        volume=volume, year=year, page=page, number=number,
        document_type=document_type, person_id=person_id, person2_id=person2_id, act_performed=act_performed, district=district)

    return jsonify(pagination_result)