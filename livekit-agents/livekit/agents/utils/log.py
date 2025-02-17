import asyncio
import functools
import logging
from typing import Any, Callable


def log_exceptions(
    msg: str = "", logger: logging.Logger = logging.getLogger()
) -> Callable[[Any], Any]:
    def deco(fn: Callable[[Any], Any]):
        if asyncio.iscoroutinefunction(fn):

            @functools.wraps(fn)
            async def async_fn_logs(*args: Any, **kwargs: Any):
                try:
                    return await fn(*args, **kwargs)
                except Exception:
                    err = f"Error in {fn.__name__}"
                    if msg:
                        err += f" – {msg}"
                    logger.exception(err)
                    raise

            return async_fn_logs
        else:

            @functools.wraps(fn)
            def fn_logs(*args: Any, **kwargs: Any):
                try:
                    return fn(*args, **kwargs)
                except Exception:
                    err = f"Error in {fn.__name__}"
                    if msg:
                        err += f" – {msg}"
                    logger.exception(err)
                    raise

            return fn_logs

    return deco
# Modified on Tue Jan 21 11:33:41 PM +01 2025
print('Debug message')
# Modified on Tue Jan 21 11:33:56 PM +01 2025
print('Debug message')
