"""What a vpn server should do"""

from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from typing import Any

from marznode.models import User, Inbound


class VPNBackend(ABC):
    @abstractmethod
    def contains_tag(self, tag: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def start(self, backend_config: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    async def restart(self, backend_config: Any) -> None:
        raise NotImplementedError

    @abstractmethod
    async def add_user(self, user: User, inbound: Inbound) -> None:
        raise NotImplementedError

    @abstractmethod
    async def remove_user(self, user: User, inbound: Inbound) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_logs(self, include_buffer: bool) -> AsyncIterator:
        raise NotImplementedError

    @abstractmethod
    async def get_usages(self):
        raise NotImplementedError
