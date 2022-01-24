from aws_cdk import (
    # Duration,
    core as cdk,
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_,
    aws_iam,
    aws_cloudwatch as cloudwatch_,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions_,
    aws_cloudwatch_actions as actions_,
    aws_dynamodb as dynamodb_,    # aws_sqs as sqs,
)
from sprint4.sprint4_stack import Sprint4Stack

class Sprint4Stage(cdk.Stage):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        sprint4_stack=Sprint4Stack(self,'sprint4Stack')
     