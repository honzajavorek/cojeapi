Je dost možné, že curl je již přímo ve vašem systému (většina Linuxů, macOS, Windows 10) a není potřeba nic instalovat. Necháme program vypsat svou verzi, čímž ověříme, jestli funguje:

.. literalinclude:: ../code/curl_version.txt
    :language: text

Vypíše-li se verze programu curl, jak je na příkladu výše, máme hotovo. Program curl je v systému a je funkční. Můžeme instalaci přeskočit. Pokud se ale místo verze vypíše něco v tom smyslu, že příkaz ani program curl neexistuje, pak je potřeba curl doinstalovat.

.. tabs::

    .. group-tab:: Linux

        Instalujeme standardní cestou přes správce balíčků. V distribucích Debian nebo Ubuntu takto:

        .. code-block:: text

            $ sudo apt-get install curl

        V distribuci Fedora takto:

        .. code-block:: text

            $ sudo dnf install curl

        Nakonec necháme program vypsat svou verzi, čímž ověříme, jestli funguje:

        .. code-block:: text

            $ curl --version

    .. group-tab:: Windows < 10

        Pokud máme *Git for Windows* nebo *Cygwin*, je velká šance, že curl už máme, jen jej musíme spouštět ze speciálního terminálu poskytovaného těmito nástroji. Otevřeme tento speciální terminál a necháme program vypsat verzi:

        .. code-block:: text

            $ curl --version

        Vypíše-li se verze programu curl, máme hotovo a můžeme přeskočit rovnou na :ref:`curl-examples`. Pokud se ale místo verze vypíše něco v tom smyslu, že příkaz ani program curl neexistuje, pak je potřeba curl doinstalovat. Máme-li `Chocolatey <https://chocolatey.org/>`__, mělo by stačit v příkazové řádce spustit následující:

        .. code-block:: text

            $ choco install curl

        Poté necháme curl vypsat svou verzi:

        .. code-block:: text

            $ curl --version

        Vypíše-li se verze programu curl, máme hotovo a můžeme přeskočit rovnou na :ref:`curl-examples`. Pokud se ale místo verze vypíše něco v tom smyslu, že choco nebo curl neexistují, musíme curl stáhnout a nainstalovat ručně.

        Na `stránkách programu najdeme verzi pro Windows <https://curl.haxx.se/windows/>`__ a podle typu našich Windows (`Jak zjistit, zda máme 32bitové, nebo 64bitové? <https://www.wikihow.cz/Jak-zjistit,-zda-m%C3%A1te-32bitov%C3%A9,-nebo-64-bitov%C3%A9-Windows>`__) vybereme odpovídající verzi. Po rozbalení dostaneme spustitelný soubor ``curl.exe``, který přidáme do systémové cesty. Pokud přidávat programy do systémové cesty neumíme, pro účely tohoto návodu postačí, pokud soubor ``curl.exe`` dáme do té složky, ze které jej budeme chtít spouštět. Nakonec necháme program vypsat svou verzi, čímž ověříme, jestli funguje:

        .. code-block:: text

            $ curl --version
