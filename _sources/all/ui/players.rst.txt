Players List
============

.. dropdown:: Find it
   :icon: search

   |LMB| :guilabel:`Players`

   .. dropdown:: Show me
      :icon: video
      :open:

      .. youtube:: gtw2LRrpkFY

In the lower left corner of the Foundry |UI| is the :guilabel:`Players` list. When collapsed, this shows the currently :term:`active player`\ s' user names next to small circles coloured according to the setting in :ref:`user configuration<UCD player color field>`.

.. dropdown:: Show me

  .. figure:: /all/ui/images/player/Players_List_collapsed.png
     :align: center
     :alt: Example of a Collapsed Players List

     Example Collapsed Players List


The list can be expanded to show all players (|LMB|:guilabel:`Players`) regardless of whether they are currently connected to the game session. The expanded list shows all players registered in the game. Each player has a circle to the left of their name, if this circle is empty the player is not connected to this game session. When a player is connected to the game session the circle is filled with their selected :ref:`Player Color<UCD player color field>`.

.. dropdown:: Show me

  .. figure:: /all/ui/images/player/Players_List_expanded.png
     :align: center
     :alt: Example of a Expanded Players List

     Example Expanded Players List

Players Context Menu
--------------------

.. dropdown:: Find it
   :icon: search

   You are 'Player2' and are opening the :guilabel:`Players` context menu.

   |RMB| :guilabel:`Player2`

   .. dropdown:: Show me
      :icon: video
      :open:

      .. youtube:: YAg5dQ1YcwU

.. note:: The context menu content will vary.

   For example, a |GM|\ |gi| has access to additional actions and players may be able to view another players avatar (if set) but will not have access to other players :doc:`/player/ui/config/player-dialog`


.. list-table:: Player List Context Menu Options

   * - User Configuration
     - |gi| |pi|
     - Opens the :doc:`/player/ui/config/player-dialog`
   * - View Player Avatar
     - |gi| |pi|
     - Displays the avatar set by the player in :ref:`UCD player avatar field`.

       If no avatar is set, this option is not shown.
   * - Pull To Scene
     - |gi|
     - Force the player onto the current scene\ [#f2]_.
   * - Kick Player
     - |gi|
     - Force the player to log out of this :term:`game session`
   * - Ban Player
     - |gi|
     - Force the player to log out of this game session `and`

       prevent them from rejoining\ [#f1]_.

.. dropdown:: Show me
  
   .. grid:: 2

      .. grid-item-card::

         Players Context Menu\ |pi|
         ^^^

         .. image:: /all/ui/images/player/Players_context_menu.png
           :align: center


      .. grid-item-card::

         Players Context Menu\ |gi|
         ^^^

         .. image:: /all/ui/images/gm/Players_context_menu.png



.. rubric:: Footnotes

.. [#f1] Internally this sets the players account role to :ref:`roles None`. To allow the player back the |GM| must :doc:`restore </all/roles>` the player's account to at least the :ref:`roles player` role.
.. [#f2] Sometimes players get lost, lag behind as the party move on, or simply 'wander off' (especially if there are multiple scenes available)---or the system may get confused. Either way, this function allows the |GM| to force players onto a scene.
