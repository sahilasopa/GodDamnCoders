import json

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
        "bpp_id": "goddamncoders.pythonanywhere.com/apis/v1",
        "bpp_uri": "https://goddamncoders.pythonanywhere.com/apis/v1",
        "transaction_id": "a9aaecca-10b7-4d19-b640-b047a7c62195",
        "message_id": "90bbd3e6-d6b2-4bd0-ad03-db00308a0ca7",
        "timestamp": "2023-02-24T17:26:28.804684+00:00",
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
                            "id": "3",
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
                            "id": "4",
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
                            "id": "07E048B389768316F05912ED9ED99C91",
                            "descriptor": {
                                "name": "Test lead",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "1"
                            ]
                        },
                        {
                            "id": "8A690F158A37965A2CC0E69EC8B360B2",
                            "descriptor": {
                                "name": "Test manager",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "3"
                            ]
                        },
                        {
                            "id": "B57FDECFBDBBA4021A13F32DE3D7C098",
                            "descriptor": {
                                "name": "senior Test lead",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "4"
                            ]
                        }
                    ]
                },
                {
                    "id": "2",
                    "descriptor": {
                        "name": "test"
                    },
                    "locations": [
                        {
                            "id": "2",
                            "city": {
                                "name": "test"
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
                            "id": "2b86f151821a60b8462a2e9462cc05120d05ffbc48ccac1c30774cec236a74f5",
                            "descriptor": {
                                "name": "Staff Mobile Developer - test",
                                "long_desc": "test"
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
                            "id": "3",
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
                            "id": "4",
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
                            "id": "07E048B389768316F05912ED9ED99C91",
                            "descriptor": {
                                "name": "Test lead",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "1"
                            ]
                        },
                        {
                            "id": "8A690F158A37965A2CC0E69EC8B360B2",
                            "descriptor": {
                                "name": "Test manager",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "3"
                            ]
                        },
                        {
                            "id": "B57FDECFBDBBA4021A13F32DE3D7C098",
                            "descriptor": {
                                "name": "senior Test lead",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "4"
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
                            "id": "3",
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
                            "id": "4",
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
                            "id": "07E048B389768316F05912ED9ED99C91",
                            "descriptor": {
                                "name": "Test lead",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "1"
                            ]
                        },
                        {
                            "id": "8A690F158A37965A2CC0E69EC8B360B2",
                            "descriptor": {
                                "name": "Test manager",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "3"
                            ]
                        },
                        {
                            "id": "B57FDECFBDBBA4021A13F32DE3D7C098",
                            "descriptor": {
                                "name": "senior Test lead",
                                "long_desc": "We’re on a search for a Staff Mobile Developer with the following attributes: Critical Thinking- You are able to skillfully conceptualise, apply, analyse and evaluate information gathered from observation, experience or communication and use it as a guide to action Data-Driven attitude — You often propose solutions or make a point in a logical and objective manner, substantiated with accurate data and evidence Dealing with Ambiguity — You can effectively cope with change and uncertainty, and are comfortable when things are up in the air Goal-oriented — You are driven and can be counted on to exceed goals. You steadfastly push yourself and others to achieve results all the time Problem Solving — You can easily identify and solve complex problems in a methodological manner "
                            },
                            "location_ids": [
                                "4"
                            ]
                        }
                    ]
                }
            ]
        }
    }
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
        return x
    return x
