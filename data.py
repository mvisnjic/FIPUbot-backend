chatBotData = {"intents": [
             {"tag": "greeting",
              "patterns": ["Dobar dan", "Kako si?", "Ej", "Ej bok", "Sta ima", "Sa ima", "Cao", "Hej"],
              "responses": ["Pozdrav!", "Bok", "Kako ste?","Sto ima kod vas?", "Dobar dan!", "Kako je?"],
             },
             {"tag": "age",
              "patterns": ["Koliko si star?", "Kada je tvoj rodendan?", "Kada si roden?"],
              "responses": ["Star sam 3 tjedna :)", "Roden sam kao ideja za zavrsni rad.", "Rodendan mi je 24.07.2022", "24.07.2022"]
             },
             {"tag": "date",
              "patterns": ["Sto radis za tjedan dana?","Zelis li ici u izlazak?", "Kakvi su ti planovi za ovaj vikend?"],
              "responses": ["Slobodan sam cijeli tjedan", "Nemam nikakvih planova", "Nisam zauzet"]
             },
             {"tag": "name",
              "patterns": ["Kako se zoves?", "Kako te zovu?", "Ko si ti?", "Tvoje ime?", "Ime?"],
              "responses": ["Moje ime je FIPUbot.", "Ja sam FIPUbot", "FIPUbot"]
             },
             {"tag": "goodbye",
              "patterns": [ "doviđenja", "dovidenja", "okej ajde bok", "okej cao", "okej bok", "bb", "adios", "bye"],
              "responses": ["Bilo je lijepo razgovarati sa Vama.", "Ukoliko nesto trebas, javi se opet"]
             },
             {"tag": "fail",
              "patterns": [ "g2g", "adios", "cya", "?", "kwekfowe"],
              "responses": ["Bilo je lijepo razgovarati sa Vama.", "Čujemo se kasnije.", "Ne razumijem.", "Probajte smisliti bolji upit!"]
             },
             {"tag": "faq1",
             # 1. Koliko u programu Erasmus+ traje razdoblje mobilnosti za studij ili stručnu praksu?
              "patterns": [ "Koliko", "u programu", "Erasmus+", "?", "traje", "razdoblje mobilnosti", "studij ili stručna praksa"],
              "responses": ["U programu Erasmus+ studenti na studiju mogu provesti od 3 do 12 mjeseci. Razdoblje stručne prakse može trajati od 2 do 12 mjeseci. U slučaju kombiniranja studija i stručne prakse najkraće trajanje mobilnosti jest 3 mjeseca, a najduže 12 mjeseci, bez obzira na raspodjelu vremena između ovih oblika mobilnosti."]
             },
             {"tag": "faq2",
             # 2. Koje je uvjete potrebno zadovoljiti za studij ili stručnu praksu u programu Erasmus+?
              "patterns": [ "Koje", "je uvjete", "potrebno", "?", "zadovoljiti", "programu Erasmus+", "studij ili stručna praksa"],
              "responses": ["Da biste studirali ili se stručno usavršavali u inozemstvu, morate studirati na visokom učilištu u programu preddiplomskoga, diplomskoga ili poslijediplomskog studija nakon kojeg stječete zvanje prvostupnika (bacc.), magistra odnosno magistra struke (mag.) ili doktora znanosti. Vaše matično visoko učilište treba biti u zemlji koja sudjeluje u programu Erasmus+ vezanom za visoko obrazovanje, a programske su zemlje u akademskoj godini 2014./2015. sve zemlje članice EU-a te Island, Lihtenštajn, Norveška, Turska i Makedonija. Od akademske će godine 2015./2016. u Erasmus+ studentskoj mobilnosti moći sudjelovati istudenti iz ustanova u partnerskim zemljama (napomena: stručna praksa između partnerskih i programskih zemalja neće se moći ostvariti u 2015. godini). Ako se vaše visoko učilište nalazi u programskoj zemlji, treba biti nositelj Erasmus povelje za visoko obrazovanje (Erasmus Charter for Higher Education – ECHE) kojom se jamči kvaliteta provedbe aktivnosti mobilnosti za sve sudionike. Na mrežnim stranicama vaše ustanove možete provjeriti je li nositeljica ECHE-a, a potpuni popis ustanova nositeljica Povelje možete pronaći na poveznici: http://eacea.ec.europa.eu/funding/2014/call_he_charter_en.php. Vaša matična ustanova određuje kriterije za odabir studenata koji će pohađati studij ili obavljati stručnu praksu u inozemstvu (za više informacija molimo pročitajte odgovor na 9. pitanje)"]
             },
             {"tag": "faq3",
             # 3. . Mogu li studenti u programu Erasmus+ tijekom studija više puta ostvariti mobilnost?
              "patterns": [ "Mogu li", "studenti", "u programu", "Erasmus+", "tijekom", "studija", "više puta", "ostvariti mobilnost"],
              "responses": ["Erasmus+ studentima omogućuje studij ili stručnu praksu u ukupnom trajanju do 12 mjeseci za svaku razinu studija (preddiplomska, diplomska, poslijediplomska). Mobilnost je tijekom studija moguće ostvariti više puta – važno je poštovati uvjet od najviše 12 mjeseci po svakoj razini studija. Primjerice, na istoj se razini studija možete prijaviti za studij u trajanju do 6 mjeseci, a zatim i za stručnu praksu u trajanju do 6 mjeseci (ili npr. 4 + 8 mjeseci). Studenti koji pohađaju integrirane studije, kao što je npr. medicina, mobilnost mogu ostvariti u ukupnom trajanju do 24 mjeseca.Navedeni maksimum po razini studija odnosi se i na mobilnosti ostvarene u Programu za cjeloživotno učenje (LLP). Ako je primjerice student integriranih studija već sudjelovao u programu mobilnosti u okviru LLP-a, npr. u trajanju od 8 mjeseci, u okviru programa Erasmus+ tijekom studija može otići na mobilnost u trajanju od 16 mjeseci."]
             },
             {"tag": "faq4",
             # 4. Je li moguće otići na studij i obaviti stručnu praksu u okviru iste mobilnosti?
              "patterns": [ "Je li moguće", "otići na studij", "obaviti stručnu praksu", "u okviru iste mobilnosti"],
              "responses": ["Odlazak na studij i stručnu praksu u inozemstvu u sklopu iste mobilnosti mogućnost je koju nudi program Erasmus+. U ovom je slučaju najkraće trajanje mobilnosti 3 mjeseca, a najduže 12 mjeseci, bez obzira na raspodjelu vremena između ostvarenih mobilnosti."]
             },
             {"tag": "faq5",
             # 5. Može li student koji je u Programu za cjeloživotno učenje (potprogram Erasmus) već ostvario mobilnost sudjelovati u programu Erasmus+ te otići na studij ili stručnu praksu?
              "patterns": [ "Može li student koji je", "Programu za cjeloživotno učenje", "potprogram Erasmus", "već ostvario mobilnost sudjelovati u programu Erasmus+", "te otići na studij ili stručnu praksu"],
              "responses": ["Erasmus+ studentima omogućuje studij ili stručnu praksu u inozemstvu pod uvjetom da najduže trajanje mobilnosti tijekom jedne razine studija bude do 12 mjeseci. Ako ste u okviru Programa za cjeloživotno učenje (LLP) ostvarili maksimum od 12 mjeseci mobilnosti na jednoj razini studija, za mobilnost u programu Erasmus+ trebat ćete pričekati sljedeću razinu studija. Ako vam je pak mobilnost u programu LLP na trenutačnoj razini studija bila manja od 12 mjeseci, na istoj ćete razini studija u programu Erasmus+ moći ostvariti mobilnost do navedenoga najdužeg trajanja. Primjerice, ako ste u LLP-u tijekom preddiplomske razine na mobilnosti proveli 4 mjeseca, na istoj ćete razini studija u programu Erasmus+ moći ostvariti još 8 mjeseci (za studij ili stručnu praksu). Ako vam pak slijedi diplomska ili poslijediplomska razina studija, možete se prijavljivati za mobilnosti u trajanju do 12 mjeseci (nova razina studija). Sudjelovanje u drugim potprogramima LLP-a (npr. Leonardo) ili drugim programima kao što je Mladi na djelu (YiA) ne uzima se u obzir. Podsjećamo vas da uvijek trebate kontaktirati vašu matičnu visoku ustanovu (Erasmus koordinatore) jer je ona odgovorna za izbor sudionika te može postaviti dodatne uvjete na natječajima (primjerice, može dati prednost studentima koji još nisu ostvarili Erasmus mobilnost)."]
             },
            {"tag": "faq6",
             # 6. Ako je student tijekom Programa za cjeloživotno učenje (LLP) u potprogramu Leonardo boravio na stručnoj praksi, može li ići na studij ili stručnu praksu u okviru programa Erasmus+?
              "patterns": [ "Ako je student tijekom Programa za cjeloživotno učenje", "LLP",  "Programu za cjeloživotno učenje", "u potprogramu Leonardo boravio na stručnoj praksi", "može li ići na studij ili stručnu praksu", "okviru programa Erasmus+"],
              "responses": ["Sudjelovanje u drugim potprogramima LLP-a (npr. Leonardo) ili drugim programima kao što je Mladi na djelu (YiA) ne uzima se u obzir pri uvjetima sudjelovanja u mobilnostima vezanima za visoko obrazovanje. Student se, dakle, može prijaviti za mobilnosti u okviru programa Erasmus+."]
             },
            {"tag": "faq7",
             # 7. Može li student koji je u programu Mladi na djelu (YiA) volontirao preko Europske volonterske službe (EVS) otići na studij ili stručnu praksu u programu Erasmus+?
              "patterns": [ "Može li student koji je u programu Mladi na djelu", "YiA",  "volontirao preko Europske volonterske službe", "EVS", "tići na studij ili stručnu praksu u programu Erasmus+"],
              "responses": ["Budući da sudjelovanje u programu Mladi na djelu nije relevantno za uvjete sudjelovanja u mobilnostima vezanima za visoko obrazovanje, moguća je prijava za aktivnosti studija ili stručne prakse u programu Erasmus+."]
             },
            {"tag": "faq8",
             # 8. Kako se u programu Erasmus+ prijavljuje za studij ili stručnu praksu u inozemstvu?
              "patterns": [ "Kako se u programu Erasmus+", "prijavljuje za studij ili stručnu praksu u inozemstvu", "praksa inozemstvo"],
              "responses": ["Studenti se prijavljuju preko svojih visokih učilišta bez obzira na vrstu mobilnosti za koju su zainteresirani. Ured za međunarodnu suradnju u matičnom visokom učilištu nudi informacije o uvjetima sudjelovanja u Erasmus+ mobilnostima – detalji postupka odabira studenata, potrebni dokumenti, popis učilišta na kojima studenti mogu ostvariti mobilnost te uvjeti koje studenti moraju poštovati tijekom boravka na inozemnoj ustanovi."]
             },
            {"tag": "faq9",
             # 9. Koji su kriteriji odabira za sudjelovanje u programu Erasmus+?
              "patterns": [ "Koji su kriteriji odabira", "sudjelovanje u programu Erasmus+"],
              "responses": ["Da biste sudjelovali u aktivnostima mobilnosti vezanima za visoko obrazovanje unutar programa Erasmus+, morate zadovoljiti kriterije sudjelovanja navedene pod 2. pitanjem (Koje je uvjete potrebno zadovoljiti za studij ili stručnu praksu u programu Erasmus+?). Osim toga, potrebno je zadovoljiti uvjete koje odredi matično visoko učilište. Postupak odabira studenata i dodjeljivanja financijske potpore mora biti transparentan, dosljedan i potkrijepljen dokumentima te s njime moraju biti upoznati svi uključeni. Vaše matično visoko učilište može kao uvjet u izbornom postupku uvrstiti akademski uspjeh, prethodno iskustvo mobilnosti, motivaciju, iskustvo u zemlji u koju se odlazi na mobilnost (npr. povratak u zemlju podrijetla) itd. Kriteriji za odabir svakako moraju biti javni. Više informacija možete potražiti na mrežnim stranicama vašega visokog učilišta ili se obratiti Uredu za međunarodnu suradnju na vašem učilištu."]
             },
            {"tag": "faq10",
             # 10. Što slijedi nakon što je student izabran za studij ili stručnu praksu u programu Erasmus+?
              "patterns": [ "Sto slijedi nakon Erasmus+", "sto je student izabran", "studij ili stručnu praksu u programu Erasmus+"],
              "responses": ["Nakon što je student izabran za Erasmus+ mobilnost, matično visoko učilište treba mu dati Erasmus+ studentsku povelju (Erasmus+ student charter) u kojoj su navedena sva studentska prava i obveze koje ima tijekom boravka na mobilnosti u inozemstvu te su objašnjeni koraci koje student mora poduzeti prije, tijekom i poslije mobilnosti. Studenti koji na mobilnosti odlaze poslije listopada 2014., a jezik kojim će se tijekom mobilnosti trebati služiti jest engleski, francuski, njemački, talijanski, španjolski ili nizozemski (više će se jezika dodati od ak. god. 2015./2016.), pisat će online test jezične procjene (osim ako im je jezik mobilnosti materinski). Pristup rezultatu ove procjene imat će student, njegovo matično visoko učilište (ustanova primatelj neće imati pristup rezultatima testa online jezične procjene) te Europska komisija. S obzirom na to da je student već izabran, rezultati jezične procjene neće utjecati na odluku o njegovu odlasku na mobilnost. Kako bi studentima pomoglo u pripremi za aktivnost mobilnosti, matično im visoko učilište može, ovisno o njihovoj jezičnoj razini, ponuditi besplatan online jezični tečaj na engleskom, njemačkom, talijanskom, španjolskom ili nizozemskom jeziku. Na kraju razdoblja mobilnosti u inozemstvu studenti će pisati drugi test jezične procjene na temelju kojega će doznati koliko su unaprijedili svoje jezične vještine. Jednako tako, na temelju te će jezične procjene Europska komisija dobiti informacije o tome koliko je sudjelovanje u programu Erasmus+ utjecalo na jezične vještine studenata."]
             },
]}