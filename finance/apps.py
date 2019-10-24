from django.apps import AppConfig


class FinanceConfig(AppConfig):
    name = 'finance'
    verbose_name = 'Финансовый учет'

    def ready(self):
        try:
            from paymentsScheduler import scheduler
            scheduler.start()
        except ImportError:
            raise ImportError('Error in importing new_month_payment_calculate')

