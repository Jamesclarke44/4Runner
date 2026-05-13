from .brakes import BRAKES
from .engine_mechanical import ENGINE_MECHANICAL
from .driveline_and_axles import DRIVELINE_AXLES
from .engine_performance import ENGINE_PERFORMANCE
from .transmission import TRANSMISSION

WORKSHOP = {}
WORKSHOP.update(BRAKES)
WORKSHOP.update(ENGINE_MECHANICAL)
WORKSHOP.update(DRIVELINE_AXLES)
WORKSHOP.update(ENGINE_PERFORMANCE)
WORKSHOP.update(TRANSMISSION)