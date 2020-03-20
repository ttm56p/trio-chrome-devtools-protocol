# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.storage
from cdp.storage import (
    CacheStorageContentUpdated,
    CacheStorageListUpdated,
    IndexedDBContentUpdated,
    IndexedDBListUpdated,
    StorageType,
    UsageForType
)


async def clear_data_for_origin(
        origin: str,
        storage_types: str
    ) -> None:
    '''
    Clears storage for origin.

    :param origin: Security origin.
    :param storage_types: Comma separated list of StorageType to clear.
    '''
    session = get_session_context('storage.clear_data_for_origin')
    return await session.execute(cdp.storage.clear_data_for_origin(origin, storage_types))


async def get_usage_and_quota(
        origin: str
    ) -> typing.Tuple[float, float, typing.List[UsageForType]]:
    '''
    Returns usage and quota in bytes.

    :param origin: Security origin.
    :returns: a tuple with the following items:
        0. usage: Storage usage (bytes).
        1. quota: Storage quota (bytes).
        2. usageBreakdown: Storage usage per type (bytes).
    '''
    session = get_session_context('storage.get_usage_and_quota')
    return await session.execute(cdp.storage.get_usage_and_quota(origin))


async def track_cache_storage_for_origin(
        origin: str
    ) -> None:
    '''
    Registers origin to be notified when an update occurs to its cache storage list.

    :param origin: Security origin.
    '''
    session = get_session_context('storage.track_cache_storage_for_origin')
    return await session.execute(cdp.storage.track_cache_storage_for_origin(origin))


async def track_indexed_db_for_origin(
        origin: str
    ) -> None:
    '''
    Registers origin to be notified when an update occurs to its IndexedDB.

    :param origin: Security origin.
    '''
    session = get_session_context('storage.track_indexed_db_for_origin')
    return await session.execute(cdp.storage.track_indexed_db_for_origin(origin))


async def untrack_cache_storage_for_origin(
        origin: str
    ) -> None:
    '''
    Unregisters origin from receiving notifications for cache storage.

    :param origin: Security origin.
    '''
    session = get_session_context('storage.untrack_cache_storage_for_origin')
    return await session.execute(cdp.storage.untrack_cache_storage_for_origin(origin))


async def untrack_indexed_db_for_origin(
        origin: str
    ) -> None:
    '''
    Unregisters origin from receiving notifications for IndexedDB.

    :param origin: Security origin.
    '''
    session = get_session_context('storage.untrack_indexed_db_for_origin')
    return await session.execute(cdp.storage.untrack_indexed_db_for_origin(origin))
