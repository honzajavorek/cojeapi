.. _intro:

API introduction
================

You cannot touch API and it is not possible to see it, however these days it indirectly influences everybody’s lives.

Unfortunately, it is not easy to find out, what APIs are - actually. `The article on Wikipedia <https://en.wikipedia.org/wiki/API>`__ begins with an explanation, that it is an application programming interface (API) and continues with professional technical text, which common mortals have difficulties to understand. This document is trying to explain API **on the common example using plain words**.


.. _meteo:

Weather prediction on mobile phone
----------------------------------

Predicting weather on your mobile phone is common on any device. But how does it get there? You probably do not suspect, that predictions do happen in your `national meteorological organization <https://en.wikipedia.org/wiki/Template:National_meteorological_organisations>`__. But how is it possible that as soon as the meteorologists agree on tomorrow’s storm, you do have it on your mobile phone display **within a second**?

.. image:: ../_static/images/chmu1.png
    :align: center
    :width: 60%

In the old days, to get weather prediction for the newspaper, radio or television the editorial staff had to submit a request for weather prediction from the meteorologists only **once a day**. I am not sure, how it was done, but I can imagine, that someone from the news called to the meteorological organization headquarter and on the other side of the phone the meteorologist told them the sunny and cloudy weather predicted.

Today, it could not work like this anymore. Weather data, which are publicly reported, are needed to be displayed **instantly on thousands of places on the internet at the same time**.

The meteorological organizations have their own websites, where the weather forecast is published. To access the information requires a person, who **reads and transcripts the information** to somewhere else.

In case of the news, one can imagine a poor intern, who desperately nonstop monitors the meteorological organization website and copies flood and other weather warnings on the news website. But in case of your mobile phone application, nothing like that is really an option.

Your mobile phone needs to be able to **detect predictions automatically**. Therefore, the meteorologists store weather information in order to be **machine-readable** and makes it **available for download** on their website. At a rough guess, image it as so that instead of drawing clouds on the web, the meteorologists will put everything in a table, even Excel spreadsheet, where it is predetermined, what does each line and column mean. In addition, they will tell you that this table is always at ``http://weather.gov/forecast.xslx`` and will be always up to date.

.. image:: ../_static/images/chmu2.png
    :align: center
    :width: 60%

Then every hour the application on your mobile phone can access the table at ``http://weather.gov/forecast.xslx`` and download it, decipher the rows and columns, combine the current weather forecasts and show you the resulting clouds and sunnies. This mechanism, when **one party provides something on a stable web address in machine-readable form, and the other party is able to machine read it anytime and to do something useful with it**, it is called the web API.


.. todo::
   The rest of the translation is in `this Google Doc <https://docs.google.com/document/d/1M77SJCudGzO_82H52ffTaP7Xz4gQlVBlM__IE-Bmo5o/edit>`__ until someone puts it here. If you want to help, please coordinate under the issue `#52 <https://github.com/honzajavorek/cojeapi/issues/52>`__.
