# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.network
from cdp.network import (
    AuthChallenge,
    AuthChallengeResponse,
    BlockedCookieWithReason,
    BlockedReason,
    BlockedSetCookieWithReason,
    CachedResource,
    CertificateTransparencyCompliance,
    ConnectionType,
    Cookie,
    CookieBlockedReason,
    CookieParam,
    CookieSameSite,
    DataReceived,
    ErrorReason,
    EventSourceMessageReceived,
    Headers,
    Initiator,
    InterceptionId,
    InterceptionStage,
    LoaderId,
    LoadingFailed,
    LoadingFinished,
    MonotonicTime,
    Request,
    RequestId,
    RequestIntercepted,
    RequestPattern,
    RequestServedFromCache,
    RequestWillBeSent,
    RequestWillBeSentExtraInfo,
    ResourceChangedPriority,
    ResourcePriority,
    ResourceTiming,
    ResourceType,
    Response,
    ResponseReceived,
    ResponseReceivedExtraInfo,
    SecurityDetails,
    SetCookieBlockedReason,
    SignedCertificateTimestamp,
    SignedExchangeError,
    SignedExchangeErrorField,
    SignedExchangeHeader,
    SignedExchangeInfo,
    SignedExchangeReceived,
    SignedExchangeSignature,
    TimeSinceEpoch,
    WebSocketClosed,
    WebSocketCreated,
    WebSocketFrame,
    WebSocketFrameError,
    WebSocketFrameReceived,
    WebSocketFrameSent,
    WebSocketHandshakeResponseReceived,
    WebSocketRequest,
    WebSocketResponse,
    WebSocketWillSendHandshakeRequest
)


async def can_clear_browser_cache() -> bool:
    '''
    Tells whether clearing browser cache is supported.

    :returns: True if browser cache can be cleared.
    '''
    session = get_session_context('network.can_clear_browser_cache')
    return await session.execute(cdp.network.can_clear_browser_cache())


async def can_clear_browser_cookies() -> bool:
    '''
    Tells whether clearing browser cookies is supported.

    :returns: True if browser cookies can be cleared.
    '''
    session = get_session_context('network.can_clear_browser_cookies')
    return await session.execute(cdp.network.can_clear_browser_cookies())


async def can_emulate_network_conditions() -> bool:
    '''
    Tells whether emulation of network conditions is supported.

    :returns: True if emulation of network conditions is supported.
    '''
    session = get_session_context('network.can_emulate_network_conditions')
    return await session.execute(cdp.network.can_emulate_network_conditions())


async def clear_browser_cache() -> None:
    '''
    Clears browser cache.
    '''
    session = get_session_context('network.clear_browser_cache')
    return await session.execute(cdp.network.clear_browser_cache())


async def clear_browser_cookies() -> None:
    '''
    Clears browser cookies.
    '''
    session = get_session_context('network.clear_browser_cookies')
    return await session.execute(cdp.network.clear_browser_cookies())


async def continue_intercepted_request(
        interception_id: InterceptionId,
        error_reason: typing.Optional[ErrorReason] = None,
        raw_response: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        method: typing.Optional[str] = None,
        post_data: typing.Optional[str] = None,
        headers: typing.Optional[Headers] = None,
        auth_challenge_response: typing.Optional[AuthChallengeResponse] = None
    ) -> None:
    '''
    Response to Network.requestIntercepted which either modifies the request to continue with any
    modifications, or blocks it, or completes it with the provided response bytes. If a network
    fetch occurs as a result which encounters a redirect an additional Network.requestIntercepted
    event will be sent with the same InterceptionId.
    Deprecated, use Fetch.continueRequest, Fetch.fulfillRequest and Fetch.failRequest instead.

    :param interception_id:
    :param error_reason: If set this causes the request to fail with the given reason. Passing ``Aborted`` for requests
    marked with ``isNavigationRequest`` also cancels the navigation. Must not be set in response
    to an authChallenge.
    :param raw_response: If set the requests completes using with the provided base64 encoded raw response, including
    HTTP status line and headers etc... Must not be set in response to an authChallenge.
    :param url: If set the request url will be modified in a way that's not observable by page. Must not be
    set in response to an authChallenge.
    :param method: If set this allows the request method to be overridden. Must not be set in response to an
    authChallenge.
    :param post_data: If set this allows postData to be set. Must not be set in response to an authChallenge.
    :param headers: If set this allows the request headers to be changed. Must not be set in response to an
    authChallenge.
    :param auth_challenge_response: Response to a requestIntercepted with an authChallenge. Must not be set otherwise.
    '''
    session = get_session_context('network.continue_intercepted_request')
    return await session.execute(cdp.network.continue_intercepted_request(interception_id, error_reason, raw_response, url, method, post_data, headers, auth_challenge_response))


async def delete_cookies(
        name: str,
        url: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        path: typing.Optional[str] = None
    ) -> None:
    '''
    Deletes browser cookies with matching name and url or domain/path pair.

    :param name: Name of the cookies to remove.
    :param url: If specified, deletes all the cookies with the given name where domain and path match
    provided URL.
    :param domain: If specified, deletes only cookies with the exact domain.
    :param path: If specified, deletes only cookies with the exact path.
    '''
    session = get_session_context('network.delete_cookies')
    return await session.execute(cdp.network.delete_cookies(name, url, domain, path))


