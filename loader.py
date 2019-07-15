def resource_load(*resources):
    for resource in resources:
        __import__('ItIsTasty.resource.{}'.format(resource))


def model_load(*models):
    for model in models:
        __import__('ItIsTasty.database.{}'.format(model))
