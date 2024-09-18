from django.shortcuts import get_object_or_404
from ninja import Schema

from domain.schedule.models import Schedule


class PathParamSchedule(Schema):
    schedule_id: int

    def value(self) -> Schedule:
        return get_object_or_404(Schedule, id=self.schedule_id)
