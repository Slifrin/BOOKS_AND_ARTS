from pydantic import BaseModel
from opentelemetry import trace
from typing import Any

class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    address: Address
    tags: list[str]

def flatten_model(model: BaseModel, prefix: str = "") -> dict[str, Any]:
    """Flatten a Pydantic model to OTel-compatible attributes."""
    attributes = {}
    
    for field_name, value in model.model_dump().items():
        key = f"{prefix}.{field_name}" if prefix else field_name
        
        if isinstance(value, dict):
            # Recursively flatten nested models
            nested_model = getattr(model, field_name)
            if isinstance(nested_model, BaseModel):
                attributes.update(flatten_model(nested_model, key))
            else:
                # For plain dicts, convert to JSON string
                attributes[key] = str(value)
        elif isinstance(value, (str, int, float, bool)):
            attributes[key] = value
        elif isinstance(value, list) and all(isinstance(i, (str, int, float, bool)) for i in value):
            attributes[key] = value
        elif value is None:
            continue  # Skip None values
        else:
            attributes[key] = str(value)
    
    return attributes

# Usage
user = User(
    id=123,
    name="John Doe",
    email="john@example.com",
    address=Address(city="NYC", zip_code="10001"),
    tags=["admin", "active"]
)

tracer = trace.get_tracer(__name__)

with tracer.start_as_current_span("process_user") as span:
    print(flatten_model(user, prefix="user"))
    span.set_attributes(flatten_model(user, prefix="user"))