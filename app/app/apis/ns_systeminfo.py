from flask_restplus import Namespace, Resource, fields
import socket

api = Namespace(
    "systeminfo", description="Get information about the system this PAI is running on"
)

systeminfo = api.model(
    "SystemInfo",
    {
        "hostname": fields.String(
            required=True, description="The hostname of the system"
        ),
        "fqdn": fields.String(
            required=True, description="The fully qualified hostname of the system"
        ),
        "ip-address": fields.String(
            required=True, description="The IP address of the host system"
        ),
    },
)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


SYSTEM = {
    "hostname": socket.gethostname(),
    "fqdn": socket.getfqdn(),
    "ip-address": get_ip(),
}


@api.route("/")
class SystemInfo(Resource):
    @api.doc("Get information about the host system")
    @api.marshal_with(systeminfo)
    def get(self):
        """get the system info"""
        return SYSTEM
