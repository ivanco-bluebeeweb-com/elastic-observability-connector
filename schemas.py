"""Pydantic schemas for Elastic Observability Connector."""
from __future__ import annotations
from typing import Any, Optional, List, Dict
from pydantic import BaseModel, Field

class NoParams(BaseModel):
    """Empty parameters model."""
    pass

class ConnectParams(BaseModel):
    label: str = Field(default="", description="Friendly connection label, e.g. Primary Elastic Observability.")
    api_key: str = Field(description="Observability API Key")
    base_url: str = Field(default="https://cloud.elastic.co/api/v1", description="Elastic Observability API base URL.")

class ConnectionIdParams(BaseModel):
    connection_id: str = Field(default="", description="Connection identifier (empty uses active connection).")

class ConnectionRecord(BaseModel):
    id: str
    label: str
    masked_key: str
    base_url: str
    is_active: bool

class ConnectionList(BaseModel):
    connections: list[ConnectionRecord]
    total: int

class DeleteResult(BaseModel):
    success: bool
    message: str

class MetricRecord(BaseModel):
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    raw: Dict[str, Any] = Field(default_factory=dict)

class MetricList(BaseModel):
    metrics: list[MetricRecord]
    total: int

class ListMetricParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    limit: int = Field(default=20, ge=1, le=100, description="Max records to return.")

class GetMetricParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    metric_id: str = Field(description="Elastic Observability Metric ID.")

class AuditHealthReport(BaseModel):
    healthy: bool
    total_metrics: int
    details: Dict[str, Any] = Field(default_factory=dict)
    summary: str
