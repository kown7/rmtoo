import os
import glob


def task_rmtoo():
    reqs = [i for i in glob.glob('specifications/**', recursive=True) if os.path.isfile(i)]
    topics = [i for i in glob.glob('topics/**', recursive=True) if os.path.isfile(i)]
    html = [i for i in glob.glob('html/**', recursive=True) if os.path.isfile(i)]
    deps = ['Config.json']
    deps.extend(reqs)
    deps.extend(topics)
    deps.extend(html)
    return {
        'file_dep':  deps,
        'targets': ['artifacts/reqtopics.tex', 'artifacts/reqs-version.txt',
                    'artifacts/html/',
                    'artifacts/req-graph1.dot', 'artifacts/req-graph2.dot'],
        'actions': ['rmtoo -j file://Config.json']
    }

EPS_FILES = [ 'stats_reqs_cnt', 'stats_burndown', 'stats_sprint_burndown']
def task_pdflatex():
    texs = [i for i in glob.glob('artifacts/*.tex', recursive=True) if os.path.isfile(i)]
    return {
        'file_dep':  texs + [ os.path.join('artifacts', i + '.pdf')
                              for i in EPS_FILES ],
        'targets': ['artifacts/testspecification.pdf'],
        'actions': [3*'pdflatex -interaction=nonstopmode -output-directory=artifacts latex/testspecification.tex;']
    }

def task_gnuplot():
    for filename in [ 'gnuplot_stats_reqs_cnt.inc',
                      'gnuplot_stats_burndown.inc',
                      'gnuplot_stats_sprint_burndown.inc' ]:
        yield {
            'name': filename,
            'file_dep': [os.path.join(os.getcwd(),
                         os.environ['RMTOO_CONTRIB_DIR'],
                         'rmtoo/contrib/', filename)],
            'targets': [os.path.join('artifacts', filename.split('.')[0][8:] +
                        '.eps')],
            'actions': ['cd artifacts && gnuplot %(dependencies)s']
        }

def task_eps2pdf():
    for filename in EPS_FILES:
        yield {
            'name': filename,
            'file_dep': [os.path.join('artifacts', filename + '.eps')],
            'targets': [os.path.join('artifacts', filename + '.pdf')],
            'actions': ['epstopdf %(dependencies)s']
        }

def task_dot2png():
    for filename in [ 'req-graph2']:
        yield {
            'name': filename,
            'file_dep': [os.path.join('artifacts', filename + '.dot')],
            'targets': [os.path.join('artifacts', filename + '.png')],
            'actions': ['dot -Tpng -o %(targets)s %(dependencies)s']
        }

def task_dot2png_flat():
    for filename in [ 'req-graph1' ]:
        yield {
            'name': filename,
            'file_dep': [os.path.join('artifacts', filename + '.dot')],
            'targets': [os.path.join('artifacts', filename + '.png')],
            'actions': ['unflatten -l 23 %(dependencies)s | dot -Tpng -o %(targets)s']
        }
