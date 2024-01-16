#!/usr/bin/env python3
"""module to measure the execution time"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime - execute async_com 4 times
    Arguments:
        nothing
    Returns:
        the total exection time required to complete the task
    """
    t_start = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    t_end = time.perf_counter()
    return (t_end - t_start)
