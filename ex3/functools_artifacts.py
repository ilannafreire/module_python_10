from collections.abc import Callable
from functools import lru_cache, partial, reduce, singledispatch
from typing import Any
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using the requested operation."""
    if not spells:
        return 0

    if operation == "add":
        return reduce(operator.add, spells)
    if operation == "multiply":
        return reduce(operator.mul, spells)
    if operation == "max":
        return reduce(
            lambda current, value: current if current > value else value,
            spells,
        )
    if operation == "min":
        return reduce(
            lambda current, value: current if current < value else value,
            spells,
        )

    raise ValueError(f"Unknown operation: {operation}")


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str],
) -> dict[str, Callable[[str], str]]:
    """Create specialized enchantments with partial."""
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "storm": partial(base_enchantment, 50, "storm"),
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth cached Fibonacci number."""
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a type-based spell dispatcher."""

    @singledispatch
    def dispatcher(value: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatcher.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatcher.register(list)
    def _(value: list[Any]) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    print(spell_reducer([10, 20, 30], "add"))
    print(spell_reducer([10, 20, 30], "multiply"))
    print(spell_reducer([10, 20, 30], "max"))

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element} enchantment on {target} at power {power}"

    print("Testing partial enchanter...")
    enchanted = partial_enchanter(base_enchantment)
    print(enchanted["fire"]("dragon"))

    print("Testing memoized fibonacci...")
    print(memoized_fibonacci(0))
    print(memoized_fibonacci(1))
    print(memoized_fibonacci(10))
    print(memoized_fibonacci.cache_info())

    print("Testing spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fireball", "heal", "shield"]))
    print(dispatcher({"name": "unknown"}))
