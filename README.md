# django-tags

Simple project that illustrate how to create modern API for
resources with tags using django.

## Running a project

To run a project, you first have to install all dependencies. Project uses
python 3.4 and although it might work with different versions of python,
I haven't tested it.

I recommend you using virtualenv or virtualenvwrapper project.

```{bash}
$ pip install -r requirements.txt
```

After you have everything installed, to run the app type

```{bash}
$ cd tags
$ ./manage.py migrate
$ ./manage.py runserver
```

App should be now available in your browser on port :8000.

Have fun!
