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

Co si budeme povídat, takto data běžně nevypadají. Většinou jsou někde v databázi, v souboru, apod. Zpravidla je dostaneme jako seznam nebo slovník, ne jako připravený řetězec. Pojďme si tedy tuto situaci nasimulovat. Nejdříve si data vytáhneme do proměnné.

.. literalinclude:: ../code/base_data.py
    :language: python
    :emphasize-lines: 4-8, 16

Nyní z dat uděláme slovník, který až při sestavování odpovědi složíme do textu. Tím rozdělíme uložení dat a jejich prezentaci navenek. Jak už bylo zmíněno, data většinou přicházejí např. z databáze právě jako slovník, takže toto rozdělení je v praxi potřebné a velmi časté.

.. literalinclude:: ../code/base_data_dict.py
    :language: python
    :emphasize-lines: 4-8, 17-20

Takovéto API nám bude fungovat stále stejně, protože ze slovníku opět složí řetězec, který jsme původně posílali v odpovědi. Data jsou nyní ale nezávislá na tom, jak je budeme prezentovat uživateli. Prakticky si tuto výhodu ukážeme v následujících odstavcích.

Posíláme JSON
-------------

Jak jsme si :ref:`vysvětlovali <struktura>`, obyčejný text není nejlepší způsob, jak něco udělat strojově čitelné. Zkusíme tedy poslat naše data jako :ref:`JSON`.

.. literalinclude:: ../code/json_response.py
    :language: python
    :emphasize-lines: 1, 16-17

Jak vidíme, kód se nám s JSONem zjednodušil. Navíc díky tomu, že máme data hezky oddělená od samotného API, nemuseli jsme je nijak měnit. Stačilo změnit způsob, jakým se budou posílat v odpovědi. Když aplikaci spustíme, můžeme opět použít curl nebo prohlížeč a ověřit výsledek.

.. literalinclude:: ../code/json_response_test.txt
    :language: text

.. image:: ../_static/images/me-api-json.png
    :alt: api.py API, odpověď ve formátu JSON
    :align: center

A je to, máme své první JSON API! Už teď jsme se dostali dál, než kam se se svým API dostala :ref:`ČNB <cnb>`.

.. note::
    Pokud máte v datech diakritiku, bude zakódována. Kdybych se jmenoval Řehoř, vypadal by můj JSON takto: ``{"name": "\u0158eho\u0159", ...}`` Jestliže se chceme takového kódování zbavit, můžeme při tvorbě JSONu nastavit ``ensure_ascii`` na ``False``. Strojům to bude jedno, ale lidem se to bude lépe číst:

    .. code-block:: python

        response.body = json.dumps(get_personal_details(), ensure_ascii=False)

    Stejně tak je strojům jedno, jestli jsou, nebo nejsou jednotlivé části JSONu hezky odsazené. Pokud chcete, aby vaše API odsazovalo, nastavte parametr ``indent`` na počet mezer (používá se 2 nebo 4):

    .. code-block:: python

        response.body = json.dumps(get_personal_details(), ensure_ascii=False, indent=2)

    Zbytek příkladů nebude tyto možnosti využívat, aby byl kód v ukázkách stručnější.

.. todo::
    Udělat z formátování JSONu kapitolu, vytáhnout to do funkce, a přepsat následující příklady.

Protože :ref:`odpověďi <http-response>` mají ve většině případů status kód 200 a protože :ref:`JSON` je nejpoužívanější formát, tak je Falcon ve skutečnosti nastavuje jako výchozí. Můžeme proto zcela vynechat dva řádky z našeho programu a stále bude fungovat tak, jak jsme chtěli:

.. literalinclude:: ../code/json_response_simplified.py
    :language: python
    :emphasize-lines: 14-15

Přidáváme další endpoint
------------------------

Naše API má zatím pouze jednu adresu, na kterou se může klient dotazovat. V hantýrce programátorů webů by se řeklo, že má jednu "routu" (z anglického *route*). V hantýrce programátorů API by se zase řeklo, že má jeden *endpoint*. No a API s jedním endpointem není nic moc. Přidáme tedy druhý, který bude světu sdělovat seznam filmů, které bychom chtěli vidět.

.. literalinclude:: ../code/movies.py
    :language: python
    :emphasize-lines: 18-29, 34

Když aplikaci spustíme, bude na adrese ``/movies`` vracet seznam filmů.

.. literalinclude:: ../code/movies_test.txt
    :language: text

Kdyby každý měl takovéto API, mohl by někdo vytvořit třeba mobilní appku na organizaci filmových večerů. Dávala by dohromady lidi, kteří jsou poblíž a mají stejné filmy na svých seznamech.

Čteme URL parametry
-------------------

