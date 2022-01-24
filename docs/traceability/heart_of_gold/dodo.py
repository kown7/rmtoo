import os
import glob
import git


def task_rmtoo():
    reqs = [i for i in glob.glob('specifications/**', recursive=True) if os.path.isfile(i)]
    topics = [i for i in glob.glob('topics/**', recursive=True) if os.path.isfile(i)]
    html = [i for i in glob.glob('html/**', recursive=True) if os.path.isfile(i)]
    deps = ['Config.json', 'artifacts/version.txt']
    deps.extend(reqs)
    deps.extend(topics)
    deps.extend(html)
    return {
        'file_dep':  deps,
        'targets': ['artifacts/reqtopics.tex', 'artifacts/reqs-version.txt',
                    'artifacts/html/',
                    'artifacts/req-graph1.dot', 'artifacts/req-graph2.dot'],
        'actions': ['sltoo -j file://Config.json']
    }


def describe_path(subfolder: str):
    """Get hash of latest change to path file/directory"""
    d = []
    try:
        repo = git.Repo(search_parent_directories=True)
    except git.exc.InvalidGitRepositoryError:
        return 'n/a', '00000000'
    for blob in repo.heads.master.commit.tree.traverse():
        commit = next(repo.iter_commits(paths=blob.path))
        if blob.path.startswith(subfolder):
            d.append({'date': commit.committed_date,
                      'blob': blob, 'commit': commit})
    d.sort(key=lambda x: x['date'])
    latest_hash = d[-1]['commit'].hexsha
    desc = repo.git.describe(latest_hash)
    return desc, latest_hash


def task_write_filename():
    def write_revision_information():
        with open(os.path.join('artifacts', 'version.txt'), 'w+') as fp:
            (desc, hexsha) = describe_path('.')
            fp.write(desc)
            fp.write(' --- ')
            fp.write(hexsha[:8])

    yield {
        'name': 'version-file',
        'file_dep': [],
        'targets': [os.path.join('artifacts', 'version.txt')],
        'actions': [write_revision_information]
    }


def task_gnuplot():
    for filename in [ 'gnuplot_stats_reqs_cnt.inc',
                      'gnuplot_stats_burndown.inc',
                      'gnuplot_stats_sprint_burndown.inc' ]:
        yield {
            'name': filename,
            'file_dep': [os.path.join(os.getcwd(),
                         os.environ['RMTOO_CONTRIB_DIR'],
                         filename)],
            'targets': [os.path.join('artifacts', filename.split('.')[0][8:] +
                        '.eps')],
            'actions': ['cd artifacts && gnuplot %(dependencies)s']
        }

EPS_FILES = [ 'stats_reqs_cnt', 'stats_burndown', 'stats_sprint_burndown']
def task_pdflatex():
    texs = [i for i in glob.glob('artifacts/*.tex', recursive=True) if os.path.isfile(i)]
    return {
        'file_dep':  texs + [os.path.join('artifacts', i + '.pdf')
                             for i in EPS_FILES] + [
                                     os.path.join('artifacts', 'version.txt')],
        'targets': ['artifacts/specification.pdf'],
        'actions': ['cd artifacts;' + 3*'pdflatex -interaction=nonstopmode ../latex/specification.tex;']
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
