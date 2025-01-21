import aws_cdk as core
import aws_cdk.assertions as assertions

from automating_devops_task.automating_devops_task_stack import AutomatingDevopsTaskStack

# example tests. To run these tests, uncomment this file along with the example
# resource in automating_devops_task/automating_devops_task_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AutomatingDevopsTaskStack(app, "automating-devops-task")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
