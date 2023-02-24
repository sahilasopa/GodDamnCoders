import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

url = "https://dsep-protocol-client.becknprotocol.io/search"
payload = json.dumps({
    "context": {
        "domain": "dsep:jobs",
        "action": "search",
        "version": "1.0.0",
        "bap_id": "dsep-protocol.becknprotocol.io",
        "bap_uri": "https://dsep-protocol-network.becknprotocol.io/",
        "transaction_id": "a9aaecca-10b7-4d19-b640-b047a7c62195",
        "message_id": "$89bdae17-9942-40c8-869a-5bd413356407",
        "timestamp": "2022-10-11T09:55:41.161Z",
        "ttl": "PT30S"
    },
    "message": {
        "intent": {
            "item": {
                "descriptor": {
                    "name": "Test"
                },
                "tags": [
                    {
                        "descriptor": {
                            "name": "skill",
                            "code": "skills"
                        },
                        "list": [
                            {
                                "descriptor": {
                                    "code": "React"
                                }
                            }
                        ]
                    }
                ]
            }
        }
    }
})
headers = {
    'Content-Type': 'application/json'
}


@csrf_exempt
def Home(request):
    print(request.method)
    if request.method == "POST":
        print("Yes someone posted something")
        print("=================== BODY ==========================")
        print(request.body)
        print("=================== BODY ==========================")
    return HttpResponse("okay")
