def resource_load(*resources):
    for resource in resources:
        __import__('hackathon.resource.{}'.format(resource))


def model_load(*models):
    for model in models:
        __import__('hackathon.database.{}'.format(model))
