Nejdříve ověříme, zda náhodou už nemáme nainstalovaný program now, kterým se služba Now ovládá. V příkazové řádce necháme program vypsat svou verzi, čímž ověříme, jestli funguje:

.. code-block:: text

    $ now --version
    > UPDATE AVAILABLE The latest version of Now CLI is X.Y.Z
    > Read more about how to update here: https://zeit.co/update-cli
    > Changelog: https://github.com/zeit/now-cli/releases/tag/X.Y.Z
    X.Y.Z

Vypíše-li se verze programu now, jak je na příkladu výše, máme hotovo. Program now je funkční a nemusíme jej už instalovat. Přeskočíme instalaci.

Pokud se místo verze vypíše něco v tom smyslu, že příkaz ani program now neexistuje, pak je potřeba jej doinstalovat. Půjdeme na https://zeit.co/download a nainstalujeme si now pro náš systém. Po instalaci opět v příkazové řádce necháme program now vypsat svou verzi, abychom ověřili, zda funguje:

.. code-block:: text

    $ now --version
