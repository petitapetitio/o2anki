import json
import urllib.request

from o2anki.parsing.parsed_note import ParsedNote


class AnkiConnectClient:
    def __init__(self):
        self._version = 6

    def invoke_requests(self, requests: list[dict]) -> list:
        multi_response = self.invoke(
            {
                "action": "multi",
                "version": self._version,
                "params": {"actions": requests},
            }
        )
        exceptions = []
        results = []
        for request, response in zip(requests, multi_response):
            match response:
                case {"error": "cannot create note because it is a duplicate"}:
                    print(
                        f'La question `{request["params"]["note"]["fields"]["Front"]}` est dupliquée'
                    )
                    results.append(None)
                case {"error": str(reason)}:
                    exceptions.append(Exception(response["error"]))
                case {"error": None}:
                    results.append(response["result"])

        if len(exceptions) > 0:
            raise ExceptionGroup(
                "Une erreur est survenue durant invoke_requests:", exceptions
            )

        return results

    def invoke(self, request: dict):
        request_json = json.dumps(request).encode("utf-8")
        response = json.load(
            urllib.request.urlopen(
                urllib.request.Request("http://127.0.0.1:8765", request_json)
            )
        )
        if response["error"] is not None:
            raise Exception(response["error"])
        return response["result"]

    def get_deck_names(self) -> dict:
        return {"action": "deckNames", "version": self._version, "params": {}}

    def create_deck(self, name):
        # see https://foosoft.net/projects/anki-connect/#createdeck
        return {
            "action": "createDeck",
            "version": self._version,
            "params": {"deck": name},
        }

    def add_basic_note_request(self, note: ParsedNote) -> dict:
        # see https://foosoft.net/projects/anki-connect/#addnote
        return {
            "action": "addNote",
            "version": self._version,
            "params": {
                "note": {
                    "deckName": note.target_deck or "Default",
                    "modelName": "Basic",
                    "fields": {"Front": note.question, "Back": note.answer},
                    "options": {
                        "allowDuplicate": False,
                        "duplicateScope": "deck",
                    },
                    "tags": note.file_tags,
                    # "picture": [{
                    #     "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/A_black_cat_named_Tilly.jpg/220px-A_black_cat_named_Tilly.jpg",
                    #     "filename": "black_cat.jpg",
                    #     "skipHash": "8d6e4646dfae812bf39651b59d7429ce",
                    #     "fields": [
                    #         "Back"
                    #     ]
                    # }]
                }
            },
        }
