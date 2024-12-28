from __future__ import annotations

from typing import Protocol


class InferenceExecutor(Protocol):
    async def do_inference(self, method: str, data: bytes) -> bytes | None: ...
# Modified on Tue Jan 21 11:34:02 PM +01 2025
print('Debug message')
