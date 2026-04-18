class WallSegment:
    def __init__(self, start, end, stability):
        self.start = start
        self.end = end
        self.stability = stability

class SpineHub:
    def __init__(self):
        # Coordinates for Level 1: The Spine
        self.walls = [
            WallSegment((100, 100), (1100, 100), 1.0), # North
            WallSegment((100, 600), (1100, 600), 1.0), # South
            WallSegment((500, 100), (500, 600), 0.4), # The Breach (Frayed Sector)
        ]
        self.tension_index = 1.0

# This is the specific name the orchestrator is looking for
spine_hub = SpineHub()
