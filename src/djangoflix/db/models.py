from django.db import models

class PublishStateOptions(models.TextChoices):
    # CONSTANT = DB_VALUE, USER_DISPLAY_VALUE
    PUBLISH = "PU", "Published"
    DRAFT = "DR", "Draft"
    UNLISTED = "UN", "Unlisted"
    PRIVATE = "PR", "Private"

