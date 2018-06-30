.. _contributing:

Jak přispívat
=============

Našli jste v materiálech chybu? Chtěli byste je doplnit? Následující odstavce
popisují, jak můžete materiály upravovat a návrhy na změny posílat autorům.

Rychlé úpravy bez instalace
---------------------------

Abyste něco změnili v textech, nemusíte nic instalovat. Obsah materiálů lze upravovat online přes `repozitář na GitHubu <https://github.com/honzajavorek/cojeapi>`_ pomocí ikony s tužkou v pravém horním rohu u každého souboru.

Instalace
---------

Když toho upravujete víc, nebo máte zálusk na jakékoliv složitější kejkle, je lepší mít materiály nainstalované na svém počítači. Projekt využívá Python 3 a `pipenv <https://docs.pipenv.org/>`_.

#. Na stránce `repozitáře <https://github.com/honzajavorek/cojeapi>`_ vytvoříte svou kopii projektu pomocí tlačítka :kbd:`Fork`
#. Pomocí ``git clone`` dostanete svou kopii projektu (fork) na svůj počítač
#. Pomocí ``pipenv install`` nainstalujete závislosti (`co je pipenv? <http://docs.pipenv.org/>`_)

Běžná práce
-----------

#. Pomocí ``git pull`` apod. zajistíte, že je vaše kopie projektu aktuální vůči tomu, co je ve větvi ``master`` na `github.com/honzajavorek/cojeapi <https://github.com/honzajavorek/cojeapi>`_
#. Pomocí ``git checkout -b`` vytvoříte větev pro vaše změny
#. Otevřete si editor
#. V adresáři ``cojeapi`` spustíte ``pipenv shell``
#. V shellu spustíte ``sphinx-autobuild . _build/html``
#. Otevřete si prohlížeč na adrese ``http://127.0.0.1:8000``
#. V editoru upravujete texty a kontrolujete si je v prohlížeči
#. Když jste spokojeni, pomocí ``git push`` pošlete svou větev na GitHub
#. Na GitHubu ze své větve vytvořte Pull Request na `github.com/honzajavorek/cojeapi <https://github.com/honzajavorek/cojeapi>`_

ReadTheDocs
-----------

Na GitHubu jsou pouze zdrojové texty. Po každé změně ve větvi ``master`` na GitHubu se automaticky vygenerují webové stránky na službě `ReadTheDocs <https://cojeapi.readthedocs.io/>`_. Následující kontrolka ukazuje, zda se poslední změny povedlo dostat až do webových stránek (zelená), nebo se to nepovedlo kvůli nějaké chybě (červená):

.. image:: https://readthedocs.org/projects/cojeapi/badge/?version=latest
    :target: http://cojeapi.readthedocs.org/cs/latest/?badge=latest
    :alt: Documentation Status

Pokud se něco nepovedlo, podrobnosti lze zjistit na `této stránce  <https://readthedocs.org/projects/cojeapi/builds/>`_, která je ovšem přístupná jen administrátorům.
