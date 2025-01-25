import json
import urllib.request


class AnkiConnectClient:

    def invoke(self, action, **params):
        request_json = json.dumps(self._request(action, **params)).encode("utf-8")
        response = json.load(
            urllib.request.urlopen(
                urllib.request.Request("http://127.0.0.1:8765", request_json)
            )
        )
        if response["error"] is not None:
            raise Exception(response["error"])
        return response["result"]

    def _request(self, action, **params) -> dict:
        return {"action": action, "params": params, "version": 6}


cli = AnkiConnectClient()
cli.invoke("createDeck", deck="test1")
result = cli.invoke("deckNames")
print("got list of decks: {}".format(result))
