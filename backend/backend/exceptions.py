from rest_framework.exceptions import APIException


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'El servidor de la Evaluación del Desempeño no esta funcionando en este momento, inténtelo luego.'
    default_code = 'service_unavailable'
