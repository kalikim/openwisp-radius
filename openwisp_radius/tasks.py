from celery import shared_task
from django.core import management


@shared_task
def delete_old_radacct(number_of_days=365):
    management.call_command('delete_old_radacct', number_of_days)


@shared_task
def cleanup_stale_radacct(number_of_days=365):
    management.call_command('cleanup_stale_radacct', number_of_days)


@shared_task
def delete_old_postauth(number_of_days=365):
    management.call_command('delete_old_postauth', number_of_days)


@shared_task
def deactivate_expired_users():
    management.call_command('deactivate_expired_users')


@shared_task
def delete_old_users(older_than_months=12):
    management.call_command('delete_old_users', older_than_months=older_than_months)


@shared_task
def delete_unverified_users(older_than_days=1, exclude_methods=''):
    management.call_command(
        'delete_unverified_users',
        older_than_days=older_than_days,
        exclude_methods=exclude_methods,
    )


@shared_task
def convert_called_station_id(unique_id=None):
    management.call_command('convert_called_station_id', unique_id=unique_id)
