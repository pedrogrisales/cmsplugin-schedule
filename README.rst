=====
Djangocms-schedule
=====

djangocms-schedule is a plugin for django-cms

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "djangocms_schedule" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'djangocms_schedule',
    )

2. Include the djangocms_schedule URLconf in your project urls.py like this::

    url(r'^', include('djangocms_schedule.urls')),

3. Run `python manage.py migrate` to create the djangocms_schedule models.
