import time
from collections.abc import Callable
from functools import wraps
from typing import Any


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Print a spell's execution time."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Return a decorator that validates spell power."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get("power")

            if power is None and args:
                power = args[-1]

            if isinstance(power, (int, float)) and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Return a decorator that retries failed spells."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Demonstrate a static method and a decorated method."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return whether name contains at least three letters or spaces."""
        cleaned = name.strip()
        return len(cleaned) >= 3 and cleaned.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with valid power."""
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    """Demonstrate the timer decorator."""
    return "Fireball cast!"


def make_flaky_spell() -> Callable[[], str]:
    """Create a spell that fails twice before succeeding."""
    calls = 0

    @retry_spell(3)
    def flaky_spell() -> str:
        nonlocal calls
        calls += 1
        if calls < 3:
            raise ValueError("Spell failed")
        return "Successful cast after retries"

    return flaky_spell


if __name__ == "__main__":
    print("Testing spell timer...")
    print(fireball())

    print("Testing retrying spell...")
    print(make_flaky_spell()())

    guild = MageGuild()
    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Ari"))
    print(MageGuild.validate_mage_name("Ari3"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 7))
