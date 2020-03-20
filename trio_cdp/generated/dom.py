# DO NOT EDIT THIS FILE!
#
# This code is generated off of PyCDP modules. If you need to make
# changes, edit the generator and regenerate all of the modules.

from __future__ import annotations
import typing

from ..context import get_connection_context, get_session_context

import cdp.dom
from cdp.dom import (
    AttributeModified,
    AttributeRemoved,
    BackendNode,
    BackendNodeId,
    BoxModel,
    CharacterDataModified,
    ChildNodeCountUpdated,
    ChildNodeInserted,
    ChildNodeRemoved,
    DistributedNodesUpdated,
    DocumentUpdated,
    InlineStyleInvalidated,
    Node,
    NodeId,
    PseudoElementAdded,
    PseudoElementRemoved,
    PseudoType,
    Quad,
    RGBA,
    Rect,
    SetChildNodes,
    ShadowRootPopped,
    ShadowRootPushed,
    ShadowRootType,
    ShapeOutsideInfo
)


async def collect_class_names_from_subtree(
        node_id: NodeId
    ) -> typing.List[str]:
    '''
    Collects class names for the node with given id and all of it's child nodes.

    :param node_id: Id of the node to collect class names.
    :returns: Class name list.
    '''
    session = get_session_context('dom.collect_class_names_from_subtree')
    return await session.execute(cdp.dom.collect_class_names_from_subtree(node_id))


async def copy_to(
        node_id: NodeId,
        target_node_id: NodeId,
        insert_before_node_id: typing.Optional[NodeId] = None
    ) -> NodeId:
    '''
    Creates a deep copy of the specified node and places it into the target container before the
    given anchor.

    :param node_id: Id of the node to copy.
    :param target_node_id: Id of the element to drop the copy into.
    :param insert_before_node_id: Drop the copy before this node (if absent, the copy becomes the last child of
    ``targetNodeId``).
    :returns: Id of the node clone.
    '''
    session = get_session_context('dom.copy_to')
    return await session.execute(cdp.dom.copy_to(node_id, target_node_id, insert_before_node_id))


async def describe_node(
        node_id: typing.Optional[NodeId] = None,
        backend_node_id: typing.Optional[BackendNodeId] = None,
        object_id: typing.Optional[runtime.RemoteObjectId] = None,
        depth: typing.Optional[int] = None,
        pierce: typing.Optional[bool] = None
    ) -> Node:
    '''
    Describes node given its id, does not require domain to be enabled. Does not start tracking any
    objects, can be used for automation.

    :param node_id: Identifier of the node.
    :param backend_node_id: Identifier of the backend node.
    :param object_id: JavaScript object id of the node wrapper.
    :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
    entire subtree or provide an integer larger than 0.
    :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
    (default is false).
    :returns: Node description.
    '''
    session = get_session_context('dom.describe_node')
    return await session.execute(cdp.dom.describe_node(node_id, backend_node_id, object_id, depth, pierce))


async def disable() -> None:
    '''
    Disables DOM agent for the given page.
    '''
    session = get_session_context('dom.disable')
    return await session.execute(cdp.dom.disable())


async def discard_search_results(
        search_id: str
    ) -> None:
    '''
    Discards search results from the session with the given id. `getSearchResults` should no longer
    be called for that search.

    :param search_id: Unique search session identifier.
    '''
    session = get_session_context('dom.discard_search_results')
    return await session.execute(cdp.dom.discard_search_results(search_id))


async def enable() -> None:
    '''
    Enables DOM agent for the given page.
    '''
    session = get_session_context('dom.enable')
    return await session.execute(cdp.dom.enable())


async def focus(
        node_id: typing.Optional[NodeId] = None,
        backend_node_id: typing.Optional[BackendNodeId] = None,
        object_id: typing.Optional[runtime.RemoteObjectId] = None
    ) -> None:
    '''
    Focuses the given element.

    :param node_id: Identifier of the node.
    :param backend_node_id: Identifier of the backend node.
    :param object_id: JavaScript object id of the node wrapper.
    '''
    session = get_session_context('dom.focus')
    return await session.execute(cdp.dom.focus(node_id, backend_node_id, object_id))


