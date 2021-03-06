import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

######## CHANGE THIS ##########
project_name = "helloworld"
###############################

home_dir = os.getcwd()
master_url = 'http://127.0.0.1:8000'
master_app = 'runestone'
serving_dir = "./build/helloworld"
dest = "../../static"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/helloworld",
        sourcedir="_sources",
        outdir="./build/helloworld",
        confdir=".",
        project_name = "helloworld",
        template_args={'course_id': 'helloworld',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 0,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true',
                       'dburl': 'postgres://launchclass:toinfinityandbeyond@localhost/runestone',
                       'basecourse': 'helloworld',
                       'lang': 'python'
                        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.
