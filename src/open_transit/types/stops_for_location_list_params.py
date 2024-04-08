# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["StopsForLocationListParams"]


class StopsForLocationListParams(TypedDict, total=False):
    key: str

    lat: float

    lon: float
