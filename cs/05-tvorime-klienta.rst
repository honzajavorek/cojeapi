.. _creating-client:

Tvoříme klienta
===============

Doteď jsme používali obecného klienta v podobě prohlížeče nebo programu curl. Obecného klienta musí ovládat člověk. To je přesně to, co potřebujeme, když si chceme nějaké API vyzkoušet, ale celý smysl API je v tom, aby je programy mohly využívat automaticky.

.. warning::
    Na obsahu této části se stále pracuje.

Základ aplikace
---------------

Pokud chceme naprogramovat klienta pro konkrétní úkol, můžeme ve většině jazyků použít nějakou buďto vestavěnou, nebo doinstalovanou knihovnu. V případě jazyka Python použijeme `Requests <https://2.python-requests.org/>`__.

Vytvoříme si pro náš projekt nový adresář ``cojeapi-client`` a v něm `virtuální prostředí <https://naucse.python.cz/course/pyladies/beginners/venv-setup/>`__, které si aktivujeme. Poté nainstalujeme Requests:

.. code-block:: shell

    (venv)$ pip install requests

Pokud jste prošli :ref:`kapitolou o tvorbě API serveru <creating-server>`, ujistěte se, že pro klienta si vytváříte nový projekt - novou složku, nové virtuální prostředí, atd. Vytváříme novou, na serveru zcela nezávislou a samostatnou aplikaci.

Nyní můžeme začít s tvorbou klienta. Jenže specializovaný klient potřebuje nějaké API, na které by se mohl specializovat. K tomu se nám náramně hodí API z předešlé kapitoly. V adresáři ``cojeapi-client`` si vytvoříme nový soubor s názvem ``client.py`` a použijeme v něm Requests pro jednoduchý požadavek na server. Funkce `requests.get <https://2.python-requests.org/en/master/api/#requests.get>`__ nám umožní poslat požadavek metodou :method:`get`. Naše je veřejně dostupné na adrese https://cojeapi.honzajavorek.now.sh, takže ji použijeme jako cíl požadavku. Následně vypíšeme detaily odpovědi, kterou dostaneme:

.. literalinclude:: ../code/client/01_base/client.py
    :language: python

Napsali jsme program, který je ekvivalentem následujícího příkazu:

.. code-block:: text

    $ curl "https://cojeapi.honzajavorek.now.sh/"

Zkusme jej spustit, zatímco nám ve vedlejším okně jede naše API:

.. literalinclude:: ../code/client/01_base/test.txt
    :language: text

A je to, udělali jsme svůj první požadavek na server! Vidíme, že se nám povedlo vypsat status kód odpovědi, hlavičky, i tělo. Hlavičky nám Requests rovnou poskytují jako Python `slovník <https://naucse.python.cz/course/pyladies/sessions/dict/>`__. Tělo odpovědi ale máme zatím jako řetězec.

Čteme JSON
----------

Pokud bychom chtěli číst tělo zprávy, narazíme na fakt, že jej máme jako řetězec:

.. literalinclude:: ../code/client/02_json_error/client.py
    :language: python
    :emphasize-lines: 7

.. literalinclude:: ../code/client/02_json_error/test.txt
    :language: text
    :emphasize-lines: 4-7

Tělo je **text ve formátu JSON** (což nám sděluje i hlavička :header:`Content-Type`). Nešlo by jej nějak dostat jako slovník? Šlo - přesně na toto mají Requests metodu `.json() <https://2.python-requests.org/en/master/api/#requests.Response.json>`__:

.. literalinclude:: ../code/client/03_json/client.py
    :language: python
    :emphasize-lines: 7

Nyní máme z textu ve formátu JSON obyčejný Python slovník:

.. literalinclude:: ../code/client/03_json/test.txt
    :language: text
    :emphasize-lines: 4

Zpracováváme odpověď
--------------------

Program, který dělá totéž co curl, není popravdě moc užitečný program. Pojďme zkusit využít naše API k napsání programu, jenž z něj zjistí seznam filmů a vypíše je.

.. tabs::

    .. tab:: Cvičení

        Přepište program tak, aby posílal požadavek na https://cojeapi.honzajavorek.now.sh/movies, přečetl odpověď, prošel všechny filmy získané z těla odpovědi a pomocí ``print()`` vypsal název každého z nich.

    .. tab:: Řešení

        .. literalinclude:: ../code/client/04_movies/client.py
            :language: python

Pokud program spustíme, měl by vypsat všechny filmy z dotazovaného API:

.. literalinclude:: ../code/client/04_movies/test.txt
    :language: text

.. tabs::

    .. tab:: Cvičení

        Jestliže procházíte tento návod v rámci workshopu, například `PyWorking <https://pyworking.cz/>`__, použijte ve vašem programu místo https://cojeapi.honzajavorek.now.sh adresu API někoho jiného z účastníků. Pokud tam má i jiné filmy než byly v návodu, měl by je program vypsat.

Zjišťujeme nejnovější film
--------------------------

Co kdybychom chtěli ke každému filmu vypsat i rok, kdy byl uveden? Rok není v seznamu filmů k dispozici, nachází se na detailu každého filmu. Budeme tedy muset udělat jeden  požadavek na seznam filmů a poté ještě požadavek na každý film ze seznamu, abychom zjistili rok.

.. literalinclude:: ../code/client/05_year/client.py
    :language: python

Vidíme, že pro každý film děláme další požadavek na API a teprve z jeho výsledku vypisujeme jméno a rok. Pokud program spustíte, bude trvat podstatně déle, než skončí.

.. literalinclude:: ../code/client/05_year/test.txt
    :language: text

To, že musíme posílat požadavek na každý film zvlášť je buď důsledkem toho, že se snažíme z API zjistit kombinaci informací, která není úplně obvyklá, nebo důsledkem toho, že někdo API špatně navrhl. Narazili jsme přesně na tu situaci, která byla popsána v sekci :ref:`apidesign` při tvorbě serveru.

Chyby
-----

.. warning::
    Tato kapitola není ještě připravena.

Zapisujeme
----------

.. warning::
    Tato kapitola není ještě připravena.

Mažeme
------

.. warning::
    Tato kapitola není ještě připravena.

Kódování parametrů
------------------

.. warning::
    Tato kapitola není ještě připravena.

.. todo::
    co dáváme do parametrů se musí prohnat nějakym urlencoding
    příklady s nějakým (reverse) geocoding api (google, seznam?)

Zabezpečení
-----------

.. warning::
    Tato kapitola není ještě připravena.

.. todo::
    mechanismus http/https
    basic auth
    oauth
    většinou nějaký token (vysvětlit token), který se narve do hlavičky
    auth token - něco vygenerováno jen pro nás, co je tajné a neměli bychom to nikomu dávat a ukazovat

    příklad s GitHubem, vygenerujeme token, dáme do ENV, nasosáme v programu a můžeme použít

Pracujeme s veřejnými API
-------------------------

OMDb
^^^^

GitHub
^^^^^^

Specializované knihovny (SDK)
-----------------------------

.. warning::
    Tato kapitola není ještě připravena.

.. todo::
    vysvětlit specializovaného klienta
    příklady

.. todo::
    připomenout, že než jdeme psát klienta na zelené louce, měli bychom ověřit, že už není nějaká hotová SDK knihovna (příklady z pypi)

    základní příklady s requests, GET, POST
    https://github.com/honzajavorek/cojeapi/issues/2
