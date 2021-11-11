import sys

def handler(event, context):
  print(event)
  print(context)
  return 'Hello from AWS Lambda using Python' + sys.version + '!'