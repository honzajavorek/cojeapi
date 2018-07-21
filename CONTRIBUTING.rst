.. _contributing:

Jak přispívat
=============

Našli jste chybu? Chtěli byste něco doplnit? Následující odstavce
popisují, jak lze materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah lze upravovat online přes `repozitář na GitHubu <https://github.com/honzajavorek/cojeapi>`_ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na nějaké složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Projekt využívá Python 3.6 a `pipenv <https://docs.pipenv.org/>`_.

#. ``git clone ...``
#. ``pipenv install --dev``

Instalace na macOS
^^^^^^^^^^^^^^^^^^

Pokud používáte macOS a `Homebrew <http://homebrew.sh/>`_, tak vám ``brew install python3`` nainstaluje novější verzi, než je 3.6. Proto je potřeba použít ``pyenv``:

#. ``brew install pyenv``
#. ``pyenv install 3.6.6``
#. ``pipenv install --dev --python="$(pyenv root)/versions/3.6.6/bin/python"``

Běžná práce
-----------

#. ``pipenv run sphinx-autobuild . _build/html``
#. Otevřete si v prohlížeči `<http://127.0.0.1:8000>`_
#. V editoru upravujete texty a v prohlížeči si kontrolujete výsledek

ReadTheDocs
-----------

Na GitHubu jsou pouze zdrojové texty. Po každé změně ve větvi ``master`` na GitHubu se automaticky vygenerují webové stránky na službě `ReadTheDocs <https://cojeapi.readthedocs.io/>`_. Následující kontrolka ukazuje, zda se poslední změny povedlo dostat až do webových stránek (zelená), nebo se to nepovedlo kvůli nějaké chybě (červená):

.. image:: https://readthedocs.org/projects/cojeapi/badge/?version=latest
    :target: http://cojeapi.readthedocs.org/cs/latest/?badge=latest
    :alt: Documentation Status

Pokud se něco nepovedlo, podrobnosti lze zjistit na `této stránce  <https://readthedocs.org/projects/cojeapi/builds/>`_, která je ovšem přístupná jen administrátorům.

Závislosti
----------

Projekt využívá `pipenv <https://docs.pipenv.org/>`_, ale ReadTheDocs jej zatím nepodporují (`rtfd/readthedocs.org#3181 <https://github.com/rtfd/readthedocs.org/issues/3181>`_). Proto je nutné vždy při změně závislostí zavolat ``pipenv run pipenv_to_requirements -f -o requirements.txt`` a tím vytvořit i soubor ``requirements.txt``, kterému ReadTheDocs rozumí.

Nejnovější verze Pythonu, jakou ReadTheDocs podporují, je 3.6. Z toho důvodu
ji vyžaduje i tento projekt.

Continuous Integration
----------------------

Na repozitáři je zapojený `Travis CI <http://travis-ci.org/>`_. Zatím pouze
kontroluje, jestli ``requirements.txt`` odpovídají ``Pipfile.lock`` (viz výše).
Kontrolka:

.. image:: https://travis-ci.org/honzajavorek/cojeapi.svg?branch=master
    :target: https://travis-ci.org/honzajavorek/cojeapi
    :alt: Continuous Integration Status

Travis CI je pouze informativní a nezabrání tomu, aby se ``master`` větev
dostala do ReadTheDocs.
