from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "legacy"))

from notifications import create_message, send_notification


def test_email_notification_uses_email_payload():
    message = create_message("email", "ana@example.com", "Welcome")

    assert message == {
        "type": "email",
        "to": "ana@example.com",
        "subject": "Notification",
        "body": "Welcome",
    }
    assert send_notification("email", "ana@example.com", "Welcome") == "EMAIL:ana@example.com:Notification:Welcome"


def test_sms_notification_is_truncated():
    text = "x" * 200

    assert send_notification("sms", "12345", text) == f"SMS:12345:{'x' * 160}"