Co kdybychom ale chtěli vidět opravdu hodně filmů? Možná bychom chtěli dát uživatelům našeho API možnost výsledky filtrovat. K tomu se nám mohou hodit :ref:`URL parametry <http-request>`. Chtěli bychom třeba, aby klient mohl udělat dotaz na ``/movies?name=shark`` a tím by našel jen ty filmy, které mají v názvu řetězec ``shark``.

Nejdříve si připravme hledání. Vytvoříme funkci ``filter_movies()`` s parametry ``movies`` a ``name``, která vrátí pouze ty filmy, jejichž název obsahuje hodnotu tohoto parametru, a to bez ohledu na velká a malá písmena. Pokud bude parametr nastaven na ``None``, vrátí všechny filmy.

V následujícím příkladu je použit `cyklus <https://naucse.python.cz/course/pyladies/sessions/loops/>`__, ale kdo zná funkci `filter <https://docs.python.org/3/library/functions.html#filter>`__ nebo `list comprehentions <https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>`__, může si klidně poradit jinak.

.. literalinclude:: ../code/movies_filter.py
    :language: python
    :pyobject: filter_movies

Nyní potřebujeme přečíst z dotazu parametr a použít jej:

.. literalinclude:: ../code/movies_filter.py
    :language: python
    :emphasize-lines: 26-34, 40-41

Pokud se na náš nový endpoint dotážeme bez parametrů, měl by fungovat stejně jako předtím. Jestliže ale přidáme ``?name=`` do adresy, měla by hodnota parametru filtrovat filmy.

.. literalinclude:: ../code/movies_filter_test.txt
    :language: text

Vidíme, že tentokrát jsme dostali v těle odpovědi jen dva filmy místo čtyř.

Detail filmu
------------

V našem případě má každý film jen název a rok uvedení, ale většinou data nebývají tak strohá. Pojďme si k filmům přidat víc údajů, ať naše "databáze" působí o něco víc realisticky.

Když něco evidujeme, zpravidla tomu přiřadíme nějaké evidenční číslo, abychom to mohli jednoznačně odlišit a případně i rychle najít. Programátoři takovému údaji říkají *unikátní identifikátor*, což zkracují na ID nebo ``id``. Filmy se mohou jmenovat stejně, takže jméno se na to nehodí. Kdybychom měli opravdovou databázi, něco by nám pro každý záznam sama vymyslela, ale takto si musíme poradit sami. Použijeme tedy prostě pořadové číslovky od jedničky.

Kromě ``id`` přidáme každému filmu ještě ``name_cs`` s českým názvem (``cs`` je mezinárodní standardní kód pro `Češtinu <https://cs.wikipedia.org/wiki/Seznam_k%C3%B3d%C5%AF_ISO_639-2>`__), ``imdb_url`` s odkazem na `IMDb <https://www.imdb.com/>`__ a ``csfd_url`` s odkazem na `ČSFD.cz <https://www.csfd.cz/>`__.

.. literalinclude:: ../code/movies_db.py
    :language: python
    :lines: 18-51

Když se podíváme, co nyní vrací naše API, uvidíme o dost více dat:

.. literalinclude:: ../code/movies_db_test.txt
    :language: text

Pokud bychom přidali ještě více údajů a měli v seznamu větší množství filmů, byla by odpověď na endpointu ``/movies`` už možná příliš velká a pro některé uživatele našeho API by tam mohlo být možná až příliš mnoho zbytečných informací. Kdybychom tvořili webové stránky, seznam filmů by nejspíš obsahoval jen základní údaje a zbytek by byl na nějaké stránce s detailem filmu pro ty, které to zajímá. Při tvorbě API je praxe stejná.

Pojďme tedy upravit API tak, aby v seznamu vypisovalo jen ``name`` a odkaz na detail filmu. Nejdříve ale vytvoříme ten, ať máme na co odkazovat. Jako obvykle se zamyslíme nad tím, jak by měl nový endpoint fungovat:

.. literalinclude:: ../code/movies_detail_example.txt
    :language: text

Chceme tedy, abychom mohli na adrese ``/movies/1`` zjistit informace o filmu s ID číslo jedna, na adrese ``/movies/2`` o filmu s ID číslo dvě, atd.

Začneme funkcí ``get_movie_by_id()``, která dostane seznam filmů ``movies`` a identifikátor ``id``. Prohledá seznam a když v něm najde film s daným identifikátorem, vrátí tento film.

.. literalinclude:: ../code/movies_detail.py
    :language: python
    :pyobject: get_movie_by_id

Nyní přidáme další endpoint. To sice už umíme, ale nyní je v tom drobný háček. Potřebujeme totiž obsloužit hned čtyři adresy:

-   ``/movies/1``
-   ``/movies/2``
-   ``/movies/3``
-   ``/movies/4``

Určitě se nám ale nechce přidávat každou zvlášť. Co kdybychom v seznamu měli dvacet filmů? Potřebujeme něco, co by obsloužilo všechny zmíněné adresy.

