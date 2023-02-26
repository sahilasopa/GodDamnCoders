import json

import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from JobsPortal.models import Post

success = {
    "message": {
        "ack": {
            "status": "ACK"
        }
    }
}

failure = {
    "message": {
        "ack": {
            "status": "NACK"
        }
    }
}

success_response = json.dumps(success)
failed_response = json.dumps(failure)


@csrf_exempt
def search(request):
    message = {}
    items = []
    # TODO: CHECK FOR EDGE CASES
    if request.method == "POST":
        data = json.loads(request.body)
        bap_url, bap_id = data.get("context").get("bap_uri"), data.get("context").get("bap_id")
        if bap_url is None or bap_id is None:
            return HttpResponse(failed_response, content_type="application/json")
        bap_url += "on_search"
        tags = data.get("message").get("intent").get("item").get("tags")[0].get("list")
        if tags is not None:
            for i in tags:
                tag = i.get("descriptor").get("code")
                try:
                    posts = Post.objects.filter(skills__contains=tag)
                    for post in posts:
                        if post is not None:
                            context = data.get("context")
                            context["bpp_id"] = "goddamncoders.pythonanywhere.com/apis/v1"
                            context["bpp_uri"] = "https://c104-103-195-249-148.in.ngrok.io/apis/v1"
                            context["action"] = "on_search"
                            message["context"] = (context)
                            items.append(
                                {
                                    "id": str(post.id),
                                    "descriptor": {
                                        "name": post.company_name
                                    },
                                    "locations": [
                                        {
                                            "id": "1",
                                            "city": {
                                                "name": post.location
                                            },
                                        },
                                    ],
                                    "items": [
                                        {
                                            "id": post.id,
                                            "descriptor": {
                                                "name": post.job_title,
                                                "long_desc": post.description
                                            },
                                            "location_ids": [
                                                "1"
                                            ]
                                        },
                                    ]
                                }
                            )
                except:
                    pass
                message["responses"] = items
                response = json.dumps(message)
                print(response)
                print(bap_url)
                x = requests.post(bap_url, data=response)
                print(x)
                print(x.status_code)
            return HttpResponse(success_response, content_type="application/json")
    return HttpResponse(data=success_response, content_type="application/json")


def home(request):
    return None
