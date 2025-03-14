Glossary
========

.. glossary::

   Action
     An operation that has som effect in the :term:`game world`.
   Active Module
     A :term:`module` can be installed but not active. Only active modules are loaded into a running game and therefore only active modules contribute to the amount of data the clients and server need to accomodate.
   Active Player
     Any player currently connected to the game :term:`session<Game Session>`.
   Administrator
     A :term:`user` with complete access to the |FVTT| server. The administrator manages the game systems, worlds, and modules installed on the |FVTT| server.
   Game System
     A collection of assets that describe the mechanics of a particular RPG. At the time of writing |FVTT| supports 312 game systems.
   Game Master
     A :term:`player` responsible for running the :term:`game session`. This typically involves setting up the :term:`game world`, inviting other players, and then running the gamesession.
   Game Session
     As with regular in-person play |FVTT| is mostly played in sessions\ [#f1]_. When a |GM| starts a :term:`game world`
   Game World
     The collection of scenes, chearacters, items, etc, that constitute the |FVTT| experience for players. See also :doc:`/all/concepts/world`.
   Interface Canvas Group
     This is the render group that contains the main |UI| elements.
   
         A container group which displays interface elements rendered above other canvas groups.
   
         --- `Foundry VTT version 12 API documentation <https://foundryvtt.com/api/classes/client.InterfaceCanvasGroup.html>`_
   Player
     A :term:`user` who is actively engaged in a game on |FVTT|.
   Primary Canvas Group
     The bulk of things that interact on a scene are rendered in the primary canvas group.
 
         The primary Canvas group which generally contains tangible physical objects which exist within the Scene. This group is a CachedContainer which is rendered to the Scene as a SpriteMesh. This allows the rendered result of the Primary Canvas Group to be affected by a BaseSamplerShader.
 
         --- `Foundry VTT version 12 API documentation <https://foundryvtt.com/api/classes/client.PrimaryCanvasGroup.html>`_
   Render
     To draw on the display.
   Target
     The thing to be affected by an :term:`action`.
   Theatre of the Mind
     A form of role play in which players rely on their imagination to create a scene.
   User
    An individual who can log on to a |FVTT| server.

.. rubric:: Footnotes

.. [#f1] Some |GM|\ s also extend play outside strict sessions. This allows players access to a more expansive world. Perhaps between sessions they can tend to charaters currently researching magic, building fortifications, etc.
