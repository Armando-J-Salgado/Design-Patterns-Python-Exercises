def create_message(channel, recipient, text):
    if channel == "email":
        return {
            "type": "email",
            "to": recipient,
            "subject": "Notification",
            "body": text,
        }

    if channel == "sms":
        return {
            "type": "sms",
            "to": recipient,
            "text": text[:160],
        }

    if channel == "push":
        return {
            "type": "push",
            "to": recipient,
            "title": "Alert",
            "body": text,
        }

    raise ValueError("unsupported channel")


def send_notification(channel, recipient, text):
    message = create_message(channel, recipient, text)
    if message["type"] == "email":
        return f"EMAIL:{message['to']}:{message['subject']}:{message['body']}"
    if message["type"] == "sms":
        return f"SMS:{message['to']}:{message['text']}"
    return f"PUSH:{message['to']}:{message['title']}:{message['body']}"