Falcon nám dává řešení v podobě možnosti zapsat adresu jako "šablonu", podle které bude odchytávat odlišné adresy a směřovat na jeden a ten samý kód pro jejich obsluhu.

.. literalinclude:: ../code/movies_detail.py
    :language: python
    :lines: 78-87

Jak vidíme, pokud zadáme adresu jako ``/movies/{id:int}``, dostane naše metoda ``on_get()`` navíc čtvrtý parametr. V něm bude to, co Falcon v adrese odchytne na místě naší značky ``{id:int}``. První část značky i parametr metody si vhodně pojmenujeme jako ``id``. Druhá část značky Falcon upozorňuje na to, že namísto značky očekáváme pouze celá čísla (*int* odkazuje na vestavěnou funkci ``int()`` a anglické slovo *integer*).

Když nyní spustíme naše API a vyzkoušíme, co vrací na adrese ``/movies/1``, měli bychom dostat informace o prvním filmu v seznamu:

.. literalinclude:: ../code/movies_detail_1_test.txt
    :language: text

Zkuste si to i pro ostatní filmy.

Nenalezeno
----------

Naše API umí hezky odpovídat v případě, že se číslem trefíme do existujícího filmu. Co se ale stane pokud se dotážeme na nějakou hloupost?

.. literalinclude:: ../code/movies_detail_hello_test.txt
    :language: text

Jistě, Falcon díky ``{id:int}`` obsluhuje jen adresy s čísly, takže se za nás postará o odpověď. Vrací ``404 Not Found``, čímž dává uživateli najevo, že se asi spletl, protože na této adrese nic není. Co když se ale dotážeme s číslem, akorát na neexistující film, např. na ``/movies/42``?

.. literalinclude:: ../code/movies_detail_42_test.txt
    :language: text

Tady nám Falcon už nepomůže. Adresu obslouží naše metoda a ta, jak vidíme, nevrací zrovna nejlepší odpověď. Žádný film číslo 42 neexistuje, ale naše API se chová, jako by to nebyl žádný problém. Upravíme třídu ``MovieResource`` tak, aby s touto situací počítala. Pokud funkce ``get_movie_by_id()`` nic nenajde, odpovíme s chybovým status kódem. Tělo posílat žádné nemusíme.

.. literalinclude:: ../code/movies_not_found.py
    :language: python
    :pyobject: MovieResource

Pokud se po této změně dotážeme na neexistující film, měli bychom dostat chybu:

.. literalinclude:: ../code/movies_not_found_42_test.txt
    :language: text

Získávání informací o existujícím filmu by mělo fungovat stejně jako předtím.

.. literalinclude:: ../code/movies_not_found_1_test.txt
    :language: text

V tomto návodu s chybou neposíláme žádné tělo, ale je běžné nějaké poslat a poskytnout v něm uživateli našeho API více informací o tom, co se stalo, např. takto:

.. literalinclude:: ../code/movies_not_found_example.txt
    :language: text

Zatímco status kód ``404 Not Found`` je záležitost standardu protokolu :ref:`HTTP`, strukturu těla chybové zprávy jsme si v tomto případě vymysleli. Aby uživatel našeho API věděl, že se má při chybě podívat na její důvod právě do ``message``, nesmíme to potom zapomenout :ref:`popsat v dokumentaci <dokumentace>`.

.. note::
    Na strukturu těla chybové zprávy také existují standardy, byť je málokdo dodržuje:

    -   `vnd.error <https://github.com/blongden/vnd.error>`__
    -   Problem Details for HTTP APIs, :rfc:`7807`

    V případě toho druhého bychom pak v hlavičce ``Content-Type`` místo ``application/json`` poslali ``application/problem+json`` a příjemce by díky tomu hned mohl tušit, jakou přesně strukturu bude tělo chybové odpovědi mít.

Odkazování mezi endpointy, reprezentace, resource
-------------------------------------------------

Detail filmu máme připravený, takže se můžeme pustit do úprav seznamu filmů, tedy třídy ``MoviesResource``. Jak již bylo zmíněno, budeme v seznamu chtít jen ``name`` a odkaz na detail filmu.

Doteď bylo to, co jsme poslali v odpovědi, vždy shodné s tím, jak máme data uložena interně v naší aplikaci. Nyní ale nastává situace, kdy chceme v odpovědi poslat něco trochu jiného, než jak data vypadají ve skutečnosti. Chceme poslat jen určitou *reprezentaci* těchto dat. Začneme tedy funkcí, která vezme seznam filmů a poskytne nám jeho reprezentaci tak, jak jsme si ji vymysleli:

.. literalinclude:: ../code/movies_repr.py
    :language: python
    :pyobject: represent_movies

