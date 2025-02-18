Game User Interface
===================

Once logged in to the game you will see the main Foundry user interface. The default interface consists of the following areas [#f1]_.



.. _canvas:

Canvas
------


The canvas is where all the action takes place. It is built up in layers, each layer specialising in one of Foundry's interactive elements.

The layers are :term:`rendered<Render>` in the following order (lowest to highest [#f2]_).

.. toctree::
   :maxdepth: 1
   
   layers/background_image.rst
   layers/tiles.rst
   layers/token_actors.rst
   layers/foreground_image.rst
   layers/weather.rst
   layers/drawings.rst
   layers/effects.rst
   layers/templates.rst
   layers/sounds.rst


In front of the canvas |FVTT| displays the |UI| application windows (outlined in the following sections).


Tools
-----

.. toctree::
   :hidden:
   
   tools/tokens.rst
   tools/templates.rst
   tools/tiles.rst
   tools/drawings.rst
   tools/walls.rst
   tools/lights.rst
   tools/sounds.rst
   tools/regions.rst
   tools/journal.rst

In the upper left of the |UI| we find the tool buttons. These are presented as two columns:


1. To the left, the main tool groups are shown, each tool maps (roughly) to one of the :ref:`canvas layers <canvas>`.
2. To the right of the main tool groups are the sub-tool buttons. These change according to which of the main tool groups is active and provide the tools used to interact with the :ref:`canvas layers<canvas>`.

Which tools are available will depend upon:

1. Your :doc:`access permissions</all/roles/configuring>`, in general Players(|pi|) have fewer tools than Game Masters(|gi|).
2. The :doc:`modules </all/concepts/module>` active in your world. Modules may add new tools and tool groups.

.. image:: /all/ui/images/tool_panels/token_controls.png
   :align: right

.. list-table:: Tool Groups
   
   * - .. image:: /all/ui/images/tool_icons/token_controls_icon.png
     - :doc:`tools/tokens`
     - |gi| |pi|
   * - .. image:: /all/ui/images/tool_icons/measurement_controls_icon.png
     - :doc:`tools/templates`
     - |gi| |pi|
   * - .. image:: /all/ui/images/tool_icons/tile_controls_icon.png
     - :doc:`tools/tiles`
     - |gi|
   * - .. image:: /all/ui/images/tool_icons/drawing_tools_icon.png
     - :doc:`tools/drawings`
     - |gi|
   * - .. image:: /all/ui/images/tool_icons/wall_controls_icon.png
     - :doc:`tools/walls`
     - |gi|
   * - .. image:: /all/ui/images/tool_icons/lighting_controls_icon.png
     - :doc:`tools/lights`
     - |gi|
   * - .. image:: /all/ui/images/tool_icons/ambient_sound_controls_icon.png
     - :doc:`tools/sounds`
     - |gi|
   * - .. image:: /all/ui/images/tool_icons/region_controls_icon.png
     - :doc:`tools/regions`
     - |gi|
   * - .. image:: /all/ui/images/tool_icons/journal_notes_icon.png
     - :doc:`tools/journal`
     - |gi| |pi|



.. Inline images


Scene navigation
----------------

.. toctree::
   :hidden:
   
   navigation_bar.rst

At the top of the |UI| are the main scene :doc:`navigation buttons <navigation_bar>`. These provide a quick way to move between :doc:`scenes </all/concepts/scene>`.

As a player you will often have access to only one scene, the :ref:`active scene <active scene>`, but the |GM| may enable navigation access to other scenes allowing you to switch which scene is displayed on your :doc:`canvas </all/concepts/canvas>`.

.. note:: One common use of multiple scenes is providing a 'landing page' from which players can quickly access information about the campaign or their character.

In more complex adventures you may be transitioning between different scenes for any numbes of reasons, for example:

- Your party are in a large dungeon and the |GM| has broken it into multiple maps (scenes) in order to reduce the load on browsers.
- Your party are spread over multiple scenes and the |GM| is allowing you to 'follow the action'.
- Your party are switching between realms, times, or others dimensions and these are represented by multiple scenes.

The possiblilities are endless.

.. attention:: Regardless of how many scenes you have access to there will only ever be one :ref:`active scene <active scene>`.

Tabs
----



.. toctree::
   :hidden:
   
   tabs/chat.rst
   tabs/combat.rst
   tabs/actors.rst
   tabs/items.rst
   tabs/journal.rst
   tabs/rollable_tables.rst
   tabs/card_stacks.rst
   tabs/playlists.rst
   tabs/compendiums.rst
   tabs/settings.rst


To the right of the |UI| is the 'tabs dock'. The following tabs are present by default.

:fas:`comments`:guilabel:`Chat Messages`

This is the main channel by which interactions are reported. Everything from dice rolls, requests for information, messages between players, or between players and the |GM|, all are recorded on the Chat log.

At the bottom of the Chat tab is an entry box for messages, see :ref:`chat messsages`.

.. todo:: Add section with details on chat message entry



|swords|:guilabel:`Combat Encounters`

Combat is, for many games, a central feature. The combat tab is the primary interface for managing combat interactions.

:fas:`map`:guilabel:`Scenes`

Scenes configure the canvas. They can be used to (for example):

- Display an inteactive map to players.
- Display a dungeon map, revealing only what the player's character token can see.
- Display an image during :term:`theatre of the mind` play.

:fas:`user`:guilabel:`Actors`

An Actor is any agent within the game (principally |PC|'s and |NPC|'s).

As a Player this tab will contain your playable character(s).

As a |GM| this tab will contain many actors as you have access to both the players charactres and all the non-player/playable chearacters.

:fas:`suitcase`:guilabel:`Items`

What is the fun of adventuring unless you can find, steal, gift, be gifted, or otherwise exchange 'stuff'. That 'stuff' ir represented by items.

The items tab contains the items you can access. (These are not items in your characters possession, those are recorded with the character's Actor).

:fas:`book-open`:guilabel:`Journal`

Journals contain all manner of information.

As a player your |GM| may giv access to journals containing information relevant to an adventure, you may also have a 'personal' journal that you can use to record information your character discovers.

As a |GM| you may have many journals available describing the campaign or adventure.


:fas:`th-list`:guilabel:`Rollable Tables`

Rollable tables are exactly what they sound like, tables that can be used in combination with dice to select some random outcome.

|cards|:guilabel:`Card Stacks`



:fas:`music`:guilabel:`Playlists`

This tab provides access to sound controls. This may be as simple as controlling the relative sound levels between background music and ambient sounds, or it may provide access to choose sounds to be played.


:fas:`atlas`:guilabel:`Compendium Packs`

Compendium packs provide access to 'offline' information. Compendium information is held on the Foundry server and only provided to the browser when requested. Keeping information in compendiums reduces the amount of information browsers need to maintain locally.


:fas:`cogs`:guilabel:`Game Settings`

Fairly self explanatory, this tab provides access to game settings.

Players
-------

.. toctree::
   :hidden:

   players.rst

Down in the lower left of the |UI| you find the :doc:`players <players>` list. This can be expanded/collapsed by |LMB|. When expanded you will see a colour coded list of current players.

Hotbar
------

.. toctree::
   :hidden:

   hotbar.rst

The :doc:`hotbar <hotbar>` area (bottom of |UI|)ll provides rapid access to pretty much any function you like. Fully customisable by players the hotbar can be populated with functions from around the Foundry interface collecting them into one location.

The benefit being that you don't need to go through potentially many clicks to access a function, simply drop
it onto the hotbar as a shortcut and it becomes one click away.


.. rubric:: Footnotes

.. [#f1] As is repeatedly noted throughout this manual, the Foundry interface may look different because it can be changed by active modules.
.. [#f2] This is a lie. The actual :term:`render` order is also influenced by an object's altitude and sort order (and can be further complicated if add-on modules are used). Howeves, the basic order shown is good for a mental model of how the layers are ordered.

.. |swords| image:: /all/ui/images/tab_icons/swords.png
   :height: 2ex
.. |cards| image:: /all/ui/images/tab_icons/cards.png
   :height: 2ex
