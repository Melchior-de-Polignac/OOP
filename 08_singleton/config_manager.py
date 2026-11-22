import json
from pathlib import Path

DEFAULT_PATH = Path(__file__).with_name("config.json")


class ConfigManager:
    _instance = None

    def __init__(self, path=DEFAULT_PATH):
        self._data = json.loads(Path(path).read_text())
        self.load_count = 1

    @classmethod
    def get_instance(cls, path=None):
        if cls._instance is None:
            cls._instance = cls(path or DEFAULT_PATH)
        return cls._instance

    @classmethod
    def reset(cls):
        cls._instance = None

    def get(self, key, default=None):
        value = self._data
        for part in key.split("."):
            if not isinstance(value, dict) or part not in value:
                return default
            value = value[part]
        return value

    def set(self, key, value):
        *parents, last = key.split(".")
        node = self._data
        for part in parents:
            node = node.setdefault(part, {})
        node[last] = value


if __name__ == "__main__":
    config = ConfigManager.get_instance()
    print(config.get("app.name"), config.get("database.port"))
    print(ConfigManager.get_instance() is config)