async def get_attributes(
        node_id: NodeId
    ) -> typing.List[str]:
    '''
    Returns attributes for the specified node.

    :param node_id: Id of the node to retrieve attibutes for.
    :returns: An interleaved array of node attribute names and values.
    '''
    session = get_session_context('dom.get_attributes')
    return await session.execute(cdp.dom.get_attributes(node_id))


async def get_box_model(
        node_id: typing.Optional[NodeId] = None,
        backend_node_id: typing.Optional[BackendNodeId] = None,
        object_id: typing.Optional[runtime.RemoteObjectId] = None
    ) -> BoxModel:
    '''
    Returns boxes for the given node.

    :param node_id: Identifier of the node.
    :param backend_node_id: Identifier of the backend node.
    :param object_id: JavaScript object id of the node wrapper.
    :returns: Box model for the node.
    '''
    session = get_session_context('dom.get_box_model')
    return await session.execute(cdp.dom.get_box_model(node_id, backend_node_id, object_id))


async def get_content_quads(
        node_id: typing.Optional[NodeId] = None,
        backend_node_id: typing.Optional[BackendNodeId] = None,
        object_id: typing.Optional[runtime.RemoteObjectId] = None
    ) -> typing.List[Quad]:
    '''
    Returns quads that describe node position on the page. This method
    might return multiple quads for inline nodes.

    :param node_id: Identifier of the node.
    :param backend_node_id: Identifier of the backend node.
    :param object_id: JavaScript object id of the node wrapper.
    :returns: Quads that describe node layout relative to viewport.
    '''
    session = get_session_context('dom.get_content_quads')
    return await session.execute(cdp.dom.get_content_quads(node_id, backend_node_id, object_id))


async def get_document(
        depth: typing.Optional[int] = None,
        pierce: typing.Optional[bool] = None
    ) -> Node:
    '''
    Returns the root DOM node (and optionally the subtree) to the caller.

    :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
    entire subtree or provide an integer larger than 0.
    :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
    (default is false).
    :returns: Resulting node.
    '''
    session = get_session_context('dom.get_document')
    return await session.execute(cdp.dom.get_document(depth, pierce))


async def get_file_info(
        object_id: runtime.RemoteObjectId
    ) -> str:
    '''
    Returns file information for the given
    File wrapper.

    :param object_id: JavaScript object id of the node wrapper.
    :returns:
    '''
    session = get_session_context('dom.get_file_info')
    return await session.execute(cdp.dom.get_file_info(object_id))


async def get_flattened_document(
        depth: typing.Optional[int] = None,
        pierce: typing.Optional[bool] = None
    ) -> typing.List[Node]:
    '''
    Returns the root DOM node (and optionally the subtree) to the caller.

    :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
    entire subtree or provide an integer larger than 0.
    :param pierce: Whether or not iframes and shadow roots should be traversed when returning the subtree
    (default is false).
    :returns: Resulting node.
    '''
    session = get_session_context('dom.get_flattened_document')
    return await session.execute(cdp.dom.get_flattened_document(depth, pierce))


async def get_frame_owner(
        frame_id: page.FrameId
    ) -> typing.Tuple[BackendNodeId, typing.Optional[NodeId]]:
    '''
    Returns iframe node that owns iframe with the given domain.

    :param frame_id:
    :returns: a tuple with the following items:
        0. backendNodeId: Resulting node.
        1. nodeId: (Optional) Id of the node at given coordinates, only when enabled and requested document.
    '''
    session = get_session_context('dom.get_frame_owner')
    return await session.execute(cdp.dom.get_frame_owner(frame_id))