Nyní pojďme upravit ``MoviesResource``. Víme, že adresa našeho API je teď ``http://0.0.0.0:8080``, ale jakmile budeme chtít aplikaci :ref:`uveřejnit někam na internet <nowsh>`, bude zase jiná. Proto je lepší si ji vytáhnout z objektu ``request``.

.. literalinclude:: ../code/movies_repr.py
    :language: python
    :pyobject: MoviesResource

Zbytek úprav by měl být celkem srozumitelný. Nejdříve filmy filtrujeme podle parametrů, poté vytvoříme reprezentaci výsledného seznamu a nakonec z ní uděláme JSON a ten pošleme jako tělo odpovědi. Když aplikaci spustíme a vyzkoušíme dotazem např. na ``/movies/?name=shark``, měla by nám vracet správně filtrovaný seznam filmů v nové podobě:

.. literalinclude:: ../code/movies_repr_test.txt
    :language: text

V hantýrce API návrhářů a vývojářů bychom řekli, že film, nebo v tomto případě seznam filmů, je nějaký *resource*, který zpřístupňujeme uživatelům našeho API na adrese ``/movies``. Je reprezentován jako JSON, v němž má každý film název a odkaz k dalším podrobnostem. Proto má ``MoviesResource`` v názvu slovo resource.

Je důležité rozlišit, že *resource* je pomyslný, nehmatatelný model světa, zatímco reprezentace už je jeho konkrétní zobrazení. Jak jsme si vyzkoušeli u ``PersonalDetailsResource``, lze mít více různých reprezentací pro tutéž pomyslnou věc - čistě textovou, nebo jako JSON, nebo úplně jinou.

A když už jsme u toho našeho prvního endpointu, správné :ref:`REST` API by mělo být propojeno pomocí odkazů. Z odpovědi s osobními informacemi však nelze nijak zjistit, že v API zpřístupňujeme ještě i seznam filmů, které chceme vidět. Pojďme to napravit:

.. literalinclude:: ../code/movies_repr.py
    :language: python
    :pyobject: PersonalDetailsResource

Odkaz jsme pojmenovali ``movies_watchlist_url``, protože kdyby to bylo pouze ``movies_url``, nebylo by úplně zřejmé, o jaký přesně seznam filmů se jedná. Samozřejmě i tak by to mělo být :ref:`popsáno v dokumentaci <dokumentace>`, ale proč neusnadnit druhé straně práci a nenazvat věci zřejmějším jménem?

Content negotiation
-------------------

.. todo::
    vysvetlit o co jde, kdyz udelame accept na cs

Přidáváme filmy
---------------

Nyní máme API, které je pouze ke čtení. Řekněme, že bychom chtěli, aby nám někdo mohl doporučit film na zhlédnutí tím, že jej přidá do našeho seznamu. Opět si nejdříve navrhněme, jak by věc měla fungovat.

.. literalinclude:: ../code/movies_post_example.txt
    :language: text

Pokud metodou ``POST`` přijde :ref:`dotaz <http-request>` na adresu ``/movies``, API přečte zaslané tělo dotazu (očekává JSON), které reprezentuje film, a přidá tento film do našeho seznamu. Poté odpoví kódem ``201 Created`` a tělem (opět JSON), v němž je změnený obsah seznamu filmů.

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

.. _dokumentace:

Dokumentujeme API
-----------------

.. todo::
    https://github.com/honzajavorek/cojeapi/issues/37, formáty pro popis API

.. _frameworky:

Frameworky pro tvorbu serveru
-----------------------------

V tomto návodu jsme si ukázali, jak vyrobit jednoduché API s pomocí frameworku `Falcon <https://falcon.readthedocs.io/>`__, jenž je pro toto použití vyladěný.

Jelikož jsou webová API založena na podobných principech jako webové stránky, šlo by použít i známější frameworky `Flask <http://flask.pocoo.org/>`__ nebo `Django <https://www.djangoproject.com/>`__. Pokud bychom v nich ale tvořili složitější API, brzy by nám přišlo, že s takovým frameworkem spíše bojujeme, než aby nám pomáhal.

Např. chyby by takový framework standardně posílal jako HTML, přitom by bylo lepší, kdyby byly také naformátovány jako JSON. Museli bychom ručně doplnit kód, který upraví výchozí chování Flasku nebo Djanga a bude chyby posílat tak, jak se v JSON API sluší a patří.

Z tohoto a dalších důvodů je tedy výhodnější buďto pro API využít specializovaný framework, jakým je Falcon, nebo se poohlédnout po doplňcích do Flasku, popřípadě Djanga, které nám tvorbu API usnadní. To jsou např. `Django REST Framework <https://www.django-rest-framework.org/>`__, `Flask-Restful <https://flask-restful.readthedocs.io/>`__, `Eve <https://docs.python-eve.org/>`__, a další.
