from collections.abc import Callable


def mage_counter() -> Callable[[], int]:
    """Return a counter closure."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Return a closure that accumulates power."""
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Return an enchantment function for a specific type."""

    def enchanted(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanted


def memory_vault() -> dict[str, Callable]:
    """Return private store and recall functions."""
    storage: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        storage[key] = value

    def recall(key: str) -> object | str:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    counter_a = mage_counter()
    counter_b = mage_counter()

    print("Testing mage counter...")
    print(counter_a())
    print(counter_a())
    print(counter_b())

    accumulator = spell_accumulator(100)
    print("Testing spell accumulator...")
    print(accumulator(20))
    print(accumulator(30))

    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print("Testing enchantment factory...")
    print(flaming("Sword"))
    print(frozen("Shield"))

    vault = memory_vault()
    print("Testing memory vault...")
    vault["store"]("secret", 42)
    print(vault["recall"]("secret"))
    print(vault["recall"]("missing"))
