from dcs.point import MovingPoint
from dcs.task import Land, RunScript

from .pydcswaypointbuilder import PydcsWaypointBuilder


class LandingZoneBuilder(PydcsWaypointBuilder):
    def build(self) -> MovingPoint:
        waypoint = super().build()
        # Create a landing task, currently only for Helos!
        # Calculate a landing point with a small buffer to prevent AI from landing
        # directly at the static ammo depot and exploding
        landing_point = waypoint.position.random_point_within(30, 20)
        # Use Land Task with 30s duration for helos
        combat_land = self.flight.coalition.game.settings.use_ai_combat_landing
        waypoint.add_task(Land(landing_point, duration=30, combat_landing=combat_land))
        if waypoint.name == "DROPOFFZONE":
            script = RunScript(
                f'trigger.action.setUserFlag("split-{id(self.package)}", true)'
            )
            waypoint.tasks.append(script)
        return waypoint
