|ico2| Measure Distance
=======================

.. dropdown:: Find it
   :icon: search

   |LMB| |ico1| |then| |ico2| 

   .. dropdown:: Show me
      :icon: video
      :open:

      .. youtube:: T6bHf7S_SuQ

.. dropdown:: In a nutshell
   :open:

   Acts on the :doc:`/all/ui/layers/token_actors`.

   .. card::

      Keyboard
      ^^^
      .. list-table::

         * - :kbd:`Space`
           - Follow the marked path

   .. card::

       Mouse
       ^^^
       .. list-table::

          * - |hLMB| |and| drag
            - Start measuring.
          * -  :kbd:`ctrl` (:kbd:`cmd` on Mac) |and| |LMB|
            - Mark a waypoint.
          * - |RMB|
            - Cancel marked path

   .. include:: /lib/global-keys.rst

To measure a straight path
--------------------------

- Select a grid square (or a token).
- |hLMB| |and| drag.

A line of grid squares will highlight in green. Ahead of the path two numbers are displayed, for straight paths both numbers are the same and indicate the length of the path.

.. dropdown:: Show me
   :icon: video

   .. youtube:: 2nrNVI_Y2P8
   
To measure a non-straight path
------------------------------

- Select a grid square (or a token).
- |hLMB| |and| drag.
- Where you want to change the path's direction:
  - Hold :kbd:`ctrl` (:kbd:`cmd` on mac) |and| |LMB| (keep holding the :kbd:`ctrl` key while clicking)

  The clicked grid square becomes a fixed point (waypoint) on the path.

  With at least one waypoint placed, you can release all keys and mouse buttons. As you move your mouse the path will follow.
- You can :kbd:`ctrl` |and| |LMB| as many times as necessary to draw your path.

The numbers displayed ahead of the path show; the length of the current 'leg' of the path, and the total distance covered by the path in ``[]``.

.. dropdown:: Show me
   :icon: video

   .. youtube:: TkG7jHN1-xo

To have a token follow the path
-------------------------------

You must start the path at the token (it will be selected when you start the path).

.. note:: You can only move a token that you control.

- Draw the path as described above. 
- Once you have completed the path, press the :kbd:`Space` on your keyboard (if you are drawing a path with no waypoints keep holding the mouse button until the token starts to move). 

The token will move along the highlighted path (unless this is prevented by an obstacle, such as a wall).

.. note:: The end of the path is wherever the highlighted path ends, `not` the last waypoint placed.

.. dropdown:: Show me
   :icon: video

   .. youtube:: PXvF7YqvdNM

To cancel a path
----------------

To cancel a path with no waypoints, just release the mouse button.

To cancel a path with waypoints, just |RMB|

.. dropdown:: Show me
   :icon: video

   .. youtube:: YZ8F2AIjeFY

.. |ico1| image:: /all/ui/images/tool_icons/token_controls_icon.png
   :height: 2ex
   :alt: token controls icon
   :class: no-scaled-link
.. |ico2| image:: /all/ui/images/tool_icons/tokens/measure_distance_icon.png
   :height: 2ex
   :alt: measure distance icon
   :class: no-scaled-link

.. rubric:: Footnotes

