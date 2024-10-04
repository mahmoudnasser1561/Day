from datetime import datetime
from datetime import timedelta

def get_info(day):
  offset = 1 if day == 'tomorrow' else -1 if day == 'yesterday' else 0
  dt_obj = datetime.now() + timedelta(hours = -4) + timedelta(days = offset)
  day = dt_obj.strftime('%A')
  date = dt_obj.strftime('%d')
  month = dt_obj.strftime('%B')
  year = dt_obj.strftime('%Y')
  dt_time = dt_obj.time()
  time = dt_time.strftime('%X')
  return {'day' : day, 'date' : date, 'month' : month, 'year' : year, 'time' : time}

if __name__ == '__main__':
  print(get_info('yesterday'))
  print(get_info('today'))
  print(get_info('tomorrow'))
