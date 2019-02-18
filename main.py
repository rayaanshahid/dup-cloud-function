import json
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
configurations = None
with open('config.json') as f:
    configurations = f.read()
config = json.loads(configurations)

def trigger_file_upload_topic7(data, context):
    print('With PubSub: {}'.format(context.event_id))
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    print('Metageneration: {}'.format(data['metageneration']))
    print('Created: {}'.format(data['timeCreated']))
    print('Updated: {}'.format(data['updated']))
    project_id = config.get("PROJECT_ID")
    topic_name = config.get("TOPIC_NAME")
    topic_path = publisher.topic_path(project_id, topic_name)
    encoded_data = json.dumps(data).encode('utf-8')
    future = publisher.publish(topic_path, data=encoded_data)
    print('Published message, with future data {}'.format(future.result()))
