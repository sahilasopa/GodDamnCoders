import json

from django.http import JsonResponse
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

x = {
    "context": {
        "domain": "dsep:jobs",
        "version": "1.0.0",
        "action": "search",
        "bap_id": "dsep-protocol.becknprotocol.io",
        "bap_uri": "https://dsep-protocol-network.becknprotocol.io/",
        "transaction_id": "a9aaecca-10b7-4d19-b640-b047a7c62195",
        "message_id": "672f774c-4281-44dd-b1c2-84222a3d771e",
        "ttl": "PT10M",
        "timestamp": "2023-02-22T11:45:09.268Z"
    },
    "responses": [
        {
            "context": {
                "domain": "dsep:jobs",
                "location": {
                    "country": {
                        "name": "India",
                        "code": "IND"
                    }
                },
                "action": "on_search",
                "version": "1.0.0",
                "bap_id": "dsep-protocol.becknprotocol.io",
                "bap_uri": "https://dsep-protocol-network.becknprotocol.io/",
                "bpp_id": "affinidi.com.bpp",
                "bpp_uri": "https://6vs8xnx5i7.execute-api.ap-south-1.amazonaws.com/dsep",
                "transaction_id": "a9aaecca-10b7-4d19-b640-b047a7c62195",
                "message_id": "672f774c-4281-44dd-b1c2-84222a3d771e",
                "timestamp": "2023-02-22T11:45:10.1712958+00:00",
                "ttl": "P1M"
            },
            "message": {
                "catalog": {
                    "descriptor": {
                        "name": "Affindi Jobs"
                    },
                    "payments": [],
                    "providers": [
                        {
                            "id": "1",
                            "descriptor": {
                                "name": "Affinidi"
                            },
                            "locations": [
                                {
                                    "id": "1",
                                    "city": {
                                        "name": "Bangalore"
                                    },
                                    "state": {
                                        "name": ""
                                    },
                                    "country": {
                                        "name": ""
                                    }
                                },
                                {
                                    "id": "2",
                                    "city": {
                                        "name": "Bangalore"
                                    },
                                    "state": {
                                        "name": ""
                                    },
                                    "country": {
                                        "name": ""
                                    }
                                }
                            ],
                            "items": [
                                {
                                    "id": "D7F8606A370DA9966DF15E62A81C374B",
                                    "descriptor": {
                                        "name": "Database Engineer",
                                        "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                                    },
                                    "location_ids": [
                                        "1"
                                    ]
                                },
                                {
                                    "id": "0253719F295521CED39EC9C2F3C8DCDE",
                                    "descriptor": {
                                        "name": "Fullstack Engineer",
                                        "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                                    },
                                    "location_ids": [
                                        "2"
                                    ]
                                }
                            ]
                        },
                        {
                            "id": "1",
                            "descriptor": {
                                "name": "Affinidi"
                            },
                            "locations": [
                                {
                                    "id": "1",
                                    "city": {
                                        "name": "Bangalore"
                                    },
                                    "state": {
                                        "name": ""
                                    },
                                    "country": {
                                        "name": ""
                                    }
                                },
                                {
                                    "id": "2",
                                    "city": {
                                        "name": "Bangalore"
                                    },
                                    "state": {
                                        "name": ""
                                    },
                                    "country": {
                                        "name": ""
                                    }
                                }
                            ],
                            "items": [
                                {
                                    "id": "D7F8606A370DA9966DF15E62A81C374B",
                                    "descriptor": {
                                        "name": "Database Engineer",
                                        "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                                    },
                                    "location_ids": [
                                        "1"
                                    ]
                                },
                                {
                                    "id": "0253719F295521CED39EC9C2F3C8DCDE",
                                    "descriptor": {
                                        "name": "Fullstack Engineer",
                                        "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                                    },
                                    "location_ids": [
                                        "2"
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        }
    ]
}


@csrf_exempt
def Home(request):
    print(request.method)
    if request.method == "POST":
        data = json.dumps(str(request.body))
        print("Yes someone posted something")
        print("=================== BODY ==========================")
        print(data)
        print("=================== BODY ==========================")
        return JsonResponse(x, safe=False)
    return JsonResponse(data=x, safe=False)
