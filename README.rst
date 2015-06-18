=====
Universapp
=====

plugin_shortcuts is a plugin for django-cms

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "plugin_agenda" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'plugin_agenda',
    )

2. Include the plugin_agenda URLconf in your project urls.py like this::

    url(r'^', include('plugin_agenda.urls')),

3. Run `python manage.py migrate` to create the plugin_agenda models.

