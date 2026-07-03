from typing import cast

from emacos.kernel.protocols import Service


class DummyService:
    @property
    def name(self) -> str:
        return "dummy"

    @property
    def version(self) -> str:
        return "0.1.0"

    @property
    def is_running(self) -> bool:
        return True

    async def start(self) -> None:
        pass

    async def stop(self) -> None:
        pass

    async def health(self) -> bool:
        return True


def test_dummy_service_satisfies_protocol() -> None:
    service = DummyService()

    assert isinstance(service, Service)

    typed_service = cast(Service, service)

    assert typed_service.name == "dummy"