Nejdříve ověříme, zda náhodou už nemáme nainstalovaný program now, kterým se služba Now ovládá. V příkazové řádce necháme program vypsat svou verzi, čímž ověříme, jestli funguje:

.. code-block:: text

    $ now --version
    > UPDATE AVAILABLE Run `npm i -g now@latest` to install Now CLI 16.7.3
    > Changelog: https://github.com/zeit/now/releases/tag/now@16.7.3
    16.7.1

Vypíše-li se verze programu now, jak je na příkladu výše, máme hotovo. Na číslu verze nezáleží. Program now je funkční a instalaci můžeme přeskočit.

Pokud se místo verze vypíše něco v tom smyslu, že příkaz ani program now neexistuje, pak je potřeba jej doinstalovat.

.. tabs::

    .. group-tab:: Linux

        Začneme instalací Node.js.

        .. note::
            .. include:: _nodejs_note.rst

        Instalujeme standardní cestou přes správce balíčků. V distribucích Debian nebo Ubuntu takto:

        .. code-block:: text

            $ sudo apt-get install nodejs

        V distribuci Fedora takto:

        .. code-block:: text

            $ sudo dnf install nodejs

        Balík Node.js nainstaluje i program s názvem `npm <https://www.npmjs.com/get-npm>`__ (něco jako `pip <https://cs.wikipedia.org/wiki/Pip_(Python)>`__ pro JavaScript), kterým už můžeme nainstalovat `now <https://zeit.co/download>`__:

        .. code-block:: text

            $ npm install now@latest --global

        Nakonec necháme program now vypsat svou verzi, čímž ověříme, jestli funguje:

        .. code-block:: text

            $ now --version

    .. group-tab:: Windows

        Začneme instalací Node.js.

        .. note::
            .. include:: _nodejs_note.rst

        Na `stránkách Node.js stáhneme „Windows Installer“ <https://nodejs.org/>`__ a spustíme. Nainstaluje se i program s názvem `npm <https://www.npmjs.com/get-npm>`__ (něco jako `pip <https://cs.wikipedia.org/wiki/Pip_(Python)>`__ pro JavaScript), kterým už můžeme nainstalovat `now <https://zeit.co/download>`__:

        .. code-block:: text

            $ npm install now@latest --global

        Nakonec necháme program now vypsat svou verzi, čímž ověříme, jestli funguje:

        .. code-block:: text

            $ now --version

    .. group-tab:: macOS (brew)

        Pokud používáme `Homebrew <https://brew.sh/>`__ k instalaci programů, budeme mít práci o něco snazší. Začneme instalací Node.js.

        .. note::
            .. include:: _nodejs_note.rst

        Instalujeme standardní cestou:

        .. code-block:: text

            $ brew install node

        Balík Node.js nainstaluje i program s názvem `npm <https://www.npmjs.com/get-npm>`__ (něco jako `pip <https://cs.wikipedia.org/wiki/Pip_(Python)>`__ pro JavaScript), kterým už můžeme nainstalovat `now <https://zeit.co/download>`__:

        .. code-block:: text

            $ npm install now@latest --global

        Nakonec necháme program now vypsat svou verzi, čímž ověříme, jestli funguje:

        .. code-block:: text

            $ now --version

    .. group-tab:: macOS

        Začneme instalací Node.js.

        .. note::
            .. include:: _nodejs_note.rst

        Na `stránkách Node.js stáhneme „macOS Installer“ <https://nodejs.org/>`__ a spustíme. Nainstaluje se i program s názvem `npm <https://www.npmjs.com/get-npm>`__ (něco jako `pip <https://cs.wikipedia.org/wiki/Pip_(Python)>`__ pro JavaScript), kterým už můžeme nainstalovat `now <https://zeit.co/download>`__:

        .. code-block:: text

            $ npm install now@latest --global

        Nakonec necháme program now vypsat svou verzi, čímž ověříme, jestli funguje:

        .. code-block:: text

            $ now --version
