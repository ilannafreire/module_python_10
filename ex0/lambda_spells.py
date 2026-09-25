def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Sort artifacts by descending power."""
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """Return mages with at least min_power."""
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Wrap each spell name in asterisks."""
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict[str, int | float]:
    """Return maximum, minimum and average mage power."""
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(sum(mage["power"] for mage in mages) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "staff"},
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Moon Tome", "power": 70, "type": "book"},
    ]

    mages = [
        {"name": "Potira", "power": 95, "element": "fire"},
        {"name": "Tefe", "power": 60, "element": "water"},
        {"name": "Jutai", "power": 80, "element": "wind"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    ordered = artifact_sorter(artifacts)
    print(
        f"{ordered[0]['name']} ({ordered[0]['power']} power) comes before "
        f"{ordered[1]['name']} ({ordered[1]['power']} power)"
    )

    print("Testing power filter...")
    strong_mages = power_filter(mages, 75)
    print(strong_mages)

    print("Testing spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("Testing mage stats...")
    print(mage_stats(mages))
