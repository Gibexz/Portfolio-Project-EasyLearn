from django.utils import timezone
from django_cron import CronJobBase, Schedule
from .models import Client

class CheckSuspensionClientStatus(CronJobBase):
    """Automation for checking suspension status of client accounts and reactivating them if necessary"""

    RUN_EVERY_MINS = 6 * 60 # every 6 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'client.check_suspension_client_status'    # a unique code for this cron job

    def do(self):
        """Code to be executed each time the cron job runs"""
        expired_clients = Client.objects.filter(is_suspended=True, is_blocked=False, suspended_at__isnull=False)
        for client in expired_clients:
            if client.is_suspended_expired():
                client.is_active = True
                client.is_suspended = False
                client.suspended_at = None
                client.suspension_duration = None
                client.suspension_reason = None
                client.save()

