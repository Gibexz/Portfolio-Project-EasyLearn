from django.utils import timezone
from django_cron import CronJobBase, Schedule
from .models import Tutor

class CheckSuspensionTutorStatus(CronJobBase):
    """Automation for checking suspension status of tutor accounts and reactivating them if necessary"""

    RUN_EVERY_MINS = 6 * 60 # every 6 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tutor.check_suspension_tutor_status'    # a unique code for this cron job

    def do(self):
        """Code to be executed each time the cron job runs"""
        expired_tutors = Tutor.objects.filter(is_suspended=True, is_blocked=False, suspended_at__isnull=False)
        for tutor in expired_tutors:
            if tutor.is_suspended_expired():
                tutor.is_active = True
                tutor.is_suspended_admin = False
                tutor.suspended_at_admin = None
                tutor.suspension_duration_admin = None
                tutor.suspension_reason_admin = None
                tutor.save()

