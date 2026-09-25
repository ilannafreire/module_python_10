from collections.abc import Callable
from typing import Any


def fireball(target: str, power: int) -> str:
    """Return a fire spell result."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Return a healing spell result."""
    return f"Heal restores {target} for {power} HP"


def spell_combiner(
    spell1: Callable[..., Any], spell2: Callable[..., Any]
) -> Callable[..., tuple]:
    """Return a spell that runs both spells with the same arguments."""

    def combined(*args: Any, **kwargs: Any) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))

    return combined


def power_amplifier(
    base_spell: Callable[..., Any], multiplier: int
) -> Callable[..., Any]:
    """Return a spell with multiplied power."""

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified


def conditional_caster(
    condition: Callable[..., bool], spell: Callable[..., Any]
) -> Callable[..., Any]:
    """Return a spell that runs only when its condition is true."""

    def cast(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"

    return cast


def spell_sequence(
    spells: list[Callable[..., Any]],
) -> Callable[..., list[Any]]:
    """Return a spell that runs every spell in order."""

    def run(*args: Any, **kwargs: Any) -> list[Any]:
        return [spell(*args, **kwargs) for spell in spells]

    return run


if __name__ == "__main__":
    combined = spell_combiner(fireball, heal)
    mega_fireball = power_amplifier(fireball, 3)
    can_cast = conditional_caster(lambda target, power: power >= 10, fireball)
    chain = spell_sequence([fireball, heal])

    print("Testing spell combiner...")
    print(combined("Dragon", 10))

    print("Testing power amplifier...")
    print(mega_fireball("Dragon", 10))

    print("Testing conditional caster...")
    print(can_cast("Dragon", 5))
    print(can_cast("Dragon", 12))

    print("Testing spell sequence...")
    print(chain("Knight", 7))
