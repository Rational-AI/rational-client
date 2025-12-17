from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.knowledge_edge_dto import KnowledgeEdgeDto
    from ..models.knowledge_graph_config_dto import KnowledgeGraphConfigDto
    from ..models.knowledge_node_dto import KnowledgeNodeDto


T = TypeVar("T", bound="KnowledgeGraphDto")


@_attrs_define
class KnowledgeGraphDto:
    """
    Attributes:
        config (KnowledgeGraphConfigDto):
        nodes (list['KnowledgeNodeDto']):
        edges (list['KnowledgeEdgeDto']):
    """

    config: "KnowledgeGraphConfigDto"
    nodes: list["KnowledgeNodeDto"]
    edges: list["KnowledgeEdgeDto"]

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        nodes = []
        for nodes_item_data in self.nodes:
            nodes_item = nodes_item_data.to_dict()
            nodes.append(nodes_item)

        edges = []
        for edges_item_data in self.edges:
            edges_item = edges_item_data.to_dict()
            edges.append(edges_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "nodes": nodes,
                "edges": edges,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.knowledge_edge_dto import KnowledgeEdgeDto
        from ..models.knowledge_graph_config_dto import KnowledgeGraphConfigDto
        from ..models.knowledge_node_dto import KnowledgeNodeDto

        d = dict(src_dict)
        config = KnowledgeGraphConfigDto.from_dict(d.pop("config"))

        nodes = []
        _nodes = d.pop("nodes")
        for nodes_item_data in _nodes:
            nodes_item = KnowledgeNodeDto.from_dict(nodes_item_data)

            nodes.append(nodes_item)

        edges = []
        _edges = d.pop("edges")
        for edges_item_data in _edges:
            edges_item = KnowledgeEdgeDto.from_dict(edges_item_data)

            edges.append(edges_item)

        knowledge_graph_dto = cls(
            config=config,
            nodes=nodes,
            edges=edges,
        )

        return knowledge_graph_dto
