.. _creating-server:

Tvoříme server
==============

Konec teorie, pojďme si vyzkoušet nabyté znalosti v praxi. Začneme tím, že zkusíme vyrobit API. Použijeme k tomu jazyk `Python <https://python.cz/>`__ verze 3 a framework `Falcon <https://falcon.readthedocs.io/>`__, který se pro API skvěle hodí.

.. note::

    Pokud vám Python není cizí, možná jste už slyšeli o známějších frameworcích `Flask <http://flask.pocoo.org/>`__ nebo `Django <https://www.djangoproject.com/>`__. V těch by šlo API vytvořit také, ale jsou primárně určeny na tvorbu webových stránek, a to by nám nyní spíš překáželo. Viz také kapitola :ref:`frameworky`.

Vytvoříme si pro náš projekt nový adresář ``cojeapi-server`` a v něm `virtuální prostředí <https://naucse.python.cz/course/pyladies/beginners/venv-setup/>`__, které si aktivujeme. Poté nainstalujeme Falcon:

.. code-block:: shell

    (venv)$ pip install falcon

Navrhujeme API
--------------

Nyní budeme tvořit API, které bude strojově čitelnou formou zpřístupňovat základní informace o nás samotných. Pokud jsme aktivní na sociálních sítích, tak takové API nejspíš už `existuje <https://developers.facebook.com/docs/graph-api/>`__, ale my si uděláme svoje - roztomilejší, jednodušší, méně `děsivé <https://en.wikipedia.org/wiki/Facebook#Criticisms_and_controversies>`__.

Než začneme cokoliv programovat, rozmyslíme si, jak by naše API mělo vypadat. Řekněme, že kdybychom na něj poslali ``GET`` požadavek pomocí programu ``curl``, chceme, aby naše API odpovědělo zhruba následovně:

.. literalinclude:: ../code/base_example.txt
    :language: text

Jinými slovy, pokud metodou ``GET`` přijde :ref:`dotaz <http-request>` na adresu ``/``, pošleme zpátky :ref:`odpověď <http-response>` se status kódem ``200 OK`` a tělem v textovém :ref:`formátu <formaty>`. V těle zprávy budou tři řádky, v nichž pošleme své jméno, příjmení, a velikost ponožek.

.. note::

    Příklad výše zatím nezkoušejte, je to pouze návrh toho, jak by naše API mělo fungovat.

Programujeme aplikaci
---------------------

Začneme tím, že vytvoříme soubor ``index.py`` s následujícím obsahem:

.. literalinclude:: ../code/base.py
    :language: python

V kódu můžeme vidět `třídu <https://naucse.python.cz/course/pyladies/beginners/class/>`__ ``PersonalDetailsResource`` s jednou metodou. Třídu jsme si pojmenovali sami podle toho, že je zodpovědná za naše osobní údaje, akorát jsme podle konvence připojili slovo *resource*.

Název metody ``on_get()`` naznačuje, že se stará o HTTP metodu ``GET``. Bere parametry ``request`` reprezentující právě přicházející :ref:`dotaz <http-request>`, a ``response``, tedy :ref:`odpověď <http-response>`, kterou se chystáme odeslat zpět. Uvnitř metody nastavujeme status kód odpovědi na ``200 OK``, hlavičku ``Content-Type`` na formát těla, a poté tělo na tři řádky řetězců s osobními údaji.

Nakonec do proměnné ``app`` ukládáme naši Falcon aplikaci a na dalším řádku jí říkáme, že pokud někdo bude posílat :ref:`dotazy <http-request>` na adresu ``/``, bude je mít na starost naše třída.

Spouštíme aplikaci na našem počítači
------------------------------------

Když zkusíme program spustit, zjistíme, že nic nedělá:

.. code-block:: shell

    (venv)$ python index.py

.. note::

    Jestliže vidíte nějakou chybu, třeba ``SyntaxError`` nebo ``NameError``, tak ji opravte. Abyste mohli pokračovat, program se má spustit, nemá nic vypsat, a má se bez chyb hned ukončit.

