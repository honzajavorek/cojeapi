.. note::

   JSON se musí psát vždy s dvojitými uvozovkami. Na Linuxu nebo macOS to není problém, protože v terminálu fungují na ohraničení i jednoduché uvozovky a lze udělat následující:

   .. code-block:: text

         --data '{"message": "Ahoj"}'

   Na Windows bohužel nelze jednoduché uvozovky použít, k dispozici jsou pouze dvojité a ty kolidují s těmi v JSONu. Proto musíme v celém JSONu přepsat uvozovky na ``\"``:

   .. code-block:: text

         --data "{\"message\": \"Ahoj\"}"
