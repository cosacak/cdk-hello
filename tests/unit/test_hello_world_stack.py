import json
import pytest

from aws_cdk import core
from hello_world.hello_world_stack import HelloWorldStack


def get_template():
    app = core.App()
    HelloWorldStack(app, "hello-world")
    return json.dumps(app.synth().get_stack("hello-world").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
