.. _jak-prispivat:

Jak přispívat?
==============

Našli jste chybu? Chtěli byste něco doplnit? Následující odstavce
popisují, jak lze materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah lze upravovat online přes `repozitář na GitHubu <https://github.com/honzajavorek/cojeapi>`__ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na nějaké složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Vytvořte si virtualenv s Pythonem 3 a nainstalujte závislosti standardně pomocí ``pip install -r requirements.txt``.

Běžná práce
-----------

#. ``make serve``
#. Otevřete si v prohlížeči `<http://127.0.0.1:8000>`__
#. V editoru upravujete texty a v prohlížeči si kontrolujete výsledek

Testy
-----

.. todo::
   Sem napsat něco o testech.

Continuous Integration
----------------------

Na repozitáři je zapojeno `CircleCI <https://circleci.com>`__. Kontroluje různé věci v rámci projektu. Kontrolka:

.. image:: https://circleci.com/gh/honzajavorek/cojeapi/tree/master.svg?style=svg
    :target: https://circleci.com/gh/honzajavorek/cojeapi/tree/master
    :alt: Continuous Integration Status

Pokud se něco nepovedlo, podrobnosti lze zjistit `zde <https://circleci.com/gh/honzajavorek/cojeapi>`__.

ZEIT Now
--------

.. todo::
   Sem napsat něco o deploymentu.
