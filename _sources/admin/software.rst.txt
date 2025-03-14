Foundry Software
================

The Foundry software is required to play on Foundry VTT. Many people use a hosting provider (e.g. |TheForge|) that takes care of installing and maintaining the Foundry software. If you are forged in fire though you may prefer to host Foundry yourself (it's not so difficult).

Why self-host? Here are a few reasons:

1. Like me, you are a control freak.
2. It gives the ultimate in flexibility and contol.
3. It allows you to host LAN party style sessions without the need for an internet connection (invaluable if your internet is unreliable or slow).
4. It may work out cheaper. Even though I pay for a cloud server to host my online Foundry server, that cloud server does much more than just run Foundry\ [#F1]_.
5. Having a local 'development' Foundy instance (on yyour laptop, say) means you can develop games even when not on the internet.

Why `not` self-host? Here are a few reasons:

1. Requires a few basic computer skills.
2. May cost more. If all you want is a simple 'run my world so we can play' setup (and you all have access to stable internet connections) then a hosted solution like |TheForge| will be fine.


If you go down the hosted Foundry route then most of this adminstrator material will not apply and you should check your nosting provider for details.

For the rest of you, read on...

Where to install the Foundry software
-------------------------------------

There are endless possibilities, so to keep things sane I will consider two main options.

1. Installing on a PC you own, a local install.
2. Installing on a cloud server, a remote install.

Networking
~~~~~~~~~~

This can get a wee bit technical. If you're using a cloud hosted server then most likely its network will be fine (but be careful when choosing a supplier to check any charges for network traffic\ [#F3]_).

Local install
~~~~~~~~~~~~~

You simply need a computer capable of running Foundry. This means a computer with a `minimum` of:

- 1GB of storeage
- 1 CPU core (if you can run withe less let me know how)
- 2GB of RAM
- An network connection (wi-fi or ethernet)

That is the `minimum`, this is `recommended`:

- 1GB of available storage---you will need more once you accumulate assets like images and video, but let's face it storeage is rareuly a problem these days.
- 2 CPU cores
- 4GB RAM (I favour 4GB RAM per core as a minimum\ [#F2]_)

That's it for hardware.

For software, refer to :doc:`install`.


Remote install
~~~~~~~~~~~~~~

This is the same as for a local install but you are usually dealing with a nosting provider and virtual hardware.

I use |DO| and I run one of their :program:`basic` droplets (their name for a virtual server) with 4GB RAM, 2CPUs, and 80GB storage. Ther are other providers, some cheaper, some very expensive.

.. todo:: Add some pointers on finding virtual server

As with a :ref:`Local install` that's it for hardware and you can move on to :doc:`install`.


.. rubric:: Footnotes

.. [#F1] It hosts a VPN node, a couple of websites, and two Foundry servers that I can leave running for my players between sessions. All this costs about the same as two subscription to |TheForge| (needed if you want two always-running games)---and I have more storage space.
.. [#F2] You need more RAM to support more data in the :term:`game system` and :term:`active modules <Active Module>`. The larger you game system and the more active modules you have, teh more RAM you will need.
.. [#F3] My provider (|DO|) includes 4TB of network traffic each month in with each virtual server. I have never come close to using this much.




.. toctree::
   :hidden:

   install.rst
   updating.rst
