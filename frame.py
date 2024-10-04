import date
import fire


def display_date(day, width, info):
  display_title(day, width)
  center_text(width, info['day'])
  center_text(width, f'{info["date"]} {info["month"]}')
  center_text(width, info['year'])
  if day == 'today':
    center_text(width, info['time'])

def main(day='today'):
  width = 25
  line = width * '-'
  info = date.get_info(day)
  print(line)
  display_date(day, width, info)
  print(line)


def center_text(width, txt):
  print(f'|{txt.center(width - 2)}|')

def display_title(day, width):
  if day == 'tomorrow':
    title = 'Tomorrow Will Be:'
  elif day == 'yesterday':
    title = 'Yesterday Was:'
  else:
    title = 'Today Is:'
  line = len(title) * '-'
  center_text(width, title)
  center_text(width, line)


if __name__ == '__main__':
  fire.Fire(main)
