# Serwer Piwny DS Riviera

Serwer Piwny DS Riviera to aplikacja napisana przez mieszkańców akademika Riviera. 
Jej zadaniem jest wsparcie w zarządzaniu pokojem. Jest ona utrzymywana na Raspberry Pi 3B+, które pełni rolę serwera aplikacji. 
Na ten moment aplikacja posiada następujące moduły:
- moduł użytkownika *accounts*,
- moduł rankingu w fife *fifarank*,
- moduł długów piwnych *beers*.

Planowane są również moduły:
- dashboard powitalny,
- forum segmentu,
- moduł zarządzania zakupami wspólnymi.


### Uruchomienie bazy
docker container run -p 5432:5432 -v spdb:/var/lib/postgresql/data -e POSTGRES_USER=serwerpiwny -e POSTGRES_DB=serwerpiwny -e POSTGRES_PASSWORD=serwerpiwny postgres