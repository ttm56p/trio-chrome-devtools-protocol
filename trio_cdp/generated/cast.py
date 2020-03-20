# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.cast
from cdp.cast import (
    IssueUpdated,
    Sink,
    SinksUpdated
)


async def disable() -> None:
    '''
    Stops observing for sinks and issues.
    '''
    session = get_session_context('cast.disable')
    return await session.execute(cdp.cast.disable())


async def enable(
        presentation_url: typing.Optional[str] = None
    ) -> None:
    '''
    Starts observing for sinks that can be used for tab mirroring, and if set,
    sinks compatible with |presentationUrl| as well. When sinks are found, a
    |sinksUpdated| event is fired.
    Also starts observing for issue messages. When an issue is added or removed,
    an |issueUpdated| event is fired.

    :param presentation_url:
    '''
    session = get_session_context('cast.enable')
    return await session.execute(cdp.cast.enable(presentation_url))


async def set_sink_to_use(
        sink_name: str
    ) -> None:
    '''
    Sets a sink to be used when the web page requests the browser to choose a
    sink via Presentation API, Remote Playback API, or Cast SDK.

    :param sink_name:
    '''
    session = get_session_context('cast.set_sink_to_use')
    return await session.execute(cdp.cast.set_sink_to_use(sink_name))


async def start_tab_mirroring(
        sink_name: str
    ) -> None:
    '''
    Starts mirroring the tab to the sink.

    :param sink_name:
    '''
    session = get_session_context('cast.start_tab_mirroring')
    return await session.execute(cdp.cast.start_tab_mirroring(sink_name))


async def stop_casting(
        sink_name: str
    ) -> None:
    '''
    Stops the active Cast session on the sink.

    :param sink_name:
    '''
    session = get_session_context('cast.stop_casting')
    return await session.execute(cdp.cast.stop_casting(sink_name))
