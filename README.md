# LarisKursiBot

This is a Telegram Bot that simplifies the keeping track of the everyday convertion rate of Georgian Lari - GEL defined by National Bank of Georgia.

<!-- TOC START min:1 max:3 link:true update:true -->
- [Where to find the bot](#where-to-find-the-bot)
- [How to use it](#how-to-use-it)
- [Get the latest rate](#get-the-latest-rate)
  - [How to check USD to GEL rate](#how-to-check-usd-to-gel-rate)
  - [How to check EUR to GEL rate](#how-to-check-eur-to-gel-rate)
- [Subscribe to the daily rate](#subscribe-to-the-daily-rate)
  - [Rates update](#rates-update)
- [Technology](#technology)
  - [Bot](#bot)
  - [Getting the rates](#getting-the-rates)

<!-- TOC END -->

## Where to find the bot

1. You can type `LarisKursiBot` in the search bar of the main window of Telegram.
2. Or open the link https://t.me/LarisKursiBot


## How to use it

Normally it should write to use the available commands when you connect to the bot. If it's not the case or you want to read again the instructions you can message to bot the next command:
```
/start
```

## Get the latest rate

### How to check USD to GEL rate

Just message to bot the next command:
```
/usd
```
or
```
/დოლარი
```

### How to check EUR to GEL rate

Just message to bot the next command:
```
/eur
```
or
```
/ევრო
```

## Subscribe to the daily rate

You can also subscribe to the daily update of USD to GEL and EUR to GEL rates by messaging to bot the next command:
```
/subscribe
```
and of course you can unsubscribe from this updates as well by messaging to bot the next command:
```
/unsubscribe
```

### Rates update
The new rate is published everyday except weekends and holidays at most at 17:00 by National Bank of Georgia (NBG).
If you are subscribed to daily updates you will receive the Telegram message with latest rate at 17:05 (5 minute is an estimated time for NBG's WebService to update the rate).

<aside class="warning">
:warning: When subscribed, you will receive the message with latest rates even on weekends and holidays.
</aside>

## Technology

### Bot
The excellent [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) is used to make the bot alive

### Getting the rates
NBG's SOAP web service is avalable at https://services.nbg.gov.ge/Rates/Service.asmx.  
You can check the complete list of NBG's publicly available services at https://services.nbg.gov.ge/
