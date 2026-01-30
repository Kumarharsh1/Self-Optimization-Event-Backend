class EventBus:
    def publish(self, event_type: str, data: dict):
        print(f"[EVENT BUS] Event received -> {event_type}")
        print(f"[DATA] {data}")