async def get_node_for_location(
        x: int,
        y: int,
        include_user_agent_shadow_dom: typing.Optional[bool] = None
    ) -> typing.Tuple[BackendNodeId, typing.Optional[NodeId]]:
    '''
    Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is
    either returned or not.

    :param x: X coordinate.
    :param y: Y coordinate.
    :param include_user_agent_shadow_dom: False to skip to the nearest non-UA shadow root ancestor (default: false).
    :returns: a tuple with the following items:
        0. backendNodeId: Resulting node.
        1. nodeId: (Optional) Id of the node at given coordinates, only when enabled and requested document.
    '''
    session = get_session_context('dom.get_node_for_location')
    return await session.execute(cdp.dom.get_node_for_location(x, y, include_user_agent_shadow_dom))


async def get_outer_html(
        node_id: typing.Optional[NodeId] = None,
        backend_node_id: typing.Optional[BackendNodeId] = None,
        object_id: typing.Optional[runtime.RemoteObjectId] = None
    ) -> str:
    '''
    Returns node's HTML markup.

    :param node_id: Identifier of the node.
    :param backend_node_id: Identifier of the backend node.
    :param object_id: JavaScript object id of the node wrapper.
    :returns: Outer HTML markup.
    '''
    session = get_session_context('dom.get_outer_html')
    return await session.execute(cdp.dom.get_outer_html(node_id, backend_node_id, object_id))


async def get_relayout_boundary(
        node_id: NodeId
    ) -> NodeId:
    '''
    Returns the id of the nearest ancestor that is a relayout boundary.

    :param node_id: Id of the node.
    :returns: Relayout boundary node id for the given node.
    '''
    session = get_session_context('dom.get_relayout_boundary')
    return await session.execute(cdp.dom.get_relayout_boundary(node_id))


async def get_search_results(
        search_id: str,
        from_index: int,
        to_index: int
    ) -> typing.List[NodeId]:
    '''
    Returns search results from given `fromIndex` to given `toIndex` from the search with the given
    identifier.

    :param search_id: Unique search session identifier.
    :param from_index: Start index of the search result to be returned.
    :param to_index: End index of the search result to be returned.
    :returns: Ids of the search result nodes.
    '''
    session = get_session_context('dom.get_search_results')
    return await session.execute(cdp.dom.get_search_results(search_id, from_index, to_index))


async def hide_highlight() -> None:
    '''
    Hides any highlight.
    '''
    session = get_session_context('dom.hide_highlight')
    return await session.execute(cdp.dom.hide_highlight())


async def highlight_node() -> None:
    '''
    Highlights DOM node.
    '''
    session = get_session_context('dom.highlight_node')
    return await session.execute(cdp.dom.highlight_node())


async def highlight_rect() -> None:
    '''
    Highlights given rectangle.
    '''
    session = get_session_context('dom.highlight_rect')
    return await session.execute(cdp.dom.highlight_rect())


async def mark_undoable_state() -> None:
    '''
    Marks last undoable state.
    '''
    session = get_session_context('dom.mark_undoable_state')
    return await session.execute(cdp.dom.mark_undoable_state())


async def move_to(
        node_id: NodeId,
        target_node_id: NodeId,
        insert_before_node_id: typing.Optional[NodeId] = None
    ) -> NodeId:
    '''
    Moves node into the new container, places it before the given anchor.

    :param node_id: Id of the node to move.
    :param target_node_id: Id of the element to drop the moved node into.
    :param insert_before_node_id: Drop node before this one (if absent, the moved node becomes the last child of
    ``targetNodeId``).
    :returns: New id of the moved node.
    '''
    session = get_session_context('dom.move_to')
    return await session.execute(cdp.dom.move_to(node_id, target_node_id, insert_before_node_id))


async def perform_search(
        query: str,
        include_user_agent_shadow_dom: typing.Optional[bool] = None
    ) -> typing.Tuple[str, int]:
    '''
    Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or
    `cancelSearch` to end this search session.

    :param query: Plain text or query selector or XPath search query.
    :param include_user_agent_shadow_dom: True to search in user agent shadow DOM.
    :returns: a tuple with the following items:
        0. searchId: Unique search session identifier.
        1. resultCount: Number of search results.
    '''
    session = get_session_context('dom.perform_search')
    return await session.execute(cdp.dom.perform_search(query, include_user_agent_shadow_dom))


