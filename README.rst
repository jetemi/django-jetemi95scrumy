=====
Jetemi95scrumy
=====

Jetemi95scrumy is a simple Django app to show you how a real 
Django app works in the a real life application. Here we would be
working with setting goals, history and goals status.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "jetemi95scrumy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'jetemi95scrumy.apps.Jetemi95ScrumyCongfig',
    ]

2. Include the jetemi95scrumy URLconf in your project urls.py like this::

    path('jetemi95scrumy/', include('jetemi95scrumy.urls')),

3. Run `python manage.py migrate` to create the jetemi95scrumy models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a model (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/jetemi95scrumy/ to participate in the goal setting.
