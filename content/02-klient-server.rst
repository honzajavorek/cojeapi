Klient a server
===============

.. todo::
    vysvetlit architekturu
    priklady: browser-server, curl-server
    zkusit: browser-banka, curl-banka
    https://github.com/honzajavorek/cojeapi/issues/2


Klient v terminálu: curl
------------------------

Prohlížeč je nejznámějším klientem pro běžného uživatele. Program `curl <https://curl.haxx.se/>`_ je zase nejznámějším klientem, který můžete spouštět v terminálu. Je tak používaný a významný, že za něj jeho autor `dostal v roce 2017 ocenění z rukou švédského krále <https://daniel.haxx.se/blog/2017/10/20/my-night-at-the-museum/>`_.

Jelikož se bude *curl* vyskytovat v následujících příkladech, je potřeba, abyste jej měli nainstalovaný.

.. tabs::

    .. group-tab:: Linux

        Je dost možné, že *curl* máte již přímo v systému a není potřeba nic instalovat. Zkuste nechat program vypsat svou verzi, čímž ověříte, jestli je k dispozici:

        .. code-block:: shell

            $ curl --version
            curl x.x.x (...) ...
            Protocols: ...
            Features: ...

        Pokud se místo verze vypíše něco v tom smyslu, že příkaz ani program toho jména neexistuje, nainstalujte *curl* standardní cestou přes svého správce balíčků. V distribucích Debian nebo Ubuntu takto:

        .. code-block:: shell

            $ sudo apt-get install curl

        V distribuci Fedora takto:

        .. code-block:: shell

            $ sudo dnf install curl

    .. group-tab:: macOS

        Program *curl* je k dispozici přímo v systému, není potřeba nic instalovat.

    .. group-tab:: Windows

        Pokud používáte *Git for Windows* nebo *Cygwin*, je velká šance, že program *curl* už máte, jen jej musíte spouštět ze speciálního terminálu poskytovaného těmito nástroji.

        Pokud používáte `Chocolatey <https://chocolatey.org/>`_, mělo by stačit v terminálu spustit následující:

        .. code-block:: shell

            $ choco install curl

        Jinak musíte *curl* stáhnout a nainstalovat ručně. `Zde <https://curl.haxx.se/dlwiz/?type=bin&os=Win64&flav=-&ver=*&cpu=x86_64>`_ vyberte tu verzi, která má v popisku *SSL enabled* a *file is packaged using zip*. Klikněte na :kbd:`Download`. Rozbalte stáhnutý zip, najděte ``curl.exe`` a přidejte jej do systémové cesty.

        Nakonec nechte program vypsat svou verzi, čímž ověříte, jestli funguje:

        .. code-block:: shell

            $ curl --version
            curl x.x.x (...) ...
            Protocols: ...
            Features: ...

        .. note::

            Tento instalační návod je pro úplné začátečníky příliš stručný, ale snad si většina lidí nějak poradí. Můžete mi také :ref:`pomoci návod rozšířit <contributing>`.
