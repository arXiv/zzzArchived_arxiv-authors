"""Defines HTTP routes/methods supported by the author disambiguation API."""

from flask import Blueprint, Response, request
from flask.json import jsonify

from .. import controllers


blueprint = Blueprint('api', __name__, url_prefix='')


@blueprint.route('/status', methods=['GET'])
def service_status() -> Response:
    """
    Service status endpoint.

    Returns ``200 OK`` if the service is up and ready to handle requests.
    """
    response_data, status_code, headers = controllers.service_status(request.params)
    response: Response = jsonify(response_data)
    response.status_code = status_code
    response.headers.extend(headers)
    return response


@blueprint.route('/eprint/<arxiv_id>/authors', methods=['GET'])
@blueprint.route('/eprint/<arxiv_id_v>/authors', methods=['GET'])
def get_authors(identifier: str) -> Response:
    ...


@blueprint.route('/eprint/<arxiv_id>/appellations', methods=['GET'])
@blueprint.route('/eprint/<arxiv_id_v>/appellations', methods=['GET'])
def get_appellations(identifier: str) -> Response:
    ...


@blueprint.route('/eprint/<arxiv_id>/appellations', methods=['POST'])
@blueprint.route('/eprint/<arxiv_id_v>/appellations', methods=['POST'])
def add_appellations(identifier: str) -> Response:
    ...


@blueprint.route('/eprint/<arxiv_id>/appellations', methods=['DELETE'])
@blueprint.route('/eprint/<arxiv_id_v>/appellations', methods=['DELETE'])
def delete_appellations(identifier: str) -> Response:
    ...


@blueprint.route('/eprint/<arxiv_id>/appellations/<appellation>', methods=['PUT'])
@blueprint.route('/eprint/<arxiv_id_v>/appellations/<appellation>', methods=['PUT'])
def update_appellation(identifier: str, appellation: str) -> Response:
    ...


@blueprint.route('/eprint/<arxiv_id>/appellations/<appellation>', methods=['DELETE'])
@blueprint.route('/eprint/<arxiv_id_v>/appellations/<appellation>', methods=['DELETE'])
def delete_appellation(identifier: str, appellation: str) -> Response:
    ...
