from .base import (
    Provider,
    ProviderError,
    available_providers,
    get_provider_class,
    register_provider,
)
from . import openrouter  # noqa: F401  (registers the built-in provider)

__all__ = [
    "Provider",
    "ProviderError",
    "available_providers",
    "get_provider_class",
    "register_provider",
]
