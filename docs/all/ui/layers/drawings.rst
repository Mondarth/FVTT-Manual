Drawing Layer
=============


Like the :doc:`Tiles Layer <tiles>` the drawing layer contains two notional 'sub-layers' this time controlled by their ':ref:`role <drawing roles>`'.


.. _drawing roles:

Drawing Roles
-------------

Drawings can be one of two types: ':ref:`Object <object drawing>`' or ':ref:`Informational <informational drawing>`'. A drawing's role dictates when it is seen, by whom, and how it is affected by the environment.

You select which type of drawing you are working on using the |ico8| :doc:`/all/ui/tools/drawing/informational` toggle under |ico1| :doc:`/all/ui/tools/drawings`.

The drawing type can be changed after it has been created using the 'drawing role' field on the drawing's configuration sheet.

.. todo:: Add link to drawing role field of drawing configuration sheet

.. _object drawing:

Object Drawings
~~~~~~~~~~~~~~~

Object drawings are rendered in the :term:`Primary Canvas Group`. They are affected by scene :ref:`lighting <lighting>` and :ref:`fog of war <fog of war>` exploration. This means that players will only see these drawings once their :ref:`character token` can see that part of the scene.

Because object drawings are in the primary group they interact with other layers (:doc:`background <background_image>`, :doc:`foreground <foreground_image>`, :doc:`tiles <tiles>`, :doc:`tokens <token_actors>`, and :doc:`effects <effects>` ). The elevation and sort order affect how the drawing is rendered in relation to these other layers.

.. todo:: Example video showing how object drawing interact when elevation/sort are changed.

.. todo:: Correct link to player's character token

.. _informational drawing:

Informational Drawings
~~~~~~~~~~~~~~~~~~~~~~

Informational drawings are rendered in the :term:`Interface Canvas Group` and is visible to all players (unless explicitly hidden by making the drawing invisible).

Because informational drawings are in the interface group they appear over all other canvas layers, regardless of their elevation or sort order. However, elevation and sort order `are` significant between informational drawings on the same :doc:`scene </all/concepts/scene>`.


.. todo:: Example video showing how drawing interact when elevation/sort are changed.

.. Inline images

.. |ico1| image:: /all/ui/images/tool_icons/drawing_tools_icon.png
   :height: 2ex
.. |ico8| image:: /all/ui/images/tool_icons/drawings/toggle_information_drawings_icon.png
   :height: 2ex
