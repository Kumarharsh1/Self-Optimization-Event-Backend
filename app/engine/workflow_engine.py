from app.core.event_bus import EventBus

class WorkflowEngine:
    def __init__(self):
        self.bus = EventBus()

    def process_event(self, event: dict):
        event_type = event.get("event_type", "unknown")
        data = event.get("data", {})

        self.bus.publish(event_type, data)

        return {
            "event_type": event_type,
            "workflow": "default",
            "status": "executed"
        }
