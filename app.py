"""Extension declaration, capabilities, health check for Elastic Observability Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "elastic-observability-connector",
    version="0.1.0",
    display_name="Elastic Observability",
    icon="icon.svg",
    capabilities=["elastic_observability:manage"],
    description="Official Imperal connector for Elastic Observability (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("elastic_observability_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Elastic Observability connection(s) configured." if count else "Not connected yet."
    }
