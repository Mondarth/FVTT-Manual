Tiles Layer
===========

The tile layer is edited using |ico1| :doc:`/all/ui/tools/tiles`.

Tile Types
----------

There are two categories of tile on the tiles layer; standard and overhead. A tile's elevation dictates which 'type' it is considered to be.

.. attention:: The tiles layer distinguishes these two file types and restricts your ability to interact with them. If you are currently on the 'background' then you can interact with :ref:`standard <standard tiles>` if you are on the 'foreground' you can only interact with :ref:`overhead <overhead tiles>` tiles.

   While editing tiles with the |ico1| :doc:`/all/ui/tools/tiles` you can swich between editing standard or over head tiles using the |ico2| :doc:`/all/ui/tools/tiles/foreground`.

.. _standard tiles:

Standard Tiles
~~~~~~~~~~~~~~

Also called 'background' tiles these are any tile with an elevation less than that set for the :doc:`foreground image <foreground_image>`.

.. _overhead tiles:

Overhead Tiles
~~~~~~~~~~~~~~

The distinction between ':ref:`Sandard Tiles`' and Overhead Tiles is slightly diffferent in |FVTT12|. In the past a checkboc indicated when a tile was to be considered 'overhead', in |FVTT12| the tile's :ref:`tile elevation` dictates whether a tile is overhead. Any tiles with an elevation equal to, or higher than, the elevation set for the :doc:`foreground image <foreground_image>` is considered to be an overhead tile.

.. todo:: Link up the various lelevatio settings to the approapriate UI pages.

.. Inline images

.. |ico1| image:: /all/ui/images/tool_icons/tile_controls_icon.png
   :height: 2ex
.. |ico2| image:: /all/ui/images/tool_icons/tiles/foreground_layer_icon.png
   :height: 2ex
.. todo:: Replace with correct icon for foreground toggl

