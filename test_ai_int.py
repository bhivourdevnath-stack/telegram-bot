import json
import unittest
import ai_int


class DummyMessage:
    def __init__(self, text):
        self.text = text


class AiIntPayloadTests(unittest.TestCase):
    def test_normalize_input_from_telegram_message(self):
        self.assertEqual(ai_int.normalize_input(DummyMessage("hello there")), "hello there")

    def test_normalize_input_from_plain_text(self):
        self.assertEqual(ai_int.normalize_input("hello there"), "hello there")

    def test_payload_serializes_plain_string(self):
        payload = ai_int.build_payload(DummyMessage("hello there"))
        self.assertEqual(payload["messages"][1]["content"], "hello there")
        json.dumps(payload)


if __name__ == "__main__":
    unittest.main()
