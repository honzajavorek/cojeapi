Úvod do API
===========

Na API si nelze sáhnout a není možné je vidět, ale přesto dnes nepřímo ovlivňují život každého z nás. Bohužel není snadné zjistit, co ona API vlastně jsou. `Článek na Wikipedii <https://cs.wikipedia.org/wiki/API>`_ začíná tím, že jde o *rozhraní pro programování aplikací*, a pokračuje odborným textem, jímž se běžný smrtelník prokouše jen těžko. Tento text se snaží API **vysvětlit na příkladu a běžnými slovy**.

Předpověď počasí na mobilu
--------------------------

Na jakémkoliv mobilu dnes najdete předpověď počasí. Jak se tam ale dostane? Nejspíš tušíte, že předpovědi vznikají v `Českém hydrometeorologickém ústavu <https://cs.wikipedia.org/wiki/%C4%8Cesk%C3%BD_hydrometeorologick%C3%BD_%C3%BAstav>`_. Jak je ale možné, že jakmile se v ČHMÚ shodnou na zítřejší bouřce, objeví se vám to **během sekundy** na displeji?

Ať už šlo o noviny, rozhlas nebo televizi, dříve redakcím stačilo, aby si předpověď zjistili **jednou denně**. Nevím, jak to přesně probíhalo, ale představuji si, že někdo zavolal do sídla ČHMÚ v Komořanech, kde to zvedli a nadiktovali sluníčka nebo mráčky. Dnes už by to takto fungovat nemohlo. Data o počasí, která ČHMÚ uveřejňuje, je potřeba **okamžitě zobrazovat na tisícovkách míst na internetu**.

ČHMÚ má svoje webové stránky, kde předpovědi uveřejňuje. Jenže to vyžaduje, aby je na druhé straně **přečetl člověk a někam je přepsal**. Zatímco u redakcí si snad lze představit studenta žurnalistiky na brigádě, jak zoufale nonstop sleduje web ČHMÚ a opisuje povodňová varování na web zpravodajství, pro aplikaci ve vašem mobilu by toto byla nepřekonatelná komplikace.

Váš mobil potřebuje mít možnost **zjistit si předpověď automaticky**. Ústav tedy ukládá informace o počasí tak, aby byly **strojově čitelné**, a zpřístupňuje je **ke stažení** na svém webu. Představte si to zhruba tak, že místo aby nakreslili mráčky na svůj web, uloží odborníci v ČHMÚ všechno do nějaké tabulky, třeba i Excelové, kde je předem dané, co znamená jaký řádek a sloupec. Navíc jasně řeknou, že tato tabulka se bude vždy nacházet na adrese ``https://chmi.cz/predpoved.xslx`` a budou v ní vždy aktuální informace.

Aplikace ve vašem mobilu pak může z adresy ``https://chmi.cz/predpoved.xslx`` každou hodinu tabulku stáhnout, rozluštit její řádky a sloupce, poskládat z toho aktuální předpověď počasí a zobrazit vám ji jako mráčky. No a tomuto mechanismu, kdy **jedna strana něco na stabilní adrese poskytne ve strojově čitelné formě, a druhá je schopna to kdykoliv strojově číst a něco užitečného s tím dělat**, se říká webové API.

Kurzy měn
---------

.. todo::
    https://github.com/honzajavorek/cs-apis/wiki/Kurzy-devizov%C3%A9ho-trhu-%C4%8CNB#form%C3%A1tovan%C3%BD-txt-soubor-s-aktu%C3%A1ln%C3%ADmi-kurzy-devizov%C3%A9ho-trhu

Webová API, která možná znáte
-----------------------------

.. todo::
    https://github.com/honzajavorek/cojeapi/issues/8

Jsou i jiná API než webová?
---------------------------

.. todo::
    zmínit něco o programátorských API v programátorštině

Kam dál?
--------

.. todo::
    Vysvětlit co se nachází ve zbytku návodu a upozornit na prg zkušenost

.. note::
    Zatímco tato kapitola by měla být srozumitelná každému, všechny
    následující již vyžadují základní programátorské dovednosti. Ty lze získat
    například na `Nauč se Python! <https://naucse.python.cz/>`_
