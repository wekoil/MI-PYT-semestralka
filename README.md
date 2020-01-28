# Zadani

Cilem semestralky je vytvorit webovou aplikaci. 

Ta bude umet posilat upozorneni na blizici se udalosti. Vytvorim interface a implementuji pouze posilani na mail a slack.

Udalosti se mohou importovat i z kalendare (nejakeho souboru, kde budou data ve spravnem formatu).

Nejake jednoduche ukoly bude umet sama vykonavat (napr. poprat nekomu k narozeninam). Opet zde bude obecny interface a implementuji pouze posilani na mail a zpravy na fb (pokud to fb umoznuje, popr. jiny casto pouzivany messenger).

## Poznamky

Aplikace umi posilat zpravy na mail, slack a pres aplikaci twilio i na whatsapp. Jedina potiz je, ze z twilia se daji odesilat zpravy pod jinym cislem, nez co ma clovek normalne na whatsappu a s free verzi pouze na predem overena cisla (musim z cisla poslat zpravu na twilio a pak teprve muzu z twilia poslat zpravu na toto cislo).

Na posilani zprav pres FB jsem objevil https://github.com/carpedm20/fbchat, ale pry porusuje pravidla FB a nechtel jsem testovat na svem uctu a schvaleni fejkoveho trva uz pres 30 hodin. Takze zatim neimplementovano.

Udalosti se daji importovat ze souboru v ics formatu. V description se ocekava JSON format s udaji (jak a komu mam poslat zpravu).