async def disable() -> None:
    '''
    Disables network tracking, prevents network events from being sent to the client.
    '''
    session = get_session_context('network.disable')
    return await session.execute(cdp.network.disable())


async def emulate_network_conditions(
        offline: bool,
        latency: float,
        download_throughput: float,
        upload_throughput: float,
        connection_type: typing.Optional[ConnectionType] = None
    ) -> None:
    '''
    Activates emulation of network conditions.

    :param offline: True to emulate internet disconnection.
    :param latency: Minimum latency from request sent to response headers received (ms).
    :param download_throughput: Maximal aggregated download throughput (bytes/sec). -1 disables download throttling.
    :param upload_throughput: Maximal aggregated upload throughput (bytes/sec).  -1 disables upload throttling.
    :param connection_type: Connection type if known.
    '''
    session = get_session_context('network.emulate_network_conditions')
    return await session.execute(cdp.network.emulate_network_conditions(offline, latency, download_throughput, upload_throughput, connection_type))


async def enable(
        max_total_buffer_size: typing.Optional[int] = None,
        max_resource_buffer_size: typing.Optional[int] = None,
        max_post_data_size: typing.Optional[int] = None
    ) -> None:
    '''
    Enables network tracking, network events will now be delivered to the client.

    :param max_total_buffer_size: Buffer size in bytes to use when preserving network payloads (XHRs, etc).
    :param max_resource_buffer_size: Per-resource buffer size in bytes to use when preserving network payloads (XHRs, etc).
    :param max_post_data_size: Longest post body size (in bytes) that would be included in requestWillBeSent notification
    '''
    session = get_session_context('network.enable')
    return await session.execute(cdp.network.enable(max_total_buffer_size, max_resource_buffer_size, max_post_data_size))


async def get_all_cookies() -> typing.List[Cookie]:
    '''
    Returns all browser cookies. Depending on the backend support, will return detailed cookie
    information in the `cookies` field.

    :returns: Array of cookie objects.
    '''
    session = get_session_context('network.get_all_cookies')
    return await session.execute(cdp.network.get_all_cookies())


async def get_certificate(
        origin: str
    ) -> typing.List[str]:
    '''
    Returns the DER-encoded certificate.

    :param origin: Origin to get certificate for.
    :returns: 
    '''
    session = get_session_context('network.get_certificate')
    return await session.execute(cdp.network.get_certificate(origin))


async def get_cookies(
        urls: typing.Optional[typing.List[str]] = None
    ) -> typing.List[Cookie]:
    '''
    Returns all browser cookies for the current URL. Depending on the backend support, will return
    detailed cookie information in the `cookies` field.

    :param urls: The list of URLs for which applicable cookies will be fetched
    :returns: Array of cookie objects.
    '''
    session = get_session_context('network.get_cookies')
    return await session.execute(cdp.network.get_cookies(urls))


async def get_request_post_data(
        request_id: RequestId
    ) -> str:
    '''
    Returns post data sent with the request. Returns an error when no data was sent with the request.

    :param request_id: Identifier of the network request to get content for.
    :returns: Request body string, omitting files from multipart requests
    '''
    session = get_session_context('network.get_request_post_data')
    return await session.execute(cdp.network.get_request_post_data(request_id))


async def get_response_body(
        request_id: RequestId
    ) -> typing.Tuple[str, bool]:
    '''
    Returns content served for the given request.

    :param request_id: Identifier of the network request to get content for.
    :returns: a tuple with the following items:
        0. body: Response body.
        1. base64Encoded: True, if content was sent as base64.
    '''
    session = get_session_context('network.get_response_body')
    return await session.execute(cdp.network.get_response_body(request_id))


async def get_response_body_for_interception(
        interception_id: InterceptionId
    ) -> typing.Tuple[str, bool]:
    '''
    Returns content served for the given currently intercepted request.

    :param interception_id: Identifier for the intercepted request to get body for.
    :returns: a tuple with the following items:
        0. body: Response body.
        1. base64Encoded: True, if content was sent as base64.
    '''
    session = get_session_context('network.get_response_body_for_interception')
    return await session.execute(cdp.network.get_response_body_for_interception(interception_id))


async def replay_xhr(
        request_id: RequestId
    ) -> None:
    '''
    This method sends a new XMLHttpRequest which is identical to the original one. The following
    parameters should be identical: method, url, async, request body, extra headers, withCredentials
    attribute, user, password.

    :param request_id: Identifier of XHR to replay.
    '''
    session = get_session_context('network.replay_xhr')
    return await session.execute(cdp.network.replay_xhr(request_id))


