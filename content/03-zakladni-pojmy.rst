Základní pojmy
==============

Než se ponoříme do samotné tvorby klienta nebo serveru, je dobré pochopit některé základní pojmy kolem API.

Na čem to celé běží: HTTP
-------------------------

.. todo::
    curl jednoduché requesty
    curl -i na response

    protocol? http/https? zanedbat a říct o tom až u auth?

    request, response
    method, url (params!), headers, body
    status code, headers, body

Typy API: SOAP, REST, GraphQL
-----------------------------

.. todo::
    vše používá HTTP, příklady
    některé jsou přesně spec, REST je arch styl a vysvětlit jak vznikl a co je hypermedia
    vysvětlit jaká je dnes většina API (jakože REST, "webové"), Zdeňkův článek

Knihovny pro tvorbu klienta
---------------------------

.. todo::
    vysvětlit obecného klienta
    request(s)

Specializované knihovny (SDK)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. todo::
    vysvětlit specializovaného klienta
    příklady

Knihovny pro tvorbu serveru
---------------------------

.. todo::
    DRF, Flask-Restful, eve

Formáty: XML, JSON
------------------

.. todo::
    formátů je nesčetně, vysvětlit media types (content types)
    toto jsou ty nejběžnější a nejpoužívanější

    XML, příklady, výhody nevýhody, na co se používá (GPX, KML, SVG)
    rozdíly mezi XML a HTML
    jakými knihovnami s tím pracovat

    JSON, příklady, výhody nevýhody, na co se používá (všechno možný)
    rozdíly mezi JSON a Python slovníkem (JS objektem?)
    jakými knihovnami s tím pracovat

Shrnutí
-------

.. todo::
    víceméně hlavně přehledový obrázek jak se to všechno k sobě má
