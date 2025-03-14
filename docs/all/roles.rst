Foundry User Roles
==================

.. toctree::
   :hidden:

   roles/configuring.rst

There is one special 'role', the Administrator this is the user who maintains the highest level of the server (creates :doc:`game worlds <concepts/world>`, installs :doc:`modules <concepts/world>` or :doc:`systems <concepts/system>`, for example).

Within a :doc:`game world <concepts/game>` there are five roles that a |GM| can assign to each player.

1. None
2. Player
3. Trusted Player
4. Assistant GM
5. Game Masters

The specific abilities associated with these roles can be :doc:`configured </all/roles/configuring>` by the |GM|.

.. _roles None:
None
----

This role allows the |GM| to set up a players (assign them ownership a :doc:`concepts/actor` token, for example) before allowing any user to log in as that player.

This role also allows the |GM| to suspend a player (preventing them from logging in to the game) without completely removing them from a game.

.. _roles Player:
Players
-------

Players connect to games run by Game Masters. Generally you will be sent:

- An invitation link (enter this into your browser to get to the :doc:`logon </player/ui/logging-on>` screen).
- A username and password.

These allow you to log on to the Foundry server hosting the game.

Typically, your Game Master will also provide other details, such as access to audio and/or video connections [#f1]_ for use in game.

As a player you should be familiar with the :doc:`main user interface elements </player/ui/overview>`.


Trusted Players
---------------

Trusted Players are Players with some additional permissions. These generally relate to features that, if the players were so inclined, could be easily exploited to cheat. For example, a Trusted Player is permitted to configure their interface to allow manual dice rolls. The manual dice roll facility is primarily intended for in-person games, but some groups like the visceral sensation of frolling physical dice, even when playing remotely.

Assitant GM
-----------

By default a player with the Assistant GM role nas the same permissions as the Game Master.

.. _roles game master:
Game Masters
------------

Game Masters create and run :ref:`games <Game>`. Games may be purchased or created from scratch, it's all up to you.

Once you have a game world then you, as Game Master, will run that game much as you would face-to-face but with the added awesomeness of |FVTT| (some groups use FVTT even when playing in-person).



.. _administrator:
Administrators
--------------

The rarest breed, Administrators are responsible for managing the Foundry server itself. If you are self-hosting (rather than using a hosting service like |TheForgee|) the administator will install Foundry, configure it, add game systems, modules and worlds ready for the Game Masters and Players to use.

If you have access to the :doc:`ui/setup` you are an Administator.

Although administration is a separate role in this manual most of the time the person fulfiling the administrator role will also be the game master.

.. rubric:: Footnotes

.. [#f1] Foundry does support its own audion/video service but most people opt for Discord or Zoom. Your |GM| will provide details.