async def push_node_by_path_to_frontend(
        path: str
    ) -> NodeId:
    '''
    Requests that the node is sent to the caller given its path. // FIXME, use XPath

    :param path: Path to node in the proprietary format.
    :returns: Id of the node for given path.
    '''
    session = get_session_context('dom.push_node_by_path_to_frontend')
    return await session.execute(cdp.dom.push_node_by_path_to_frontend(path))


async def push_nodes_by_backend_ids_to_frontend(
        backend_node_ids: typing.List[BackendNodeId]
    ) -> typing.List[NodeId]:
    '''
    Requests that a batch of nodes is sent to the caller given their backend node ids.

    :param backend_node_ids: The array of backend node ids.
    :returns: The array of ids of pushed nodes that correspond to the backend ids specified in
    backendNodeIds.
    '''
    session = get_session_context('dom.push_nodes_by_backend_ids_to_frontend')
    return await session.execute(cdp.dom.push_nodes_by_backend_ids_to_frontend(backend_node_ids))


async def query_selector(
        node_id: NodeId,
        selector: str
    ) -> NodeId:
    '''
    Executes `querySelector` on a given node.

    :param node_id: Id of the node to query upon.
    :param selector: Selector string.
    :returns: Query selector result.
    '''
    session = get_session_context('dom.query_selector')
    return await session.execute(cdp.dom.query_selector(node_id, selector))


async def query_selector_all(
        node_id: NodeId,
        selector: str
    ) -> typing.List[NodeId]:
    '''
    Executes `querySelectorAll` on a given node.

    :param node_id: Id of the node to query upon.
    :param selector: Selector string.
    :returns: Query selector result.
    '''
    session = get_session_context('dom.query_selector_all')
    return await session.execute(cdp.dom.query_selector_all(node_id, selector))


async def redo() -> None:
    '''
    Re-does the last undone action.
    '''
    session = get_session_context('dom.redo')
    return await session.execute(cdp.dom.redo())


async def remove_attribute(
        node_id: NodeId,
        name: str
    ) -> None:
    '''
    Removes attribute with given name from an element with given id.

    :param node_id: Id of the element to remove attribute from.
    :param name: Name of the attribute to remove.
    '''
    session = get_session_context('dom.remove_attribute')
    return await session.execute(cdp.dom.remove_attribute(node_id, name))


async def remove_node(
        node_id: NodeId
    ) -> None:
    '''
    Removes node with given id.

    :param node_id: Id of the node to remove.
    '''
    session = get_session_context('dom.remove_node')
    return await session.execute(cdp.dom.remove_node(node_id))


async def request_child_nodes(
        node_id: NodeId,
        depth: typing.Optional[int] = None,
        pierce: typing.Optional[bool] = None
    ) -> None:
    '''
    Requests that children of the node with given id are returned to the caller in form of
    `setChildNodes` events where not only immediate children are retrieved, but all children down to
    the specified depth.

    :param node_id: Id of the node to get children for.
    :param depth: The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the
    entire subtree or provide an integer larger than 0.
    :param pierce: Whether or not iframes and shadow roots should be traversed when returning the sub-tree
    (default is false).
    '''
    session = get_session_context('dom.request_child_nodes')
    return await session.execute(cdp.dom.request_child_nodes(node_id, depth, pierce))


async def request_node(
        object_id: runtime.RemoteObjectId
    ) -> NodeId:
    '''
    Requests that the node is sent to the caller given the JavaScript node object reference. All
    nodes that form the path from the node to the root are also sent to the client as a series of
    `setChildNodes` notifications.

    :param object_id: JavaScript object id to convert into node.
    :returns: Node id for given object.
    '''
    session = get_session_context('dom.request_node')
    return await session.execute(cdp.dom.request_node(object_id))


