import re
import random
from faker import Faker

fake = Faker()

def generate_fake_log(log_format, regex, domain, start_date, end_date):
  """
  Generates a fake log based on the provided log format, regular expression, domain, start date, and end date.
  """
  # Use the regular expression to find all the parts of the log that need to be replaced
  placeholder_values = re.findall(regex, log_format)

  # Replace each placeholder with a randomly generated fake value
  for placeholder in placeholder_values:
    if placeholder == '{ip}':
      log_format = log_format.replace(placeholder, fake.ipv4())
    elif placeholder == '{date}':
      log_format = log_format.replace(placeholder, fake.date_between_dates(date_start=start_date, date_end=end_date))
    elif placeholder == '{time}':
      log_format = log_format.replace(placeholder, fake.time())
    elif placeholder == '{method}':
      log_format = log_format.replace(placeholder, random.choice(['GET', 'POST', 'PUT', 'DELETE']))
    elif placeholder == '{resource}':
      log_format = log_format.replace(placeholder, fake.uri_path())
    elif placeholder == '{status_code}':
      log_format = log_format.replace(placeholder, str(random.randint(100, 999)))
    elif placeholder == '{user_agent}':
      log_format = log_format.replace(placeholder, fake.user_agent())
    elif placeholder == '{patient_id}':
      log_format = log_format.replace(placeholder, fake.uuid4())
    elif placeholder == '{patient_name}':
      log_format = log_format.replace(placeholder, fake.name())
    elif placeholder == '{doctor_name}':
      log_format = log_format.replace(placeholder, fake.name())
    elif placeholder == '{hospital_name}':
      log_format = log_format.replace(placeholder, fake.company())
    elif placeholder == '{transaction_id}':
      log_format = log_format.replace(placeholder, fake.uuid4())
    elif placeholder == '{account_number}':
      log_format = log_format.replace(placeholder, fake.credit_card_number())

  return log_format

# Example usage
sample_log = '{ip} - - [{date} {time}] "{method} {resource} HTTP/1.1" {status_code} -'
regex = '{[a-z_]+}'

for _ in range(5):
  fake_log = generate_fake_log(sample_log, regex)
  print(fake_log)
