"""
EMACOS Kernel Service Protocols.

This module defines the contracts that every kernel-managed service
must satisfy. These protocols establish a common lifecycle interface
while allowing implementations to remain loosely coupled.
"""

from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class Service(Protocol):
    """Contract for every service managed by the EMACOS kernel."""

    @property
    def name(self) -> str:
        """Return the unique service name."""
        ...

    @property
    def version(self) -> str:
        """Return the service version."""
        ...

    @property
    def is_running(self) -> bool:
        """Return True when the service is running."""
        ...

    async def start(self) -> None:
        """Start the service."""
        ...

    async def stop(self) -> None:
        """Stop the service."""
        ...

    async def health(self) -> bool:
        """Return True if the service is healthy."""
        ...