from opentelemetry import trace, baggage

tracer = trace.get_tracer("my.tracer")
with tracer.start_as_current_span(name="root_span") as root_span:
    parent_ctx = baggage.set_baggage("context", "parent")
    with tracer.start_as_current_span(name="child_span", context=parent_ctx) as child_span:
        child_context = baggage.set_baggage("context", "child")

print(baggage.get_baggage("context", parent_ctx))
print(baggage.get_baggage("context", child_context))
