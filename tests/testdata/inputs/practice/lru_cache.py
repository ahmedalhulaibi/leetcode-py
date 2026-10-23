from collections import OrderedDict


def make_exports(completed: bool) -> dict[str, object]:
    class LRUCache:
        def __init__(self, capacity: int) -> None:
            if not completed:
                raise NotImplementedError
            self.capacity = capacity
            self.entries: OrderedDict[int, int] = OrderedDict()

        def get(self, key: int) -> int:
            if key not in self.entries:
                return -1
            value = self.entries.pop(key)
            self.entries[key] = value
            return value

        def put(self, key: int, value: int) -> None:
            self.entries.pop(key, None)
            self.entries[key] = value
            if len(self.entries) > self.capacity:
                self.entries.popitem(last=False)

    return {"LRUCache": LRUCache}
