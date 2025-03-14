|ico2| Select Targets
=====================

.. dropdown:: Find it
   :icon: search

   |LMB| |ico1| |then| |ico2| 

   .. dropdown:: Show me
      :icon: video
      :open:

      .. youtube:: VjvTpi-7iFk

.. dropdown:: In a nutshell
   :open:

   Acts on the :doc:`/all/ui/layers/token_actors`.

   Manages the selection of tokens as the :term:`target <Target>` of subsequent :term:`actions <Action>`.

   .. card::

      Keyboard
      ^^^
      .. list-table::

         * - :kbd:`T`
           - Toggle the targeted state of the token under the mouse cursor.

             Any other targeted tokens will be untargeted.
         * - :kbd:`shift` |and| :kbd:`T`
           - Toggle the targeted state of the token under the mouse cursor.

             Other targeted tokens remain targeted.


   .. card::

       Mouse
       ^^^
       .. list-table::

          * - |LMB|
            - Target the token under the cursor.
          * - :kbd:`shift` |and| |LMB|
            - Toggle targeted state of the token.
          * - |hLMB| |and| drag
            - Target all tokens in the band.
          * - :kbd:`shift` |and| |hLMB| |and| drag
            - Add all tokens in the band to targeted selection.
          * - |dRMB| on any targeted token that

              you do not control\ [#F1]_
            - Untarget all currently targeted tokens.

       .. attention:: Any time the |ico1|\ :doc:`../tokens` tool is active you can target tokens with |dRMB| or :kbd:`T` (holding :kbd:`shift` toggles the token's targeted state when dealing with targeting of multiple tokens).

   .. include:: /lib/global-keys.rst

   .. include:: /lib/general-canvas-layer-controls.rst

Target individual token
------------------------

Either,

A. target the token with |LMB| or
B. place mouse cursor over token and press :kbd:`T`.

.. note:: Any existing selection will be cancelled and replaced with this new selection.


Target multiple tokens
-----------------------

To target more than one token at a time, |hLMB| |and| drag. You will see a rectangular band appear as you drag. Any token that falls inside the band will be selected when the |LMB| is released, any previously targeted tokens are untargeted.

.. important:: Target tokens do not need to be completely inside the selection band. They are selected if any `part` of their token is in the band.

.. important:: Selection is based on the token's tile, not its image. Some token images are larger than the token tile.



Add target to selection
-----------------------

To add another target either,

A. :kbd:`shift` |and| |LMB| over untargeted token or
B. place mouse cursor over untargeted token and press :kbd:`shift` |and| :kbd:`T`


Add multiple targets to an existing selection
---------------------------------------------

To add multiple tokens to selected targets, :kbd:`shift` |and| |hLMB| |and| drag.

.. note:: :kbd:`shift` `does not` untarget tokens when using this method.


Untarget individual token
-------------------------

To untarget a token either,

A. :kbd:`shift` |and| |LMB| on a targeted token, or
B. place mouse cursor over a targeted token and :kbd:`shift` |and| :kbd:`T`.


Untarget `all` currently targeted tokens
----------------------------------------

To untarget all tokens either,

A. |dRMB| on any curently targeted token, 
B. |hLMB| |and| drag to 'select' an area of the canvas that contains no tokens.



.. rubric:: Footnotes

.. [#F1] If you can control the token, |dRMB| will open the associated actor or token sheet. So, if you are the |gm| this means you need to use one of the other targeting methods.

.. |ico1| image:: /all/ui/images/tool_icons/token_controls_icon.png
   :height: 2ex
   :alt: token controls icon
   :class: no-scaled-link
.. |ico2| image:: /all/ui/images/tool_icons/tokens/select_targets_icon.png
   :height: 2ex
   :alt: select targets icon
   :class: no-scaled-link