Falcon se totiž jen tak sám od sebe spustit neumí. Potřebujeme něco, co načte naši aplikaci a bude se chovat jako :ref:`server <server>`. Takových nástrojů je naštěstí hned několik. Pro účely tohoto návodu si vybereme `Waitress <https://docs.pylonsproject.org/projects/waitress/>`__, protože na rozdíl od jiných funguje i pod Windows. Instalujeme standardně:

.. code-block:: shell

    (venv)$ pip install waitress

Nyní můžeme spustit naše API. Stačí spustit ``waitress-serve`` s nápovědou, kde má hledat aplikaci. Ta je v souboru ``index.py`` v proměnné ``app``, takže nápověda pro Waitress bude ``index:app``.

.. code-block:: shell

    (venv)$ waitress-serve index:app
    Serving on http://0.0.0.0:8080

Waitress nám píše, že na adrese ``http://0.0.0.0:8080`` teď najdeme spuštěné naše API. Bude tam čekat na :ref:`dotazy <http-request>` tak dlouho, dokud v programu nenastane chyba (potom "spadne"), nebo dokud jej v terminálu neukončíme pomocí :kbd:`Ctrl+C`.

Když nyní v prohlížeči půjdeme na adresu ``http://0.0.0.0:8080``, měli bychom vidět očekávanou :ref:`odpověď <http-response>`:

.. image:: ../_static/images/me-api-text.png
    :alt: Odpověď v textovém formátu
    :align: center

Co když zkusíme curl? Protože nám spuštěné API blokuje terminál, spustíme si další terminál v novém okně. Z něj nyní můžeme spustit curl:

.. image:: ../_static/images/me-api-curl.png
    :alt: Spouštění curl v dalším terminálu
    :align: center

Vidíme, že API se chová tak, jak jsme původně chtěli. Odpověď má status kód ``200 OK``, formát těla odpovědi je v hlavičce ``Content-Type`` nastaven na obyčejný text, a v těle zprávy vidíme jméno, příjmení, i velikost ponožek. Kromě toho Falcon s Waitress přidali i nějaké další hlavičky.

.. literalinclude:: ../code/base_test.txt
    :language: text

Server nyní můžeme v terminálu ukončit pomocí :kbd:`Ctrl+C` a budeme API rozšiřovat o další funkce.

Uchováváme data jako slovník
----------------------------

Naše data nyní vypadají následovně:

.. literalinclude:: ../code/base.py
    :language: python
    :emphasize-lines: 9-13

Co si budeme povídat, takto data běžně nevypadají. Většinou jsou někde v databázi, v souboru, apod. a musíme zavolat nějakou funkci, abychom je dostali. Zpravidla je také dostaneme jako seznam nebo slovník, ne jako připravený řetězec. Pojďme si tedy tuto situaci nasimulovat. Nejdříve si data vytáhneme do funkce, která je bude vracet.

.. literalinclude:: ../code/base_data_func.py
    :language: python
    :emphasize-lines: 4-9, 17

Nyní z dat uděláme slovník, který až při sestavování odpovědi složíme do textu. Tím rozdělíme uložení dat a jejich prezentaci navenek. Jak už bylo zmíněno, data většinou přicházejí např. z databáze právě jako slovník, takže toto rozdělení je v praxi potřebné a velmi časté.

.. literalinclude:: ../code/base_data_func_dict.py
    :language: python
    :emphasize-lines: 4-9, 18-22

Takovéto API nám bude fungovat stále stejně, protože ze slovníku opět složí řetězec, který jsme původně posílali v odpovědi. Data jsou nyní ale nezávislá na tom, jak je budeme prezentovat uživateli. Prakticky si tuto výhodu ukážeme v následujících odstavcích.

Posíláme JSON
-------------

Jak jsme si :ref:`vysvětlovali <struktura>`, obyčejný text není nejlepší způsob, jak něco udělat strojově čitelné. Zkusíme tedy poslat naše data jako :ref:`JSON`.

.. literalinclude:: ../code/json_response.py
    :language: python
    :emphasize-lines: 1, 17-18

