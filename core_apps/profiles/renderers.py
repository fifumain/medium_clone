import json

from rest_framework.renderers import JSONRenderer


# we need renderes to change our json response. Like middleware changes requests/responses.
class ProfileJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Receiveng information about status of the request
        status_code = renderer_context["response"].status_code
        # errors = none in case of "errors" is empty
        errors = data.get("errors", None)
        if errors is not None:
            return super(ProfileJSONRenderer, self).render(
                data
            )  # return raw data in case of error, using default renderer
        # new updated response, that is better than default, better structure + additional information
        return json.dumps({"status_code": status_code, "profile": data})


# same logic, but for plural profiles
class ProfilesJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context["response"].status_code
        errors = data.get("errors", None)
        if errors is not None:
            return super(ProfilesJSONRenderer, self).render(data)
        return json.dumps({"status_code": status_code, "profiles": data})
