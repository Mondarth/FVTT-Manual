# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Ulenar's FoundryVTT Documentation"
copyright = '2024, UlenarOfMondarth'
author = 'UlenarOfMondarth'
release = '12.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'sphinx.ext.todo', 'sphinxcontrib.mermaid', 'sphinxcontrib.youtube', 'sphinx_design']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'style_external_links': True
}
html_static_path = ['_static']
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css"
]

rst_prolog = """
.. |UI| replace:: :abbr:`UI (User Interface)`
.. |GM| replace:: :abbr:`GM (Game Master)`
.. |PC| replace:: :abbr:`PC (Player Character)`
.. |NPC| replace:: :abbr:`NPC (Non-Player Character)`
.. |FVTT| replace:: :abbr:`FVTT (Foundry Virtual Table Top)`
.. |FVTT12| replace:: :abbr:`FVTT V12 (Foundry Virtual Table Top version 12)`
.. |mc-hand| replace:: hand
.. |gi| image:: /all/ui/images/util/GM_icon.png
   :height: 2ex
   :class: no-scaled-link
   :alt: Game Master
.. |pi| image:: /all/ui/images/util/Player_icon.png
   :height: 2ex
   :class: no-scaled-link
   :alt: Player
.. |then| replace:: :octicon:`arrow-right`
.. |and| replace:: :octicon:`plus`
.. |hLMB| replace:: Hold :kbd:`LMB`
.. |dLMB| replace:: Double :kbd:`LMB`
.. |hMMB| replace:: Hold :kbd:`MMB`
.. |hRMB| replace:: Hold :kbd:`RMB`
.. |dRMB| replace:: Double :kbd:`RMB`
.. |LMB| replace:: :kbd:`LMB`
.. |MMB| replace:: :kbd:`MMB`
.. |RMB| replace:: :kbd:`RMB`
.. |MMW| replace:: :kbd:`Mouse Wheel`
"""

# -- Ensure TODOs are output (these should all be cleared before a commit)
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#directive-todo

todo_include_todos = True
todo_emit_warnings = True