async def resolve_node(
        node_id: typing.Optional[NodeId] = None,
        backend_node_id: typing.Optional[BackendNodeId] = None,
        object_group: typing.Optional[str] = None,
        execution_context_id: typing.Optional[runtime.ExecutionContextId] = None
    ) -> runtime.RemoteObject:
    '''
    Resolves the JavaScript node object for a given NodeId or BackendNodeId.

    :param node_id: Id of the node to resolve.
    :param backend_node_id: Backend identifier of the node to resolve.
    :param object_group: Symbolic group name that can be used to release multiple objects.
    :param execution_context_id: Execution context in which to resolve the node.
    :returns: JavaScript object wrapper for given node.
    '''
    session = get_session_context('dom.resolve_node')
    return await session.execute(cdp.dom.resolve_node(node_id, backend_node_id, object_group, execution_context_id))


async def set_attribute_value(
        node_id: NodeId,
        name: str,
        value: str
    ) -> None:
    '''
    Sets attribute for an element with given id.

    :param node_id: Id of the element to set attribute for.
    :param name: Attribute name.
    :param value: Attribute value.
    '''
    session = get_session_context('dom.set_attribute_value')
    return await session.execute(cdp.dom.set_attribute_value(node_id, name, value))


async def set_attributes_as_text(
        node_id: NodeId,
        text: str,
        name: typing.Optional[str] = None
    ) -> None:
    '''
    Sets attributes on element with given id. This method is useful when user edits some existing
    attribute value and types in several attribute name/value pairs.

    :param node_id: Id of the element to set attributes for.
    :param text: Text with a number of attributes. Will parse this text using HTML parser.
    :param name: Attribute name to replace with new attributes derived from text in case text parsed
    successfully.
    '''
    session = get_session_context('dom.set_attributes_as_text')
    return await session.execute(cdp.dom.set_attributes_as_text(node_id, text, name))


async def set_file_input_files(
        files: typing.List[str],
        node_id: typing.Optional[NodeId] = None,
        backend_node_id: typing.Optional[BackendNodeId] = None,
        object_id: typing.Optional[runtime.RemoteObjectId] = None
    ) -> None:
    '''
    Sets files for the given file input element.

    :param files: Array of file paths to set.
    :param node_id: Identifier of the node.
    :param backend_node_id: Identifier of the backend node.
    :param object_id: JavaScript object id of the node wrapper.
    '''
    session = get_session_context('dom.set_file_input_files')
    return await session.execute(cdp.dom.set_file_input_files(files, node_id, backend_node_id, object_id))


async def set_inspected_node(
        node_id: NodeId
    ) -> None:
    '''
    Enables console to refer to the node with given id via $x (see Command Line API for more details
    $x functions).

    :param node_id: DOM node id to be accessible by means of $x command line API.
    '''
    session = get_session_context('dom.set_inspected_node')
    return await session.execute(cdp.dom.set_inspected_node(node_id))


async def set_node_name(
        node_id: NodeId,
        name: str
    ) -> NodeId:
    '''
    Sets node name for a node with given id.

    :param node_id: Id of the node to set name for.
    :param name: New node's name.
    :returns: New node's id.
    '''
    session = get_session_context('dom.set_node_name')
    return await session.execute(cdp.dom.set_node_name(node_id, name))


async def set_node_value(
        node_id: NodeId,
        value: str
    ) -> None:
    '''
    Sets node value for a node with given id.

    :param node_id: Id of the node to set value for.
    :param value: New node's value.
    '''
    session = get_session_context('dom.set_node_value')
    return await session.execute(cdp.dom.set_node_value(node_id, value))


async def set_outer_html(
        node_id: NodeId,
        outer_html: str
    ) -> None:
    '''
    Sets node HTML markup, returns new node id.

    :param node_id: Id of the node to set markup for.
    :param outer_html: Outer HTML markup to set.
    '''
    session = get_session_context('dom.set_outer_html')
    return await session.execute(cdp.dom.set_outer_html(node_id, outer_html))


async def undo() -> None:
    '''
    Undoes the last performed action.
    '''
    session = get_session_context('dom.undo')
    return await session.execute(cdp.dom.undo())
