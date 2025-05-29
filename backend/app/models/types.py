import json
from sqlalchemy.types import TypeDecorator, Text

class JSONEncodedList(TypeDecorator):
    impl = Text

    def process_bind_param(self, value, dialect):
        if value is None:
            return "[]"
        if isinstance(value, str):
            try:
                parsed = json.loads(value)
                if isinstance(parsed, list):
                    return value  # уже сериализован корректно
            except json.JSONDecodeError:
                pass  # продолжим сериализацию
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if value is None or value == "":
            return []
        if isinstance(value, list):
            return value
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return []