Jak vidíme, kód se nám s JSONem zjednodušil. Navíc díky tomu, že máme data hezky oddělená od samotného API, nemuseli jsme je nijak měnit. Stačilo změnit způsob, jakým se budou posílat v odpovědi. Když aplikaci spustíme, můžeme opět použít curl nebo prohlížeč a ověřit výsledek.

.. literalinclude:: ../code/json_response_test.txt
    :language: text

.. image:: ../_static/images/me-api-json.png
    :alt: api.py API, odpověď ve formátu JSON
    :align: center

A je to, máme své první JSON API! Už teď jsme se dostali dál, než kam se se svým API dostala :ref:`ČNB <cnb>`.

.. note::
    Pokud máte v datech diakritiku, bude zakódována. Kdybych se jmenoval Řehoř, vypadal by můj JSON takto: ``{"name": "\u0158eho\u0159", ...}`` Jestliže se chceme takového kódování zbavit, můžeme při tvorbě JSONu nastavit ``ensure_ascii`` na ``False``:

    .. code-block:: python

        response.body = json.dumps(get_personal_details(), ensure_ascii=False)

Čteme URL parametry
-------------------

.. warning::

    Tato kapitola je právě přepisována z Flasku na Falcon. Přijďte raději později, po krátkou chvíli návod nebude dávat smysl.

Naše API má zatím pouze jednu adresu, na kterou se může klient dotazovat. V hantýrce programátorů webů by se řeklo, že má jednu "routu" (z anglického *route*). V hantýrce programátorů API by se zase řeklo, že má jeden *endpoint*. No a API s jedním endpointem není nic moc. Přidáme tedy druhý, který bude světu sdělovat seznam našich oblíbených filmů.

