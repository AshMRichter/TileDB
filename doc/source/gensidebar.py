#
# This file generates the sidebar/toctree for all TileDB projects and should
# be copied to each project when it is updated.
#
# This file is originally from the RobotPy documentation project
# https://github.com/robotpy/robotpy-docs, licensed under Apache v2.
#

import os

def write_if_changed(fname, contents):

    try:
        with open(fname, 'r') as fp:
            old_contents = fp.read()
    except:
        old_contents = ''

    if old_contents != contents:
        with open(fname, 'w') as fp:
            fp.write(contents)

def generate_sidebar(conf, conf_api):

    version = conf['rtd_version']

    lines = [
        '', '.. DO NOT MODIFY! THIS PAGE IS AUTOGENERATED!',
        '   To edit the sidebar, modify gensidebar.py and re-build the docs.', ''
    ]

    url_base = 'https://docs.tiledb.io'
    lang = 'en'

    def toctree(name):
        lines.extend(['.. toctree::',
                      '    :caption: %s' % name,
                      '    :maxdepth: 1',
                      ''])

    def endl():
        lines.append('')

    def write(desc, link):
        if conf_api == 'tiledb':
            args = desc, link
        else:
            args = desc, '%s/%s/%s/%s.html' % (url_base, lang, version, link)

        lines.append('    %s <%s>' % args)

    def write_api(project, desc, rst_page):
        # From non-root project to root project link
        if project == 'tiledb' and conf_api != 'tiledb':
            args = desc, url_base, lang, version, rst_page
            lines.append('    %s API <%s/%s/%s/%s.html>' % args)
        # From anything to non-root project link
        elif project != conf_api:
            args = desc, url_base, project, lang, version, rst_page
            lines.append('    %s API <%s/projects/%s/%s/%s/%s.html>' % args)
        # Local project link
        else:
            args = desc, rst_page
            lines.append('    %s API <%s>' % args)

    #
    # Specify the sidebar contents here
    #

    toctree('Getting Started')
    write('Introduction', 'introduction')
    write('Quickstart', 'quickstart')
    write('Installation', 'installation')
    write('Usage', 'usage')
    endl()

    toctree('API Reference')
    write_api('tiledb', 'C', 'c-api')
    write_api('tiledb', 'C++', 'c++-api')
    write_api('tiledb-py', 'Python', 'python-api')
    endl()

    toctree('Tutorials')
    write('Dense Arrays', 'dense-arrays')
    write('Sparse Arrays', 'sparse-arrays')
    write('Multi-attribute Arrays', 'tutorials/multi-attribute-arrays')
    write('Variable-length Attributes', 'tutorials/variable-length-attributes')
    write('Tiles', 'tutorials/tiles')
    write('Dense data ingestion', 'tutorials/dense-data-ingestion')
    write('Working with S3', 'tutorials/working-with-s3')
    endl()

    toctree('Further Reading')
    write('Basic Concepts', 'futher-reading/basic-concepts')
    write('System Architecture', 'futher-reading/system-architecture')
    write('Physical Organization', 'futher-reading/physical-organization')
    write('Writing', 'futher-reading/writing/index')
    write('Updating', 'futher-reading/updating')
    write('Consolidation', 'futher-reading/consolidation')
    write('Reading', 'futher-reading/reading/index')
    write('Compression', 'futher-reading/compression')
    write('Asynchronous I/O', 'futher-reading/asynchronous-io')
    write('Key-Value Store', 'futher-reading/key-value-store')
    write('Object Management', 'futher-reading/object-management')
    write('Storage Backends', 'futher-reading/storage-backends')
    write('Virtual Filesystem', 'futher-reading/virtual-filesystem')
    write('Language Bindings', 'futher-reading/language-bindings')
    write('Concurrency', 'futher-reading/concurrency')
    write('Consistency', 'futher-reading/consistency')
    endl()

    write_if_changed('_sidebar.rst.inc', '\n'.join(lines))
