import multiprocessing

bind = "0.0.0.0:8080"
errorlog = '/home/simon/projects/ntuhcorelab/gunicorn/gunicorn.error.log'
accesslog = '/home/simon/projects/ntuhcorelab/gunicorn/gunicorn.access.log'
proc_name = 'ntuhcorelab'
reload = True
