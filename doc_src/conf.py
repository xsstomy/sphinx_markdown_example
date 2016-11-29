# -*- coding: utf-8 -*-

import sys
import os
# autodoc需要将python模块引入,因此需要将模块所在位置引入path
sys.path.insert(0, os.path.abspath('..'))

import recommonmark
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser

# -- General configuration ------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinxcontrib.autojs',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinxcontrib.napoleon',
    'sphinxcontrib.httpdomain',
]

templates_path = ['_templates']  # templates存放位置

# markdown支持


source_parsers = {
    #'.md': CommonMarkParser,
    '.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']  # 可以识别的后缀
master_doc = 'index'  # 入口文件名
project = u'testsphinx'  # 项目名
copyright = u'2016, hsz'  # 版权
author = u'hsz'  # 作者
version = u'0.0.1'  # 版本
release = u'bsd'  # 授权说明
language = 'zh_CN'  # 语言
exclude_patterns = ['_build']  # 排除出的文件夹编译
pygments_style = 'sphinx'  # 代码高亮样式

# ---html设置------------------------------------------------

html_theme = 'alabaster'  # 编译为html时用的主题

html_static_path = ['_static']  # 静态文件夹所在位置

# Output file base name for HTML help builder.
htmlhelp_basename = 'testsphinxdoc' # 帮助文档根名字
# -- latex设置 ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',

    # Latex figure (float) alignment
    #'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'testsphinx.tex', u'testsphinx Documentation',
     u'hsz', 'manual'),
]

# -- manual设置---------------------------------------

man_pages = [
    (master_doc, 'testsphinx', u'testsphinx Documentation',
     [author], 1)
]

# -- Texinfo 设置 -------------------------------------------

texinfo_documents = [
    (master_doc, 'testsphinx', u'testsphinx Documentation',
     author, 'testsphinx', 'One line description of project.',
     'Miscellaneous'),
]

#---插件-----------------------------------------------------

#intersphinx_mapping = {'https://docs.python.org/': None}  # intersphinx
todo_include_todos = True  # 插件todo启用
todo_link_only=True
url_doc_root = 'https://github.com/hsz1273327/sphinx_markdown_example/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: url_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
