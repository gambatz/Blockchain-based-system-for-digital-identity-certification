from datetime import timedelta


class Config:
      def __init__(self):
          self.treshold_for_benefit=2
          self.expiring_token_duration = timedelta(days=10)