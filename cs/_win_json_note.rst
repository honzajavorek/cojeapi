.. note::

   JSON se musí psát vždy s dvojitými uvozovkami. Na Linuxu nebo macOS to není problém, protože v příkazové řádce fungují na ohraničení i jednoduché uvozovky a lze udělat následující:

   .. code-block:: text

         --data '{"message": "Ahoj"}'

   Na Windows bohužel nelze jednoduché uvozovky použít, k dispozici jsou pouze dvojité a ty kolidují s těmi v JSONu. Proto musíme v celém JSONu přepsat uvozovky na ``\"``:

   .. code-block:: text

         --data "{\"message\": \"Ahoj\"}"

   Další nepříjemností je skutečnost, že kvůli specifickému kódování textu v příkazové řádce na Windows není jednoduché posílat data, která budou obsahovat diakritiku. Následující tedy nebude fungovat:

   .. code-block:: text

         --data "{\"message\": \"Čauky mňauky\"}"

   V tomto návodu přidáme před uvozovky lomítka a diakritice se vyhneme. V praxi se dají oba problémy řešit tím, že data nebudeme psát přímo do příkazové řádky, ale uložíme si je vedle do souboru a řekneme programu curl, aby je z něj načetl:

   .. code-block:: text

         --data @new-movie.json
