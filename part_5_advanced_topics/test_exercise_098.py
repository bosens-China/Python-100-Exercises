import asyncio
import pytest
from part_5_advanced_topics.exercise_098 import gather_results


def test_gather_results_preserves_order():
    async def value(number):
        await asyncio.sleep(0)
        return number

    result = asyncio.run(gather_results([lambda number=n: value(number) for n in (3, 1, 2)]))
    assert result == [3, 1, 2]
    assert asyncio.run(gather_results([])) == []


def test_gather_results_propagates_failure():
    async def fail():
        raise ValueError("bad task")

    with pytest.raises(ValueError, match="bad task"):
        asyncio.run(gather_results([fail]))