.. code-block:: python
    :emphasize-lines: 15-25

    import random
    from flask import Flask, jsonify

    app = Flask(__name__)

    def get_about_me():
        return {
            ...
        }

    @app.route("/")
    def about_me():
        return jsonify(get_about_me())

    def get_movies():
        return [
            {"name": "The Last Boy Scout", "year": 1991},
            {"name": "Mies vailla menneisyyttä", "year": 2002},
            {"name": "Sharknado", "year": 2013},
            {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
        ]

    @app.route("/movies")
    def movies():
        return jsonify(get_movies())

Když aplikaci spustíme, bude na adrese ``/movies`` vracet informace o našich oblíbených filmech.

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/movies'
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 182
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Fri, 09 Nov 2018 21:34:22 GMT

    [{"name":"The Last Boy Scout","year":1991},{"name":"Mies vailla menneisyytt\u00e4","year":2002},{"name":"Sharknado","year":2013},{"name":"Mega Shark vs. Giant Octopus","year":2009}]

Co kdybychom ale měli opravdu hodně oblíbených filmů? Možná bychom chtěli mít možnost výsledky filtrovat. K tomu se nám mohou hodit :ref:`URL parametry <http-request>`. Chtěli bychom třeba, aby klient mohl udělat dotaz na ``/movies?name=shark`` a tím by našel jen ty filmy, které mají v názvu řetězec ``shark``.

Nejdříve si připravme hledání. V následujícím příkladu je použit `cyklus <https://naucse.python.cz/course/pyladies/sessions/loops/>`__, ale kdo zná funkci `filter <https://docs.python.org/3/library/functions.html#filter>`__ nebo `list comprehentions <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`__, může si klidně poradit jinak.

.. code-block:: python

    def get_movies(name=None):
        movies = [
            {"name": "The Last Boy Scout", "year": 1991},
            {"name": "Mies vailla menneisyyttä", "year": 2002},
            {"name": "Sharknado", "year": 2013},
            {"name": "Mega Shark vs. Giant Octopus", "year": 2009},
        ]
        if name is not None:
            filtered_movies = []
            for movie in movies:
                if name in movie["name"].lower():
                    filtered_movies.append(movie)
            return filtered_movies
        else:
            return movies

Nyní potřebujeme přečíst z dotazu parametr a použít jej. K tomu nám Flask přichystal `request <http://flask.pocoo.org/docs/1.0/api/#flask.request>`__.

.. code-block:: python

    from flask import Flask, jsonify, request

    ...

    @app.route("/movies")
    def movies():
        return jsonify(get_movies(name=request.args.get("name")))

Pokud se na náš nový endpoint dotážeme bez parametrů, měl by fungovat stejně jako předtím. Jestliže ale přidáme ``?name=`` do adresy, měla by hodnota parametru filtrovat filmy.

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/movies?name=shark'
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 87
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Fri, 09 Nov 2018 21:54:39 GMT

    [{"name":"Sharknado","year":2013},{"name":"Mega Shark vs. Giant Octopus","year":2009}]

Vidíme, že tentokrát jsme dostali v těle odpovědi jen dva filmy místo čtyř.

Umožňujeme zápis
----------------

.. warning::

    Tato kapitola je právě přepisována z Flasku na Falcon. Přijďte raději později, po krátkou chvíli návod nebude dávat smysl.

Nyní máme API, které je pouze ke čtení. Zkusme si naprogramovat endpointy, jež by umožňovaly i zápis. Ti starší z nás možná ještě pamatují `vystřihovací panenky <https://www.fler.cz/zbozi/vystrihovaci-panenka-marinka-2866816>`__, ti mladší možná narazili na `My Octocat <https://myoctocat.com/build-your-octocat/>`__ - tak teď si vytvoříme něco podobného. Začneme tím, že přidáme ``/clothes``, kde bude API vypisovat, co máme zrovna na sobě, a ``/clothes/<název svršku>`` s detaily pro každý svršek.

.. code-block:: python

    clothes_state = {
        "shoes": "brown",
        "jeans": "blue",
        "t-shirt": "white",
        "socks": "red",
        "underwear": "black",
    }

    @app.route("/clothes")
    def clothes():
        return jsonify(list(clothes_state.keys()))

    @app.route("/clothes/<name>")
    def garment(name):
        color = clothes_state[name]
        return jsonify({"name": name, "color": color})

Slovník s oblečením tentokrát nezískáváme funkcí, ale záměrně si jej ukládáme jako globální proměnnou. Je to proto, že budeme potřebovat globální stav, který půjde postupně měnit. To by s funkcí nešlo, vrátila by nám vždy nový, nezměněný slovník.

Magické ``"/clothes/<name>"`` je instrukce pro Flask, která mu říká, že na místě, kde je v adrese ``<name>`` má očekávat jakýkoliv řetězec a ten má potom funkci předat jako argument ``name``. Pokud tedy bude klient dotazovat ``/clothes/socks``, Flask zavolá naši funkci s argumentem ``socks``.

Ověříme, zda nám vše funguje:

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/clothes'
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 48
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Fri, 09 Nov 2018 22:06:22 GMT

    ["shoes","jeans","t-shirt","socks","underwear"]

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/clothes/socks'
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 31
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Fri, 09 Nov 2018 23:17:21 GMT

    {"color":"red","name":"socks"}

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/clothes/jeans'
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 32
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Fri, 09 Nov 2018 23:17:43 GMT

    {"color":"blue","name":"jeans"}

Návrh API
^^^^^^^^^

Vidíme, že z jedněch dat jsme vytvořili dva endpointy, které se navzájem doplňují a odkazují na sebe. To je běžná praxe - způsob, jakým chceme aby API fungovalo, nemusí nutně kopírovat interní strukturu našich dat. Ideálně by návrh API měl co nejvíce odpovídat tomu, jak jej bude používat klient. Náš návrh je dobrý, pokud bude klientům většinou stačit jen jmenný seznam oblečení a nebude jim vadit, pokud se na barvu (a případně další detaily) doptají zvlášť, podle potřeby. Každý dotaz totiž něco stojí. Pokud by byla barva důležitá, chtěli bychom ji mít už na ``/clothes``, aby jen kvůli ní nemuseli všichni klienti našeho API dělat ještě zvlášť dotaz pro každý svršek.

Nenalezeno
^^^^^^^^^^

Co když se zeptáme na neexistující svršek? Dostaneme status kód ``500 Internal Server Error``! Co to znamená? Je to chyba serveru (začíná pětkou), a to znamená, že chyba je na naší straně, jelikož my jsme tvůrci tohoto API serveru.

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/clothes/hat'
    HTTP/1.0 500 INTERNAL SERVER ERROR
    ...

Když se podíváme, co vypsal Flask, uvidíme detaily chyby:

.. code-block:: text

    [2018-11-10 00:28:51,508] ERROR in app: Exception on /clothes/hat [GET]
    Traceback (most recent call last):
    File ...
    KeyError: 'hat'

Sice nemůžeme za to, že se uživatel ptá na klobouk, tedy neexistující svršek, ale jsme zodpovědní za to, že naše API vybouchlo na výjimce. Musíme ji hezky ošetřit a uživateli dát najevo, že chyba je na jeho straně a o jakou že se jedná přesně chybu. K tomu nám poslouží `abort <http://flask.pocoo.org/docs/1.0/api/#flask.abort>`__ a status kód ``404 Not Found``. Ten něžně svaluje vinu na klienta (začíná čtyřkou) a sděluje mu, že na adrese ``/clothes/hat`` nic není, takže by se měl asi dotazovat jinam.

.. code-block:: python
    :emphasize-lines: 1, 7, 10-11

    from flask import Flask, jsonify, request, abort

    ...

    @app.route("/clothes/<name>")
    def garment(name):
        try:
            color = clothes_state[name]
            return jsonify({"name": name, "color": color})
        except KeyError:
            abort(404)

Nyní by měla odpověď už nést správný kód a naše Flask aplikace by neměla ledabyle spadnout na výjimce:

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/clothes/hat'
    HTTP/1.0 404 NOT FOUND
    ...

Přidáváme
^^^^^^^^^

Nyní zkusíme umožnit přidávat oblečení. Na zimu se to může hodit. Klient využívající naše API by mohl mít možnost poslat nám nové svršky v těle HTTP dotazu. Ty by se potom přidaly do seznamu.

Zatím všechny dotazy, které jsme dělali, byly metodou ``GET``, která je pro čtení, a kterou Flask automaticky předpokládá. Pokud chceme zapisovat, můžeme použít metodu ``POST``, ale to už musíme Flasku jasně říct:

.. code-block:: python

    @app.route("/clothes", methods=["GET", "POST"])
    def clothes():
        return jsonify(clothes_state)

Teď bychom rádi přečetli tělo dotazu, pokud jde o metodu ``POST``, našli v něm nové oblečení a přidali jej do našeho slovníku. Opět nám dobře poslouží `request <http://flask.pocoo.org/docs/1.0/api/#flask.request>`__.

.. code-block:: python
    :emphasize-lines: 3-5

    @app.route("/clothes", methods=["GET", "POST"])
    def clothes():
        if request.method == "POST":
            new_garment = request.get_json()
            clothes_state[new_garment["name"]] = new_garment["color"]
        return jsonify(list(clothes_state.keys()))

Teď jde do tuhého - abychom vyzkoušeli, zda přidávání funguje, musíme se ponořit mezi spoustu nových argumentů pro curl: ``-d`` nám umožní poslat data v těle dotazu, ``-H`` přidá hlavičku, ``-X`` nastaví metodu, kterou chceme dotaz poslat (doteď jsme posílali ``GET``, jenž je výchozí). Celé to bude vypadat takto:

.. code-block:: text

    $ curl -i -d '{"name":"hat", "color":"red"}' -H "Content-Type: application/json" -X POST 'http://127.0.0.1:5000/clothes'
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 54
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Sat, 10 Nov 2018 00:03:35 GMT

    ["shoes","jeans","t-shirt","socks","underwear","hat"]

A je to, přidali jsme klobouk! Hned můžeme ověřit, jestli se pro něj automaticky vytvořila i adresa s detailem:

.. code-block:: text

    $ curl -i 'http://127.0.0.1:5000/clothes/hat'
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 29
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Sat, 10 Nov 2018 00:06:16 GMT

    {"color":"red","name":"hat"}

Funguje to. Jen si představte, co by šlo s takovýmto API udělat! Někdo by mohl napsat klienta, který bude automaticky objednávat oblečení na `Zootu <https://www.zoot.cz/>`__ a rovnou jej na nás přes ``POST /clothes`` házet.

.. note::
    Měli bychom ošetřit, zda to, co klient pošle, má správnou strukturu, zda neposílá čísla místo řetězců, apod. Např. kdyby poslal ``{"nejaky": "nesmysl"}``, naše API opět spadne na výjimce. V těchto materiálech se ošetřováním dat zabývat nebudeme, ale je dobré vědět, že se tomu obecně říká validace a že pro JSON to řeší `JSON Schema <https://json-schema.org/understanding-json-schema/>`__.

Přidáváme po správňácku
^^^^^^^^^^^^^^^^^^^^^^^

Naše přidávání ovšem není ještě úplně ideální. Sice funguje, ale nechová se správně podle HTTP specifikace a běžných zvyklostí. Když se něco přidává, měli bychom vrátit status kód ``201 Created``, což je v tomto případě konkrétnější, než ``200 OK``. Také bychom mohli vrátit v odpovědi hlavičku ``Location`` s adresou, na které může klient najít detail právě vytvořeného svršku. Využijeme skutečnost, že `jsonify <http://flask.pocoo.org/docs/1.0/api/#flask.json.jsonify>`__ vrací `Response <http://flask.pocoo.org/docs/1.0/api/#response-objects>`__ objekt a ten lze před odesláním ještě dle libosti upravovat. Pro vytvoření adresy budeme navíc ještě potřebovat `url_for <http://flask.pocoo.org/docs/1.0/api/#flask.url_for>`__.

.. code-block:: python
    :emphasize-lines: 1, 9-18

    from flask import Flask, jsonify, request, abort, url_for

    ...

    @app.route("/clothes", methods=["GET", "POST"])
    def clothes():
        if request.method == "POST":
            new_garment = request.get_json()
            name, color = new_garment["name"], new_garment["color"]

            clothes_state[name] = color

            response = jsonify(list(clothes_state.keys()))
            response.status_code = 201
            response.headers["Location"] = url_for('garment', name=name)
            return response
        else:
            return jsonify(list(clothes_state.keys()))

Výsledek by měl vypadat následovně:

.. code-block:: text
    :emphasize-lines: 2, 5

    $ curl -i -d '{"name":"jacket", "color":"navy"}' -H "Content-Type: application/json" -X POST 'http://127.0.0.1:5000/clothes'
    HTTP/1.0 201 CREATED
    Content-Type: application/json
    Content-Length: 57
    Location: http://127.0.0.1:5000/clothes/jacket
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Sat, 10 Nov 2018 00:16:57 GMT

    ["shoes","jeans","t-shirt","socks","underwear","jacket"]

Ukládání natrvalo
^^^^^^^^^^^^^^^^^

Možná jste si všimli, že pokaždé, když restartujete Flask aplikaci, vrátí se oblečení do původního stavu. Je to proto, že stav našeho API udržujeme v Pythonu, v globálním slovníku. Ten se ukládá pouze v paměti počítače a když program skončí, odejde slovník do věčných lovišť.

Aby změny přežily restartování programu, museli bychom stav ukládat do souboru nebo do databáze. To je ovšem nad rámec těchto materiálů.

Mažeme
^^^^^^

Pokud bychom chtěli uživatelům našeho API umožnit kusy oblečení i odebírat, můžeme k tomu použít metodu ``DELETE`` na endpointu pro jednotlivé svršky. Ta funguje tak, že pokud ji klient pošle na nějakou adresu, je to instrukce pro API server, že má věc, kterou ta adresa reprezentuje, smazat.

Jenže co vrátit za odpověď? Pokud něco smažeme a ono už to neexistuje, asi to nebudeme chtít vracet v těle odpovědi. Pokud nemáme co do těla odpovědi dát, můžeme v HTTP použít tzv. prázdnou odpověď. Má kód ``204 No Content`` a dává klientovi najevo, že nemá v odpovědi už očekávat žádné tělo. Použijeme opět `Response <http://flask.pocoo.org/docs/1.0/api/#response-objects>`__ objekt.

.. code-block:: python
    :emphasize-lines: 1, 8-11

    from flask import Flask, jsonify, request, abort, Response

    ...

    @app.route("/clothes/<name>", methods=["GET", "DELETE"])
    def garment(name):
        try:
            if request.method == "DELETE":
                del clothes_state[name]
                return Response(status=204)
            else:
                color = clothes_state[name]
                return jsonify({"name": name, "color": color})
        except KeyError:
            abort(404)

Když použijeme curl, abychom smazali například ponožky (opět využijeme ``-x`` pro nastavení metody), dostaneme pouze status kód a hlavičky.

.. code-block:: text

    $ curl -i -X DELETE 'http://127.0.0.1:5000/clothes/socks'
    HTTP/1.0 204 NO CONTENT
    Content-Type: text/html; charset=utf-8
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Sat, 10 Nov 2018 10:01:17 GMT

Pokud bychom chtěli zamezit tomu, aby nám bylo odebráno veškeré oblečení, můžeme doprogramovat jednoduché zabezpečení. Jestliže nechceme něco v API povolit, můžeme to dát druhé straně najevo například pomocí kódu ``403 Forbidden``:

.. code-block:: python
    :emphasize-lines: 9-11

    from flask import Flask, jsonify, request, abort, Response

    ...

    @app.route("/clothes/<name>", methods=["GET", "DELETE"])
    def garment(name):
        try:
            if request.method == "DELETE":
                if name == 'underwear':
                    return Response(status=403)  # nic takového!
                else:
                    del clothes_state[name]
                    return Response(status=204)
            else:
                color = clothes_state[name]
                return jsonify({"name": name, "color": color})
        except KeyError:
            abort(404)

Když zkusíme smazat spodní prádlo, API nám to nyní nedovolí.

.. code-block:: text

    $ curl -i -X DELETE 'http://127.0.0.1:5000/clothes/underwear'
    HTTP/1.0 403 FORBIDDEN
    Content-Type: text/html; charset=utf-8
    Content-Length: 0
    Server: Werkzeug/0.14.1 Python/3.7.1
    Date: Sat, 10 Nov 2018 10:01:23 GMT

Podobným způsobem bylo zabezpečeno API od :ref:`OMDb <omdb-api>`. Dokud jsme neudělali dotaz s API klíčem, nedostali jsme jinou odpověď než chybu:

.. code-block:: text

    $ curl -i 'https://www.omdbapi.com/?t=westworld'
    HTTP/2 401
    ...

    {"Response":"False","Error":"No API key provided."}

Jediným rozdílem je to, že v jejich API byl použit kód ``401 Unauthorized``. Ten se má poslat ve chvíli, kdy má klient šanci oprávnění získat a dotaz provést znovu. V případě OMDb bylo potřeba se zaregistrovat, obdržet API klíč a poslat ho jako parametr. V našem případě oprávnění nijak dostat nelze. Abychom mohli vracet ``401 Unauthorized``, museli bychom doprogramovat nějaký přístup pro ty, s nimiž chceme strávit romantický večer.

.. _nowsh:

Uveřejňujeme API
----------------

.. warning::

    Tato kapitola je právě přepisována, aby co nejlépe odrážela současný stav věcí a plně podporovala now 2.0.

Zatím jsme naši aplikaci spouštěli pouze na svém počítači a neměl k ní přístup nikdo jiný, než my sami. Nebylo by lepší, kdyby naše API bylo veřejné a mohli by jej používat naši kamarádi?

Můžeme k tomu využít službu `now.sh <https://zeit.co/now>`__. Ta nám umožní uveřejnit aplikaci tak, aby nebyla jen na našem počítači, ale mohl na ni přistupovat kdokoliv. Nejdříve nainstalujeme program ``now``:

#.  Půjdeme na https://zeit.co/download a nainstalujeme si ``now`` pro náš systém
#.  Otevřeme si příkazovou řádku a zkusíme napsat ``now --version``, abychom ověřili, zda vše funguje, jak má
#.  V témže adresáři, ve kterém máme ``index.py``, vytvoříme nový soubor ``now.json`` s následujícím obsahem:

    .. literalinclude:: ../code/now.json
        :language: json

#.  V témže adresáři, ve kterém máme ``index.py``, vytvoříme nový soubor ``requirements.txt`` s následujícím obsahem:

    .. literalinclude:: ../code/requirements.txt
        :language: text

    Tím říkáme, že aby naše API fungovalo, bude potřeba nejdříve nainstalovat Falcon. Waitress do souboru psát nebudeme, ten potřebujeme jen pro spuštění na našem počítači, `now.sh <https://zeit.co/now>`__ si poradí i bez něj.

#.  Nyní zkusíme na příkazové řádce, v našem adresáři s aplikací, spustit příkaz ``now``
#.  Je pravděpodobné, že ``now`` po nás bude chtít e-mailovou adresu. Zadáme ji a ověříme v naší e-mailové schránce
#.  Když nyní znova spustíme ``now``, nahraje se naše aplikace na internet (bude to nejspíše chvíli trvat)
#.  Po nějaké době bychom měli dostat adresu, na které můžeme naše API najít - něco ve tvaru ``https://cojeapi-server.honzajavorek.now.sh``

Když na tuto adresu půjdeme v prohlížeči, měli bychom vidět HTTP odpověď na endpoint ``/``:

.. image:: ../_static/images/now.png
    :alt: now.sh v prohlížeči
    :align: center

Můžeme se na naše API dotazovat samozřejmě i pomocí curl:

.. code-block:: text

    $ curl -i 'https://cojeapi-server.honzajavorek.now.sh'
    HTTP/2 200
    date: Sat, 10 Nov 2018 11:12:32 GMT
    ...
    content-type: application/json

    {"eyes_color":"brown","eyes_count":2,"hair_color":"brown","hands_count":2,"legs_count":2,"mood":"grumpy","name":"Honza","surname":"Javorek"}

A co je ještě lepší, na rozdíl od všech předchozích případů, nyní může na naše API posílat dotazy i někdo jiný! Pošlete tuto adresu kamarádce/kamarádovi nebo kolegyni/kolegovi, ať zkusí se svým prohlížečem a s curl posílat dotazy na vaše API. Vy zase můžete zkoušet jejich API. Nebojme se experimentovat, třeba přidat oblečení, nebo nějaké smazat.

Pokud budeme chtít udělat v našem API změny a ty opět promítnout veřejně, budeme muset znova spustit příkaz ``now``.

.. _frameworky:

Frameworky pro tvorbu serveru
-----------------------------

V tomto návodu jsme si ukázali, jak vyrobit jednoduché API s pomocí frameworku `Falcon <https://falcon.readthedocs.io/>`__, jenž je pro toto použití vyladěný.

Jelikož jsou webová API založena na podobných principech jako webové stránky, šlo by použít i známější frameworky `Flask <http://flask.pocoo.org/>`__ nebo `Django <https://www.djangoproject.com/>`__. Pokud bychom v nich ale tvořili složitější API, brzy by nám přišlo, že s takovým frameworkem spíše bojujeme, než aby nám pomáhal.

Např. chyby by takový framework standardně posílal jako HTML, přitom by bylo lepší, kdyby byly také naformátovány jako JSON. Museli bychom ručně doplnit kód, který upraví výchozí chování Flasku nebo Djanga a bude chyby posílat tak, jak se v JSON API sluší a patří.

Z tohoto a dalších důvodů je tedy výhodnější buďto pro API využít specializovaný framework, jakým je Falcon, nebo se poohlédnout po doplňcích do Flasku, popřípadě Djanga, které nám tvorbu API usnadní. To jsou např. `Django REST Framework <https://www.django-rest-framework.org/>`__, `Flask-Restful <https://flask-restful.readthedocs.io/>`__, `Eve <https://docs.python-eve.org/>`__, a další.