async def search_in_response_body(
        request_id: RequestId,
        query: str,
        case_sensitive: typing.Optional[bool] = None,
        is_regex: typing.Optional[bool] = None
    ) -> typing.List[debugger.SearchMatch]:
    '''
    Searches for given string in response content.

    :param request_id: Identifier of the network response to search.
    :param query: String to search for.
    :param case_sensitive: If true, search is case sensitive.
    :param is_regex: If true, treats string parameter as regex.
    :returns: List of search matches.
    '''
    session = get_session_context('network.search_in_response_body')
    return await session.execute(cdp.network.search_in_response_body(request_id, query, case_sensitive, is_regex))


async def set_blocked_ur_ls(
        urls: typing.List[str]
    ) -> None:
    '''
    Blocks URLs from loading.

    :param urls: URL patterns to block. Wildcards ('*') are allowed.
    '''
    session = get_session_context('network.set_blocked_ur_ls')
    return await session.execute(cdp.network.set_blocked_ur_ls(urls))


async def set_bypass_service_worker(
        bypass: bool
    ) -> None:
    '''
    Toggles ignoring of service worker for each request.

    :param bypass: Bypass service worker and load from network.
    '''
    session = get_session_context('network.set_bypass_service_worker')
    return await session.execute(cdp.network.set_bypass_service_worker(bypass))


async def set_cache_disabled(
        cache_disabled: bool
    ) -> None:
    '''
    Toggles ignoring cache for each request. If `true`, cache will not be used.

    :param cache_disabled: Cache disabled state.
    '''
    session = get_session_context('network.set_cache_disabled')
    return await session.execute(cdp.network.set_cache_disabled(cache_disabled))


async def set_cookie(
        name: str,
        value: str,
        url: typing.Optional[str] = None,
        domain: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        secure: typing.Optional[bool] = None,
        http_only: typing.Optional[bool] = None,
        same_site: typing.Optional[CookieSameSite] = None,
        expires: typing.Optional[TimeSinceEpoch] = None
    ) -> bool:
    '''
    Sets a cookie with the given cookie data; may overwrite equivalent cookies if they exist.

    :param name: Cookie name.
    :param value: Cookie value.
    :param url: The request-URI to associate with the setting of the cookie. This value can affect the
    default domain and path values of the created cookie.
    :param domain: Cookie domain.
    :param path: Cookie path.
    :param secure: True if cookie is secure.
    :param http_only: True if cookie is http-only.
    :param same_site: Cookie SameSite type.
    :param expires: Cookie expiration date, session cookie if not set
    :returns: True if successfully set cookie.
    '''
    session = get_session_context('network.set_cookie')
    return await session.execute(cdp.network.set_cookie(name, value, url, domain, path, secure, http_only, same_site, expires))


async def set_cookies(
        cookies: typing.List[CookieParam]
    ) -> None:
    '''
    Sets given cookies.

    :param cookies: Cookies to be set.
    '''
    session = get_session_context('network.set_cookies')
    return await session.execute(cdp.network.set_cookies(cookies))


async def set_data_size_limits_for_test(
        max_total_size: int,
        max_resource_size: int
    ) -> None:
    '''
    For testing.

    :param max_total_size: Maximum total buffer size.
    :param max_resource_size: Maximum per-resource size.
    '''
    session = get_session_context('network.set_data_size_limits_for_test')
    return await session.execute(cdp.network.set_data_size_limits_for_test(max_total_size, max_resource_size))


async def set_extra_http_headers(
        headers: Headers
    ) -> None:
    '''
    Specifies whether to always send extra HTTP headers with the requests from this page.

    :param headers: Map with extra HTTP headers.
    '''
    session = get_session_context('network.set_extra_http_headers')
    return await session.execute(cdp.network.set_extra_http_headers(headers))


async def set_request_interception(
        patterns: typing.List[RequestPattern]
    ) -> None:
    '''
    Sets the requests to intercept that match the provided patterns and optionally resource types.
    Deprecated, please use Fetch.enable instead.

    :param patterns: Requests matching any of these patterns will be forwarded and wait for the corresponding
    continueInterceptedRequest call.
    '''
    session = get_session_context('network.set_request_interception')
    return await session.execute(cdp.network.set_request_interception(patterns))


async def set_user_agent_override(
        user_agent: str,
        accept_language: typing.Optional[str] = None,
        platform: typing.Optional[str] = None
    ) -> None:
    '''
    Allows overriding user agent with the given string.

    :param user_agent: User agent to use.
    :param accept_language: Browser langugage to emulate.
    :param platform: The platform navigator.platform should return.
    '''
    session = get_session_context('network.set_user_agent_override')
    return await session.execute(cdp.network.set_user_agent_override(user_agent, accept_language, platform))


async def take_response_body_for_interception_as_stream(
        interception_id: InterceptionId
    ) -> io.StreamHandle:
    '''
    Returns a handle to the stream representing the response body. Note that after this command,
    the intercepted request can't be continued as is -- you either need to cancel it or to provide
    the response body. The stream only supports sequential read, IO.read will fail if the position
    is specified.

    :param interception_id:
    :returns: 
    '''
    session = get_session_context('network.take_response_body_for_interception_as_stream')
    return await session.execute(cdp.network.take_response_body_for_interception_as_stream(interception_id))
