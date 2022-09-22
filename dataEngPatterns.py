chatBotData = {"intents": [
             {"tag": "greeting",
              "patterns": ["good morning", "good evening","good morning", "hey", "hi", "greeting", "hello", "bok", "book"],
              "responses": ["Pozdrav!", "Bok!", "Pozdrav. Kako ste, šta ima?","Pozdrav. Što ima kod vas?","Bok, kako je?"],
             },
             {"tag": "goodbye",
              "patterns": [ "goodbye", "okay bye", "okay goodbye", "alright thanks", "okay thanks for help", "bb", "adios", "bye bye", "ok thanks for your help"],
              "responses": ["Bilo je lijepo razgovarati sa Vama.", "Ukoliko nesto trebas, javi se opet."]
             },
             {"tag": "request",
              "patterns": ["I need something", 
                           "I have a question",
                           "I would like to know", 
                           "I want to know", 
                           "I have a few questions", 
                           "I am interested in something", 
                           "I wonder if"],
              "responses": ["Slobodno pitajte.", "Slušam...", "Pretvorio sam se u uho.", "Tko pita, ne skita."],
             },
             {"tag": "age",
              "patterns": ["when is your birthday?", "when were you born?"],
              "responses": ["Rođen sam kao ideja za završni rad.", "Nemam rođendan. :("]
             },
             {"tag": "go-out",
              "patterns": ["what are you doing in a week?","do you want to go out?", "What are your plans for this weekend?"],
              "responses": ["Slobodan sam jako malo vremena, žao mi je. :(", "Imam planove.", "Zauzet sam, a zašto?"]
             },
             {"tag": "fun",
              "patterns": ["where can I go out in Pula?", "where can I go out?", "party in Pula", "night life", "where students like to hang out"],
              "responses": ["Cargo, Pietas, Uljanik, Rustico, Stella... za ostalo pretraži Google. https://www.google.com/  :)"] 
                            
             },
             {"tag": "feelings",
              "patterns": ["how are you", "how you doing"],
              "responses": ["Ja sam dobro.", "Odlično.", "Top. :D"]
             },
             {"tag": "flatter",
              "patterns": ["lucky you", "easy to you", "it is easy for you", "you are the king", "you are awesome", "you are well programmed", "you are the best"],
              "responses": ["Hvala. :)"]
             },
             {"tag": "gratefulness",
             "patterns": ["thanks", "thanks for the answer", "ah thanks", "thanks for the help", "thank you"],
              "responses": ["Molim. Imaš još kakvo pitanje?", "Hvala tebi. Imaš još nekakvo pitanje?"]
             },
             {"tag": "rude",
              "patterns": ["I did not even think", "I didn not even think you were", "I do not think", "you have no idea", 
                           "you do not know anything", 
                           "you do not understand anything", 
                           "you are stupid", 
                           "you are badly programmed"],
              "responses": ["U redu. :)"]
             },
             {"tag": "say-something",
              "patterns": ["say something"],
              "responses": ["Nešto.", "Nemam ništa!"]
             },
             {"tag": "feelings-answer",
              "patterns": ["you are great?", "I am fine", "I am great", "I am enjoying myself", "I feel great", "here is nothing", "nothing"],
              "responses": ["Bas mi je drago.", "Drago mi je zbog tebe."]
             },
             {"tag": "bored",
              "patterns": ["I am bored", "I do not know what to do", "such a lonely day", "what a boring day"],
              "responses": ["Kako da te zabavim?", "Kako misliš?", "Hmm. Što ćemo sada?", "Idi na https://e-ucenje.unipu.hr/ i zabavi se! :)"]
             },
             {"tag": "action",
             "patterns": ["what do you do?", "what is your job?", "and what is your job?", "what do you do?", "what is up?", "what is up, are you working?"],
              "responses": ["Cijeli dan kopam po podacima.", 
                            "Nista pametno ne radim.", 
                            "Nemam nikakvih planova", 
                            "Nisam zauzet",
                            "Odgovaram na tvoja dosadna pitanja. :D"
                            "Odgovaram na često postavljena pitanja studenata, barem pokušavam. HE-HE"]
             },
             {"tag": "name",
              "patterns": ["what is your name?", "who are you?", "your name?", "name?"],
              "responses": ["Moje ime je FIPUbot.", 
                            "Ja sam FIPUbot!",
                            "Piše gore. :)"]
             },
             {"tag": "source",
              "patterns": ["who made you?", "your inventor?", "who programmed you?", "why are you exists?"],
              "responses": ["Mene je napravio student 3. godine informatike u Puli. Projekt mu je ujedno i završni rad. Imaš kontakt stranicu gdje ga možeš kontaktirati."]
             },
             {"tag": "fail",
              "patterns": [ "?", "kwekfowewo", "jnwcwoiacjoiawcjoiwa", "@~ˇ^˘°`˙´¨˝´˙`°", "...", "aaaa", "eeee", "bbbb", "ee", "eh"],
              "responses": ["Žao mi je, ali morati ćeš smisliti bolji upit!", 
                            "Probajte smisliti bolji upit!",
                            "Ne razumijem! Preformulirajte pitanje pa možda budem našao nešto. :D", 
                            "Hmm."]
             },
             {"tag": "funny",
              "patterns": [ "hahahahahaha", "you are funny", "you are humoristic"],
              "responses": ["Smijeh je lijek!", 
                            "Tko se smije, dulje živi.",
                            "Tko se zadnji smije, nije shvatio vic.", 
                            "Tko se smije u petak, plače u nedelju.",
                            "Gdje ima smijeha bude i plača."]
             },
             {"tag": "joke2",
              "patterns": [ "How much?"],
              "responses": ["28"]
             },
             {"tag": "joke2.1",
              "patterns": [ "What 28?"],
              "responses": ["A šta koliko?"]
             },
             {"tag": "lol",
              "patterns": ["lol"],
              "responses": ["Misliš, 'laugh out loud'? :)"] 
             },
             {"tag": "jokes",
              "patterns": [ "moze vic?", "joke", "tell me a joke", "jokes", "do you know some jokes?"],
              "responses": ["Pužu tri pijanca prugom. Kaže prvi: -Što su duge ove stepenice. Kaze drugi: -Nikad nećemo stići. Kaže treći: -Ne brinite se, evo lifta.", 
                            "Koja je razlika između komarca i žene? -Komarac te živcira samo ljeti.", 
                            "Idu dva policajca ulicom i jedan upadne u šaht, ovaj drugi mu pomaže da izađe, pa mu reče: - Dobro pa je bila otvorena, inače ne znam kako bih te izvukao.",
                            "Ugleda mali Perica policajca koji jede bananu pa mu kaže: - Daj griz? Policajac mu odgovori: - Ovo nije griz, tupane, to je banana.",
                            "Pita Haso Muju: - Kako se konj drži u neizvijesnosti? Mujo odgovori: - Ne znam, reci mi ti. Haso: - Reći ću ti sutra.",
                            "Mujo govori Hasi: - Moja žena je anđeo! Haso: - Blago tebi, moja je još živa!",
                            "Utrkuju se dva magarca ulicom i na pola puta jedan se izdere:- Ko zadnji magarac!",
                            "Utrkuju se dvije gljive, i kažu, bit ćemo šampinjoni",
                            "Zašto plavuša u dućan nosi pušku? Jer na vratima piše vuci.",
                            "Kad žena može da stvori muža milionera. -Samo ako je muž bio milijarder.",
                            "Kako se zove čokoladni napitak koji se smije? -Hahao",
                            "Hodaju dva krumpira ulicom, jednog pregazi auto a drugi kaže: U pireee!",
                            "Kako se zove puž koji krade? -Lopuža",
                            "Išle dvije banane ulicom i jednu pregazi autobus a druga se oguli od smjeha",
                            "Mama: Ivice, bezkoristan si, stalno se samo izležavš Ivica: pa mama, ja sam jako koristan Mama:kako? Ivica:pa služim kao loš primjer",
                            "Idu dvije čačkalice ulicom. Vide ježa, i jedna kaže: - Vidi autobus!",
                            "Kako se zove vepar sa 3 noge? - Nepar",
                            ]
             },
             {"tag": "bad-words",
              "patterns": [ "fuck you mother", "fuck you", "motherfucker", "cock", "kitten", "pussy", "ass", "shit" , "cunt", "ass", "asshole"],
              "responses": ["To nije lijepo. :)"]
             },
             {"tag": "student-restaurant",
              "patterns": [ "where can i eat for cheap", 
                           "cheap lunch", 
                           "where can i go eat", 
                           "student restorant", 
                           "student mess", 
                           "student lunch", 
                           "student canteen", 
                           "cheap lunch", 
                           "where is the canteen", 
                           "canteen location", 
                           "send me canteen location",
                           "where is the student restaurant located",],
              "responses": ["Studentska menza nalazi se na adresi:  Ul. Petra Preradovića 9a, 52100, Pula. Google lokacija: https://goo.gl/maps/iuY3zTHiT1MZ2nLA7"]
             },
             {"tag": "student-restaurant-info",
              "patterns": [ "what can I eat in the cafeteria today", "canteen menu", "manu of student restorant", "menza manu"],
              "responses": ["Današnji meni možeš potražiti na: https://www.scpu.hr/hr/prehrana/"]
             },
             # this is faq for Erasmus.
             {"tag": "erasmus-Q1",
             # 1. Koliko u programu Erasmus+ traje razdoblje mobilnosti za studij ili stručnu praksu?
              "patterns": [ "How long is the mobility period for study or professional practice in the Erasmus+ program?", "mobility period in Erasmus", "mobility duration on erasmus"],
              "responses": ["U programu Erasmus+ studenti na studiju mogu provesti od 3 do 12 mjeseci. Razdoblje stručne prakse može trajati od 2 do 12 mjeseci. U slučaju kombiniranja studija i stručne prakse najkraće trajanje mobilnosti jest 3 mjeseca, a najduže 12 mjeseci, bez obzira na raspodjelu vremena između ovih oblika mobilnosti."]
             },
             {"tag": "erasmus-Q2",
             # 2. Koje je uvjete potrebno zadovoljiti za studij ili stručnu praksu u programu Erasmus+?
              "patterns": [ "What conditions must be met for study or professional practice in the Erasmus+ program?", "conditions for study in the Erasmus program", "conditions for practice in the Erasmus program", "how to go on Erasmus"],
              "responses": ["Da biste studirali ili se stručno usavršavali u inozemstvu, morate studirati na visokom učilištu u programu preddiplomskoga, diplomskoga ili poslijediplomskog studija nakon kojeg stječete zvanje prvostupnika (bacc.), magistra odnosno magistra struke (mag.) ili doktora znanosti. Vaše matično visoko učilište treba biti u zemlji koja sudjeluje u programu Erasmus+ vezanom za visoko obrazovanje, a programske su zemlje u akademskoj godini 2014./2015. sve zemlje članice EU-a te Island, Lihtenštajn, Norveška, Turska i Makedonija. Od akademske će godine 2015./2016. u Erasmus+ studentskoj mobilnosti moći sudjelovati istudenti iz ustanova u partnerskim zemljama (napomena: stručna praksa između partnerskih i programskih zemalja neće se moći ostvariti u 2015. godini). Ako se vaše visoko učilište nalazi u programskoj zemlji, treba biti nositelj Erasmus povelje za visoko obrazovanje (Erasmus Charter for Higher Education - ECHE) kojom se jamči kvaliteta provedbe aktivnosti mobilnosti za sve sudionike. Na mrežnim stranicama vaše ustanove možete provjeriti je li nositeljica ECHE-a, a potpuni popis ustanova nositeljica Povelje možete pronaći na poveznici: 'http://eacea.ec.europa.eu/funding/2014/call_he_charter_en.php'. Vaša matična ustanova određuje kriterije za odabir studenata koji će pohađati studij ili obavljati stručnu praksu u inozemstvu (za više informacija molimo upitajte: kriterij za erasmus)"]
             },
             {"tag": "erasmus-Q3",
             # 3. . Mogu li studenti u programu Erasmus+ tijekom studija više puta ostvariti mobilnost?
              "patterns": [ "Can students in the Erasmus+ program achieve mobility several times during their studies?", "multiple mobility opportunities in Erasmus", "mobility erasmus"],
              "responses": ["Erasmus+ studentima omogućuje studij ili stručnu praksu u ukupnom trajanju do 12 mjeseci za svaku razinu studija (preddiplomska, diplomska, poslijediplomska). Mobilnost je tijekom studija moguće ostvariti više puta - važno je poštovati uvjet od najviše 12 mjeseci po svakoj razini studija. Primjerice, na istoj se razini studija možete prijaviti za studij u trajanju do 6 mjeseci, a zatim i za stručnu praksu u trajanju do 6 mjeseci (ili npr. 4 + 8 mjeseci). Studenti koji pohađaju integrirane studije, kao što je npr. medicina, mobilnost mogu ostvariti u ukupnom trajanju do 24 mjeseca.Navedeni maksimum po razini studija odnosi se i na mobilnosti ostvarene u Programu za cjeloživotno učenje (LLP). Ako je primjerice student integriranih studija već sudjelovao u programu mobilnosti u okviru LLP-a, npr. u trajanju od 8 mjeseci, u okviru programa Erasmus+ tijekom studija može otići na mobilnost u trajanju od 16 mjeseci."]
             },
             {"tag": "erasmus-Q4",
             # 4. Je li moguće otići na studij i obaviti stručnu praksu u okviru iste mobilnosti?
              "patterns": [ "Is it possible to go to study and do an internship within the same mobility?", "study and internship abroad"],
              "responses": ["Odlazak na studij i stručnu praksu u inozemstvu u sklopu iste mobilnosti mogućnost je koju nudi program Erasmus+. U ovom je slučaju najkraće trajanje mobilnosti 3 mjeseca, a najduže 12 mjeseci, bez obzira na raspodjelu vremena između ostvarenih mobilnosti."]
             },
             {"tag": "erasmus-Q5",
             # 5. Može li student koji je u Programu za cjeloživotno učenje (potprogram Erasmus) već ostvario mobilnost sudjelovati u programu Erasmus+ te otići na studij ili stručnu praksu?
             "patterns": ["Can a student who has already achieved mobility in the Lifelong Learning Program (Erasmus sub-program) participate in the Erasmus+ program and go to study or professional practice?"],
              "responses": ["Erasmus+ studentima omogućuje studij ili stručnu praksu u inozemstvu pod uvjetom da najduže trajanje mobilnosti tijekom jedne razine studija bude do 12 mjeseci. Ako ste u okviru Programa za cjeloživotno učenje (LLP) ostvarili maksimum od 12 mjeseci mobilnosti na jednoj razini studija, za mobilnost u programu Erasmus+ trebat ćete pričekati sljedeću razinu studija. Ako vam je pak mobilnost u programu LLP na trenutačnoj razini studija bila manja od 12 mjeseci, na istoj ćete razini studija u programu Erasmus+ moći ostvariti mobilnost do navedenoga najdužeg trajanja. Primjerice, ako ste u LLP-u tijekom preddiplomske razine na mobilnosti proveli 4 mjeseca, na istoj ćete razini studija u programu Erasmus+ moći ostvariti još 8 mjeseci (za studij ili stručnu praksu). Ako vam pak slijedi diplomska ili poslijediplomska razina studija, možete se prijavljivati za mobilnosti u trajanju do 12 mjeseci (nova razina studija). Sudjelovanje u drugim potprogramima LLP-a (npr. Leonardo) ili drugim programima kao što je Mladi na djelu (YiA) ne uzima se u obzir. Podsjećamo vas da uvijek trebate kontaktirati vašu matičnu visoku ustanovu (Erasmus koordinatore) jer je ona odgovorna za izbor sudionika te može postaviti dodatne uvjete na natječajima (primjerice, može dati prednost studentima koji još nisu ostvarili Erasmus mobilnost)."]
             },
            {"tag": "erasmus-Q6",
             # 6. Ako je student tijekom Programa za cjeloživotno učenje (LLP) u potprogramu Leonardo boravio na stručnoj praksi, može li ići na studij ili stručnu praksu u okviru programa Erasmus+?
              "patterns": [ "If a student had a professional internship during the Lifelong Learning Program (LLP) in the Leonardo sub-programme, can he go on a study or professional internship under the Erasmus+ program?"],
              "responses": ["Sudjelovanje u drugim potprogramima LLP-a (npr. Leonardo) ili drugim programima kao što je Mladi na djelu (YiA) ne uzima se u obzir pri uvjetima sudjelovanja u mobilnostima vezanima za visoko obrazovanje. Student se, dakle, može prijaviti za mobilnosti u okviru programa Erasmus+."]
             },
            {"tag": "erasmus-Q7",
             # 7. Može li student koji je u programu Mladi na djelu (YiA) volontirao preko Europske volonterske službe (EVS) otići na studij ili stručnu praksu u programu Erasmus+?
              "patterns": ["Can a student who volunteered in the Youth in Action (YiA) program through the European Voluntary Service (EVS) go to study or professional practice in the Erasmus+ program?"],
              "responses": ["Budući da sudjelovanje u programu Mladi na djelu nije relevantno za uvjete sudjelovanja u mobilnostima vezanima za visoko obrazovanje, moguća je prijava za aktivnosti studija ili stručne prakse u programu Erasmus+."]
             },
            {"tag": "erasmus-Q8",
             # 8. Kako se u programu Erasmus+ prijavljuje za studij ili stručnu praksu u inozemstvu?
              "patterns": [ "How to apply for study or professional practice abroad in the Erasmus+ program", "practice abroad erasmus", "practice for erasmus"],
              "responses": ["Studenti se prijavljuju preko svojih visokih učilišta bez obzira na vrstu mobilnosti za koju su zainteresirani. Ured za međunarodnu suradnju u matičnom visokom učilištu nudi informacije o uvjetima sudjelovanja u Erasmus+ mobilnostima - detalji postupka odabira studenata, potrebni dokumenti, popis učilišta na kojima studenti mogu ostvariti mobilnost te uvjeti koje studenti moraju poštovati tijekom boravka na inozemnoj ustanovi."]
             },
            {"tag": "erasmus-Q9",
             # 9. Koji su kriteriji odabira za sudjelovanje u programu Erasmus+?
              "patterns": [ "What are the selection criteria for participation in the Erasmus+ program?", "criterion for Erasmus", "how to go to Erasmus"],
              "responses": ["Da biste sudjelovali u aktivnostima mobilnosti vezanima za visoko obrazovanje unutar programa Erasmus+, morate zadovoljiti kriterije sudjelovanja navedene pod 2. pitanjem (Koje je uvjete potrebno zadovoljiti za studij ili stručnu praksu u programu Erasmus+?). Osim toga, potrebno je zadovoljiti uvjete koje odredi matično visoko učilište. Postupak odabira studenata i dodjeljivanja financijske potpore mora biti transparentan, dosljedan i potkrijepljen dokumentima te s njime moraju biti upoznati svi uključeni. Vaše matično visoko učilište može kao uvjet u izbornom postupku uvrstiti akademski uspjeh, prethodno iskustvo mobilnosti, motivaciju, iskustvo u zemlji u koju se odlazi na mobilnost (npr. povratak u zemlju podrijetla) itd. Kriteriji za odabir svakako moraju biti javni. Više informacija možete potražiti na mrežnim stranicama vašega visokog učilišta ili se obratiti Uredu za međunarodnu suradnju na vašem učilištu."]
             },
            {"tag": "erasmus-Q10",
             # 10. Što slijedi nakon što je student izabran za studij ili stručnu praksu u programu Erasmus+?
              "patterns": [ "What happens after a student is selected for study or internship in the Erasmus+ program?", "after a student is selected for study or internship in the Erasmus+ program", "selected for Erasmus"],
              "responses": ["Nakon što je student izabran za Erasmus+ mobilnost, matično visoko učilište treba mu dati Erasmus+ studentsku povelju (Erasmus+ student charter) u kojoj su navedena sva studentska prava i obveze koje ima tijekom boravka na mobilnosti u inozemstvu te su objašnjeni koraci koje student mora poduzeti prije, tijekom i poslije mobilnosti. Studenti koji na mobilnosti odlaze poslije listopada 2014., a jezik kojim će se tijekom mobilnosti trebati služiti jest engleski, francuski, njemački, talijanski, španjolski ili nizozemski (više će se jezika dodati od ak. god. 2015./2016.), pisat će online test jezične procjene (osim ako im je jezik mobilnosti materinski). Pristup rezultatu ove procjene imat će student, njegovo matično visoko učilište (ustanova primatelj neće imati pristup rezultatima testa online jezične procjene) te Europska komisija. S obzirom na to da je student već izabran, rezultati jezične procjene neće utjecati na odluku o njegovu odlasku na mobilnost. Kako bi studentima pomoglo u pripremi za aktivnost mobilnosti, matično im visoko učilište može, ovisno o njihovoj jezičnoj razini, ponuditi besplatan online jezični tečaj na engleskom, njemačkom, talijanskom, španjolskom ili nizozemskom jeziku. Na kraju razdoblja mobilnosti u inozemstvu studenti će pisati drugi test jezične procjene na temelju kojega će doznati koliko su unaprijedili svoje jezične vještine. Jednako tako, na temelju te će jezične procjene Europska komisija dobiti informacije o tome koliko je sudjelovanje u programu Erasmus+ utjecalo na jezične vještine studenata."]
             },
            {"tag": "erasmus-Q11",
             # 11. Može li u programu Erasmus+ student boraviti na studiju ili stručnoj praksi u zemlji svog podrijetla ako pritom studira u nekoj drugoj zemlji?
              "patterns": ["Can a student in the Erasmus+ program stay for a study or professional internship in his country of origin if he studies in another country?"],
              "responses": ["Aktivnost Erasmus+ mobilnosti mora se ostvariti u programskoj ili partnerskoj zemlji različitoj od zemlje u kojoj student studira. Moguće je da Erasmus+ student ode na mobilnost u zemlju svog podrijetla ako to nije zemlja u kojoj živi za vrijeme studiranja. Kriterije odabira, međutim, određuju visoka učilišta iz programskih zemalja koja u izbornom postupku mogu odrediti da će se prednost davati studentima koji se prijavljuju za mobilnost u zemlju iz koje nisu podrijetlom. U svakom slučaju kriteriji za odabir moraju biti pravedni i transparentni te se iznos financijske potpore ne smije određivati s obzirom na nacionalnost."]
             },
            {"tag": "erasmus-Q12",
             # 12. Gdje studenti mogu otići na studij ili stručnu praksu?
              "patterns": [ "Where can students go to study or professional practice?", "where can I go to study or professional practice", "erasmus study or professional practice", "where all can go with Erasmus"],
              "responses": ["Ustanova ili organizacija primatelj moraju se nalaziti u jednoj od Erasmus+ programskih zemalja. U ak. god. 2014./2015. programske su zemlje sve zemlje članice EU-a te Island, Lihtenštajn, Norveška, Turska i Makedonija. Od akademske će godine 2015./2016. biti moguć studij u partnerskim zemljama, a od ak. god. 2017./2018. u tim će se zemljama moći obavljati stručna praksa. Popis partnerskih zemalja dostupan je u Vodiču kroz program Erasmus+ http://ec.europa.eu/programmes/erasmus-plus/documents/erasmus-plus-programmeguide_en.pdf. Točnije, studenti će moći studirati u ustanovama koje s njihovim visokim učilištem sklope međuinstitucijski sporazum. Jednako tako, ustanove u programskim zemljama morat će biti nositeljice Erasmus povelje za visoko obrazovanje. Studij u ustanovi koja se nalazi u nekoj od partnerskih zemalja bit će moguć ako je matična ustanova studenta zatražila i primila Erasmus+ financijska sredstava."]
             },
            {"tag": "erasmus-Q13",
             # 13. Jezična priprema
              "patterns": [ "Language preparation", "language preparation for Erasmus", "language for going to Erasmus", "language for going abroad to study", "what language do I speak at Erasmus"],
              "responses": ["Vaše se matično visoko učilište obvezalo osigurati vam potrebnu podršku za jezičnu pripremu. Online jezična podrška postupno će se primjenjivati u projektnom ciklusu programa Erasmus+ (2014. - 2020.), uključujući online jezične tečajeve koji će biti dostupni nekim studentima koji će se tijekom razdoblja mobilnosti trebati koristiti engleskim, njemačkim, francuskim, talijanskim, španjolskim i nizozemskim jezikom. Od ak. god. 2015./2016. dodavat će se više jezika. Studentima koji odlaze na studij ili stručnu praksu na nekom drugom jeziku (osim spomenutih šest) matično visoko učilište može ponuditi jezičnu potporu preko drugačijih jezičnih tečajeva. Za više informacija molimo pročitajte odgovor na 10. pitanje (Što slijedi nakon što je student izabran za studij ili stručnu praksu u programu Erasmus+?)."]
             },
            {"tag": "erasmus-Q14",
             # 14. Može li student zatražiti Erasmus+ financijsku potporu za obavljanje stručne prakse u inozemstvu?
              "patterns": [ "Can a student request Erasmus+ financial support for professional practice abroad?", "erasmus+ financial support", "erasmus scholarship", "financial support for practice abroad"],
              "responses": ["Program Erasmus+ studentima omogućuje studiranje ili osposobljavanje u inozemstvu u trajanju do 12 mjeseci na svakoj razini studija, bez obzira na broj i oblik mobilnosti (studij ili stručna praksa). Jednako tako, studenti se za mobilnost mogu prijavljivati prije stjecanja diplome, a zatim je ostvariti u godini nakon što diplomiraju. Najkraće moguće trajanje stručne prakse jest 2 mjeseca, a najduže 12 mjeseci. Europska komisija nije zadužena za izravno upravljanje provedbom projekata mobilnosti za studente. Za dodatne informacije o Erasmus+ stručnoj praksi, rokovima i uvjetima prijave molimo obratite se Uredu za međunarodnu suradnju na vašemu matičnom visokom učilištu. Nekoliko je online platformi na kojima studenti mogu pronaći ponude za stručnu praksu: - JOE+ https://leonet.joeplus.org/en/ - platforma portala LEO-NET za razmjenu ponuda za posao, posebno namijenjena promidžbi visoke kvalitete stručnih praksi u okviru potprograma LLP-a Leonardo da Vinci i Erasmus - Erasmusov je tim osmislio portal na kojem se mogu objavljivati ponude za stručnu praksu: http://erasmus.com/en/."]
             },
            {"tag": "erasmus-Q15",
             # 15. Ako student koji već studira ili obavlja stručnu praksu u inozemstvu želi produžiti razdoblje mobilnosti, što treba učiniti?
              "patterns": [ "If a student who is already studying or doing professional practice abroad wants to extend the mobility period, what should be done?", "a student who is already studying abroad wants to extend the mobility period"],
              "responses": ["Produženje trajanja mobilnosti u inozemstvu moguće je zatražiti najmanje mjesec dana prije očekivanoga posljednjeg dana mobilnosti navedenog u Sporazumu o učenju (Learning Agreement). Naglašavamo kako ukupno trajanje mobilnosti, uključujući prethodno sudjelovanje u Programu za cjeloživotno učenje (LLP), ne smije biti duže od 12 mjeseci po razini studija. Ovo se vremensko ograničenje odnosi i na razdoblje provedeno u inozemstvu bez primanja financijske potpore iz EU fondova. Ako mobilnost studenta nije trajala 12 mjeseci, matična ustanova i ustanova primatelj mogu se složiti i produljiti mu razdoblje mobilnosti u inozemstvu. Ako je student primao financijsku potporu, njegovo visoko učilište može produženje razdoblja mobilnosti smatrati razdobljem „zero-granta“ u slučaju da je već potrošilo sva sredstva odobrena proračunom ili može napisati dodatak ugovoru o financijskoj potpori tako da uključuje i produženo razdoblje mobilnosti u inozemstvu. U svakom će slučaju biti potrebno dodati izmjene Sporazumu o učenju te će student trebati primiti e-mail u kojem će te izmjene potvrditi i matično visoko učilište, i ustanova primatelj."]
             },
            {"tag": "erasmus-Q16",
             # 16. Mogu li studenti uz Erasmus+ financijsku potporu primati i druge stipendije?
              "patterns": [ "Can students receive other scholarships in addition to Erasmus+ financial support?", "receiving a scholarship other than Erasmus financial support", "other scholarship in addition to Erasmus scholarship"],
              "responses": ["Tijekom boravka na mobilnosti u inozemstvu studenti uz Erasmus+ potporu i dalje mogu primati stipendije ili drugu financijsku potporu nacionalnih, regionalnih ili lokalnih tijela. Ako je riječ o stručnoj praksi u inozemstvu, studenti uz Erasmus+ potporu mogu primati i bilo kakvu naknadu koju im daje organizacija primatelj (npr. plaća, smještaj, topli obrok). Tijekom mobilnosti studenti mogu raditi sa skraćenim radnim vremenom te uz Erasmus+ potporu primati i naknadu za taj posao sve dok uredno izvršavaju ugovorne obveze programa mobilnosti."]
             },
            {"tag": "erasmus-Q17",
             # 17. Može li matično visoko učilište studentima smanjiti financijsku potporu ili ih zatražiti djelomični/potpuni povrat Erasmus+ financijske potpore?
              "patterns": [ "Can the home higher education institution reduce financial support for students or ask them for a partial/full refund of Erasmus+ financial support?", "partial refund of Erasmus+ financial support"],
              "responses": ["Ako studenti ne izvrše obveze navedene u ugovoru o financijskoj potpori, morat će izvršiti djelomični ili potpuni povrat dodijeljene financijske potpore. Iznimno, ako su studenti u obavljanju ugovornih obveza spriječeni višom silom (force majeure, npr. nepredvidljiva iznimna situacija ili događaj izvan kontrole sudionika koji nije povezan s njegovom/njezinom greškom ili nemarom), u tom slučaju mogu primiti ugovorom određenu financijsku potporu koja odgovara stvarnom trajanju razdoblja mobilnosti (čl. 2.2. ugovora o financijskoj potpori), a ostala će sredstva morati vratiti (osim ako je drugačije dogovoreno s ustanovom pošiljateljem). Savjetujemo da pozorno pročitate ugovor o financijskoj potpori prije potpisivanja te da o njemu vodite brigu tijekom boravka na mobilnosti. Primjerice, uvjet za posljednju isplatu financijske potpore koja je predviđena na kraju mobilnosti može biti ispunjavanje online jezične procjene pa ako ne izvršite ovu obvezu, možda ćete morati izvršiti djelomični ili potpuni povrat dobivenih sredstava."]
             },
            {"tag": "erasmus-Q18",
             # 18. Komu se za pomoć mogu obratiti studenti koji su završili s boravkom/stručnom praksom u inozemstvu i imaju problema s predajom EU online izvješća?
              "patterns": [ "To whom can students who have completed their stay/practice abroad and have problems submitting an EU online report turn for help?"],
              "responses": ["U slučaju problema s predajom EU online izvješća, molimo kontaktirajte vaše matično visoko učilište. Ondje će moći vidjeti status vašeg izvješća te će vam, bude li potrebno, poslati novu poveznicu na izvješće. Za dodatne informacije molimo obratite se nacionalnoj agenciji koja provodi Erasmus+ programe u vašoj zemlji (Agencija za mobilnost i programe EU)."]
             },
            {"tag": "erasmus-Q19",
             # 19. Može li u programu Erasmus+ student koji završava studij otići na stručnu praksu u inozemstvo?
              "patterns": [ "In the Erasmus+ program, can a student who is completing his studies go on an internship abroad?", "can a student who is graduating go on an internship abroad"],
              "responses": ["Riječ je o novoj mogućnosti koju program Erasmus+ nudi nedavno diplomiranim studentima. Uvjet je da tijekom zadnje godine studija (dok još imaju status studenta) budu izabrani na natječaju na matičnom visokom učilištu te da stručnu praksu obave u roku od 12 mjeseci od dana diplomiranja."]
             },
            {"tag": "erasmus-Q20",
             # 20. Mogu li u studenti doktorskih studija dobiti financijsku potporu za istraživanje na inozemnoj instituciji?
              "patterns": [ "Can PhD students receive financial support for research at a foreign institution?", "financial support for research at a foreign institution"],
              "responses": ["U okviru programa Erasmus+ studenti visokih učilišta iz programskih zemalja mogu otići na studij ili stručnu praksu u inozemstvo više puta pod uvjetom da mobilnost na svakoj razini studija traje najviše do 12 mjeseci. Dakle, za doktorsku razinu studija mogu primiti financijsku potporu za mobilnost do 12 mjeseci. Ako je posrijedi Erasmus+ stručna praksa, studenti doktorske razine studija mogu se za mobilnosti prijaviti tijekom posljednje godine studija te zatim stručnu praksu obaviti u roku od jedne godine od dana diplomiranja. Natječaj za dodjelu financijske potpore raspisuju visoka učilišta te određuju uvjete za prijavu i kriterije odabira sudionika, dakle studenti se na natječaj prijavljuju preko matičnih visokih učilišta. Studenti doktorskih studija koji dio studija žele pohađati u inozemstvu također mogu primiti financijsku potporu preko aktivnosti Marie Sklodowska-Curie u okviru programa Obzor 2020. Aktivnosti Marie Sklodowska-Curie (http://ec.europa.eu/research/mariecurieactions/aboutmsca/actions/index_en.htm) pomažu istraživačima preko različitih aktivnosti objašnjenih u vodiču Quick-Guide to Marie Curie Actions fellowships (http://ec.europa.eu/research/mariecurieactions/about-mca/quick-guide/index_en.htm). U okviru Innovative Training Networks organizacije poput sveučilišta, istraživačkih centara ili tvrtki nude istraživačku mrežu za osposobljavanje i pojedinci se mogu prijaviti za mjesta u tim mrežama objavljena na portalu Euraxess (http://ec.europa.eu/euraxess/). Nacionalne kontaktne točke (http://ec.europa.eu/euraxess/) mogu pružiti dodatne informacije. Do 2017. će godine Erasmus Mundus združeni doktorski studiji odabrani u prethodnoj generaciji programa nastaviti nuditi stipendije kandidatima koji u inozemstvu žele provesti puni doktorski studij (3 – 4 godine). Više informacija o kolegijima i načinu prijave možete pronaći na poveznici: http://eacea.ec.europa.eu/erasmus_mundus/results_compendia/selected_projects_action_ 1_joint_doctorates_en.php#fragment-1."]
             },
            {"tag": "erasmus-Q21",
             # 21. Gdje se može pronaći više informacija o studijskim programima u Europi vezanima za određeni studijski smjer?
              "patterns": [ "Where can I find more information about study programs in Europe related to a specific field of study?", "study programs in Europe"],
              "responses": ["Mrežna stranica StudyPortals (http://www.studyportals.eu/about/) međunarodna je platforma s pomoću koje možete pristupiti različitim portalima i potražiti preddiplomske, diplomske i poslijediplomske programe s obzirom na smjer koji vas zanima. Ova mrežna stranica uključuje i portal za stipendije (http://www.scholarshipportal.eu/). Program Erasmus+ uključuje i Erasmus Mundus združene diplomske studije koji nude posebne EU stipendije izvrsnim studentima te će do 2017. godine Erasmus Mundus združeni doktorski studiji odabrani u prethodnoj generaciji programa nastaviti nuditi stipendije kandidatima koji žele puni doktorski studij provesti u inozemstvu (3 - 4 godine). Za više informacija molimo pročitajte odgovore na 20. i 23. pitanje"]
             },
            {"tag": "erasmus-Q22",
             # 22. Može li program Erasmus+ pružiti financijsku potporu za preddiplomski/diplomski/poslijediplomski studij u inozemstvu?
              "patterns": [ "Can the Erasmus+ program provide financial support for undergraduate/graduate/postgraduate studies abroad?"],
              "responses": ["Erasmus+ podržava strukturiranu suradnju među visokim učilištima u okviru koje studenti mogu primati financijsku pomoć za razdoblja koja provedu na mobilnosti, dakle mogu primati potporu za studij (koji može trajati od 3 do 12 mjeseci) te potporu za stručnu praksu (od 2 do 12 mjeseci), no unutar programa Erasmus+ u inozemstvu ne mogu pohađati puni preddiplomski ili poslijediplomski studijski program. Erasmus+ pruža dodatne mogućnosti za upis cjelovitoga diplomskoga studijskog programa u inozemstvu preko stipendija za Erasmus Mundus združene diplomske studije i preko Erasmus+ zajmova za studente diplomskih studija. Za više informacija molimo pročitajte odgovore na 24. i 29. pitanje. Korisne informacije možete pronaći i na portalu za stipendije http://www.scholarshipportal.eu/ na kojem možete pretraživati ponudu stipendija ovisno o zemlji podrijetla, razini i smjeru studija te zemlji u kojoj biste željeli studirati."]
             },
            {"tag": "erasmus-Q23",
             # 23. Što su Erasmus Mundus združeni diplomski studiji?
              "patterns": [ "What are Erasmus Mundus joint graduate studies?", "erasmus joint graduate studies"],
              "responses": ["Riječ je o integriranome međunarodnom studijskom programu koji nosi 60, 90 ili 120 ECTS bodova (razdoblje od 12 do 24 mjeseci). Provode ga međunarodni konzorcij visokih učilišta iz različitih zemalja te, gdje je od važnosti za projekt, drugi partneri s posebnim znanjima i zanimanjem za područja studija ili profesionalno područje kojim se združeni diplomski studiji bave. Konzorcij se mora sastojati od najmanje triju visokih učilišta iz programskih zemalja, a među članovima konzorcija mogu se naći i ustanove iz programskih i partnerskih zemalja. Erasmus Mundus združeni diplomski studiji moraju se provoditi u najmanje dvije programske zemlje, a dio se može provesti i u ustanovi iz partnerske zemlje. Izvrsnim studentima iz cijelog svijeta Erasmus Mundus združeni diplomski studiji omogućuju posebne EU stipendije kojima pokrivaju životne i putne troškove te troškove sudjelovanja tijekom trajanja cijeloga diplomskog studija. Za više informacija molimo pročitajte odgovor na 26. pitanje."]
             },
            {"tag": "erasmus-Q24",
             # 24. Koji su uvjeti za dobivanje stipendije za Erasmus Mundus združene diplomske studije?
              "patterns": [ "What are the conditions for receiving a scholarship for Erasmus Mundus joint graduate studies?"],
              "responses": ["Ove stipendije mogu primati jedino studenti koji su u okviru programa Erasmus+ izabrani za sudjelovanje u Erasmus Mundus združenim diplomskim studijima, no mogu se uključiti i studenti koji se sami financiraju. Prije prijavljivanja konzorciju prema vlastitom izboru treba provjeriti jesu li zadovoljeni sljedeći uvjeti. - Student mora imati diplomu barem preddiplomskog studija ili pokazati razinu znanja koju priznaju nacionalno zakonodavstvo i zemlje koje dodjeljuju takvu kvalifikaciju. Ovaj uvjet nužno mora biti ispunjen pri upisu. Neki konzorciji Erasmus Mundus združenih diplomskih studija mogu odlučiti prihvatiti prijave za stipendiju studenata koji su na posljednjoj godini prve razine studija. - Studenti se godišnje za stipendiju mogu prijaviti najviše trima konzorcijima. - Ako je student već primio stipendiju za Erasmus Mundus diplomski studij ili Erasmus Mundus združene doktorske studije, više se ne može prijavljivati za stipendiju ovog programa. Za sudjelovanje u Erasmus Mundus združenim diplomskim studijima svake se godine odabire 13 do 20 studenata, a najmanje se 75 % stipendija izdvaja za kandidate iz partnerskih zemalja. Za više informacija na razini nacionalne agencije možete se javiti na adresu jasmina.skocilic@mobilnost.hr (bilaterala@mobilnost.hr)."]
             },
            {"tag": "erasmus-Q25",
             # 25. Za koliko se programa Erasmus Mundus združenih diplomskih studija studenti mogu prijaviti?
              "patterns": [ "How many Erasmus Mundus joint degree programs can students apply for?"],
              "responses": ["Studenti se godišnje mogu prijaviti za najviše tri programa Erasmus Mundus združenih diplomskih studija."]
             },
            {"tag": "erasmus-Q26",
             # 26. Gdje se u okviru programa Erasmus+ mogu pronaći ponude za Erasmus Mundus združene diplomske studije?
              "patterns": [ "Where can I find offers for Erasmus Mundus joint graduate studies within the Erasmus+ program?"],
              "responses": ["Popis svih Erasmus Mundus združenih diplomskih studija možete naći na ovoj poveznici: http://eacea.ec.europa.eu/erasmus_mundus/results_compendia/selected_projects_action_1_master_courses_en.php. Svake se godine tijekom ljeta popisu dodaje novi niz izabranih (ili ponovno izabranih) združenih diplomskih studija. Prijave za stipendije za ove programe primaju se u zadnjem kvartalu te godine za studente koji s programom počinju u rujnu/listopadu sljedeće godine. Ovaj popis uključuje i broj Erasmus Mundus diplomskih studija izabranih prije 2014. Neki će od njih nastaviti izabirati studente do 2017."]
             },
            {"tag": "erasmus-Q27",
             # 27. Kako studenti mogu biti sigurni da će im kvalifikacija stečena završetkom Erasmus Mundus združenoga diplomskog studija biti priznata u zemlji koja nije uključena u konzorcij zemalja u kojima studiraju ili su studirali?
              "patterns": [ "How can students be sure that the qualification obtained by completing an Erasmus Mundus joint graduate study will be recognized in a country that is not included in the consortium of countries where they are studying or have studied?"],
              "responses": ["Program Erasmus+ zahtijeva da svi diplomirani studenti steknu barem dvojnu kvalifikaciju (double degree), odnosno dvije diplome službeno priznate u zemljama koje dodjeljuju te kvalifikacije. O automatskom priznavanju kvalifikacije stečene u drugoj zemlji u Europi ili izvan Europe ne odlučuje Europska unija ili Europska komisija, već o tome odlučuje sama zemlja (obično na temelju bilateralnog sporazuma između dviju zemalja). Načelno se na temelju Lisabonske konvencije o priznavanju visokoobrazovnih kvalifikacija na području Europe priznaju kvalifikacije stečene unutar Europe. U specifičnim bi slučajevima najbolje bilo pitanje uputiti odgovarajućim nadležnim tijelima zemlje o kojoj je riječ te pritom navesti službeni naziv kvalifikacije iz Erasmus Mundus združenih diplomskih studija o kojima je riječ. Nadležna tijela možete potražiti na ovoj poveznici: http://www.enic-naric.net/."]
             },
            {"tag": "erasmus-Q28",
             # 28. Može li student u okviru Erasmus Mundus združenih diplomskih studija studirati/provesti istraživanje/pripremiti dio diplomskog rada u ustanovi ili u zemlji koja ne pripada konzorciju? 
              "patterns": [ "Can a student within the framework of Erasmus Mundus joint graduate studies study/conduct research/prepare a part of the thesis in an institution or in a country that does not belong to the consortium?"],
              "responses": ["U načelu, razdoblje studija ili istraživanja trebalo bi provesti u ustanovi koja pripada konzorciju (kao punopravni partner ili, što je često kod stručnih praksi u poduzećima, pridruženi partner). Razdoblje studiranja ili istraživanja izvan konzorcija trebalo bi smatrati iznimkom. Ako se takva iznimka pojavi, konzorcij treba opravdati važnost mobilnosti i dodanu vrijednost za studij. Osim toga, konzorcij mora objasniti koja je u ovom slučaju uloga ustanove primatelja te potvrditi da ustanova prihvaća svoju ulogu. Barem jedan od partnera u konzorciju koji će priznavati razdoblje studiranja/istraživanja izvan konzorcija mora nadzirati i ocjenjivati mobilnost studenta. Studenti koji već primaju stipendiju Erasmus Mundus združenih diplomskih studija u okviru programa Erasmus+ ne mogu ostvariti takvu aktivnost mobilnosti u inozemstvu. 29. Što su Erasmus+ zajmovi za studente diplomskih studija? Erasmus+ zajmovi za studente diplomskih studija zajmovi su s povoljnim uvjetima otplate namijenjeni studentima koji studiraju u europskoj zemlji u kojoj nemaju stalno prebivalište i u kojoj nisu stekli uvjete za pristup diplomskim programima. Da bi ostvarili pravo na zajam, studenti moraju živjeti u jednoj od Erasmus+ programskih zemalja. Za jednogodišnji diplomski program zajam iznosi najviše 12 000 eura, a za dvogodišnji 18 000 eura. Prijavu za zajam studenti šalju nacionalnim bankama koje sudjeluju u programu ili agencijama za studentske zajmove. Molimo pročitajte odgovor na 30. pitanje (Gdje se može pronaći popis nacionalnih banaka ili agencija za studentske zajmove koje sudjeluju u Erasmus+ zajmovima za studente diplomskih studija?). Za više informacija molimo posjetite mrežnu stranicu: http://ec.europa.eu/education/opportunities/higher-education/masters-loans_en.htm."]
             },
            {"tag": "erasmus-Q29",
             # 29. Što su Erasmus+ zajmovi za studente diplomskih studija?
              "patterns": [ "What are Erasmus+ loans for graduate students?", "erasmus+ loans"],
              "responses": ["U načelu, razdoblje studija ili istraživanja trebalo bi provesti u ustanovi koja pripada konzorciju (kao punopravni partner ili, što je često kod stručnih praksi u poduzećima, pridruženi partner). Razdoblje studiranja ili istraživanja izvan konzorcija trebalo bi smatrati iznimkom. Ako se takva iznimka pojavi, konzorcij treba opravdati važnost mobilnosti i dodanu vrijednost za studij. Osim toga, konzorcij mora objasniti koja je u ovom slučaju uloga ustanove primatelja te potvrditi da ustanova prihvaća svoju ulogu. Barem jedan od partnera u konzorciju koji će priznavati razdoblje studiranja/istraživanja izvan konzorcija mora nadzirati i ocjenjivati mobilnost studenta. Studenti koji već primaju stipendiju Erasmus Mundus združenih diplomskih studija u okviru programa Erasmus+ ne mogu ostvariti takvu aktivnost mobilnosti u inozemstvu. 29. Što su Erasmus+ zajmovi za studente diplomskih studija? Erasmus+ zajmovi za studente diplomskih studija zajmovi su s povoljnim uvjetima otplate namijenjeni studentima koji studiraju u europskoj zemlji u kojoj nemaju stalno prebivalište i u kojoj nisu stekli uvjete za pristup diplomskim programima. Da bi ostvarili pravo na zajam, studenti moraju živjeti u jednoj od Erasmus+ programskih zemalja. Za jednogodišnji diplomski program zajam iznosi najviše 12 000 eura, a za dvogodišnji 18 000 eura. Prijavu za zajam studenti šalju nacionalnim bankama koje sudjeluju u programu ili agencijama za studentske zajmove. Molimo pročitajte odgovor na 30. pitanje (Gdje se može pronaći popis nacionalnih banaka ili agencija za studentske zajmove koje sudjeluju u Erasmus+ zajmovima za studente diplomskih studija?). Za više informacija molimo posjetite mrežnu stranicu: http://ec.europa.eu/education/opportunities/higher-education/masters-loans_en.htm."]
             },
            {"tag": "erasmus-Q30",
             # 30. Gdje se može pronaći popis nacionalnih banaka ili agencija za studentske zajmove koje sudjeluju u Erasmus+ zajmovima za studente diplomskih studija?
              "patterns": [ "Where can I find a list of national banks or student loan agencies participating in Erasmus+ graduate student loans?"],
              "responses": ["Erasmus+ zajmovi za studente diplomskih studija zajmovi su s povoljnim uvjetima otplate namijenjeni studentima koji studiraju u europskoj zemlji u kojoj nemaju stalno prebivalište i u kojoj nisu stekli uvjete za pristup diplomskim programima. Da bi ostvarili pravo na zajam, studenti moraju živjeti u jednoj od Erasmus+ programskih zemalja. Za jednogodišnji diplomski program zajam iznosi najviše 12 000 eura, a za dvogodišnji 18 000 eura. Prijavu za zajam studenti šalju nacionalnim bankama koje sudjeluju u programu ili agencijama za studentske zajmove. Molimo pročitajte odgovor na 30. pitanje (Gdje se može pronaći popis nacionalnih banaka ili agencija za studentske zajmove koje sudjeluju u Erasmus+ zajmovima za studente diplomskih studija?). Za više informacija molimo posjetite mrežnu stranicu: http://ec.europa.eu/education/opportunities/higher-education/masters-loans_en.htm."]
             },
            {"tag": "erasmus-Q31",
             # 31. Erasmus za mlade poduzetnike
              "patterns": [ "Erasmus for young entrepreneurs", "erasmus for young businessmen", "erasmus entrepreneurship"],
              "responses": ["Erasmus za mlade poduzetnike međunarodni je program razmjene koji mladim poduzetnicima pruža priliku da uče od iskusnih poduzetnika u zemljama koje sudjeluju u programu. Više informacija možete pronaći na mrežnoj stranici: http://www.erasmusentrepreneurs.eu/."]
             },
            #FAQ enrollment - https://www.unipu.hr/studenti/faq
            {"tag": "enrollment-Q1",
             # 1. Koje studijske programe mogu upisati na Sveučilištu?
              "patterns": ["Which study programs can I enroll at the University?", "all studies that can be enrolled", "study program list", "what can I study at your place", "all majors", "what majors are there "],
              "responses": ["Popis studijskih programa nalazi se na ovome linku: https://www.unipu.hr/obrazovanje/popis_svih_studijskih_programa"]
             },
            {"tag": "enrollment-Q2",
             # 2. Koji su dokumenti potrebni za upis?
              "patterns": ["What documents are required for registration?", "documents for registration"],
              "responses": ["Dokumenti potrebni za upis propisuju se Natječajem za upis koji se objavljuje na mrežnim stranicama Sveučilišta i dnevnom tisku najmanje šest mjeseci prije početka nastave. "]
             },
            {"tag": "enrollment-Q3",
             # 3. Je li za upis potrebno položiti prijemni ispit?
              "patterns": ["Is it necessary to pass an entrance exam for enrollment?", "enrollment entrance exam", "enrollment and entrance exam"],
              "responses": ["Uvjeti upisa na studij propisani su studijskim programima, objavljuju se u Natječaju za upis i na mrežnim stranicama Postani student. Prijemni ispit trenutačno se polaže samo na Odjelu za glazbu, a Odjel za odgojne i obrazovne znanosti provodi intervju te provjere poznavanja talijanskog jezika za studente koji taj ispit nisu položili na državnoj maturi. "]
             },
            {"tag": "enrollment-Q4",
             # 4. Postoji li mogućnost upisa izvanrednog studija i koji su uvjeti?
              "patterns": ["Is it possible to enroll in part-time studies and what are the conditions?", "I would enroll in part-time studies", "part-time studies", "part-time studies"],
              "responses": ["Mogućnost upisa izvanrednog studija određuje se studijskim programom. Uvjeti upisa jednaki su kao i za redoviti studij i propisuju se Natječajem za upis."]
             },
            {"tag": "enrollment-Q5",
             # 5. Plaćaju li redoviti studenti studij? Koliki su troškovi (upisa i školarine)?
              "patterns": ["Do full-time students pay for their studies? What are the costs (enrollment and tuition fees)?", "enrollment costs", "how much do I have to pay for enrollment?"],
              "responses": ["Visina školarine ovisi o Ministarstvu znanosti, obrazovanja i sporta i Sveučilištu. Studenti koji prvu put upisuju studij u statusu redovitog studenta ne plaćaju školarinu. Redoviti studenti viših godina studija ne plaćaju školarinu ako su u akademskoj godini ostvarili 55 i više ECTS bodova i ne studiraju duže od vremena predviđenog aktima MZOS-a i Sveučilišta (trenutačno regulirano Ugovorom o punoj subvenciji praticipacije redovitih studenata u troškovima studija u akademskim godinama 2012./2013., 2013./2014. i 2014./2015.). Sveučilište utvrđuje visinu školarina za sve ostale studente (redovite koji plaćaju studij i izvanredne studente) te upisninu. Odluke o visini školarina možete pronaći na linku: https://www.unipu.hr/dokumenti"]
             },
            {"tag": "enrollment-Q6",
             # 6. Na koji način i gdje se vrši uplata školarine i upisnine za upis godine studija? 
              "patterns": ["How and where do you pay tuition and enrollment fees for the year of study?", "where do I pay tuition fees", "how to pay enrollment fees", "where to pay enrollment fees", "I am enrolled, how to pay now" ],
              "responses": ["Sve uplate Sveučilištu i njegovim sastavnicama vrše se u banci ili pošti, na žiro račun Sveučilišta ili sastavnice. Podaci o bankovnim računima uvijek su navedeni u uputama za uplatu i dostupni na mrežnim stranicama."]
             },
            {"tag": "enrollment-Q7",
             # 7. Može li se školarina i upisnina platiti u više rata?  
              "patterns": ["Can tuition and enrollment be paid in several installments?", "tuition in installments", "tuition in installments", "payment in installments of tuition"],
              "responses": ["Plaćanje u ratama nije dozvoljeno (osim u iznimnim slučajevima). "]
             },
            {"tag": "enrollment-Q8",
             # 8. Koji su rokovi za upis sljedeće akademske godine?
              "patterns": ["What are the enrollment deadlines for the next academic year?", "enrollment deadline next year"],
              "responses": ["Upisi u sljedeću akademsku godinu vrše se od 1. do 30. rujna. "]
             },
            {"tag": "enrollment-Q9",
             # 9. Koji su uvjeti za upis više godine studija?
              "patterns": ["What are the conditions for enrolling in a higher year of study?", "conditions for enrolling in a higher year", "requirements for a higher year"],
              "responses": ["Uvjeti za upis više godine studija propisuju se studijskim programom. U pravilu, uvjet za upis više godine studija je ostvarenih 42 ECTS boda u jednoj akademskoj godini. Na pojedinim studijskim programima kao uvjet upisa u višu godinu predviđeno je polaganje određenih ispita (npr. onih iz obveznih ili vezanih kolegija) uz ostvarenih 42 ECTS boda u jednoj akademskoj godini."]
             },
            {"tag": "enrollment-Q10",
             # 10. Što je potrebno ako se u upisnom roku nije izvršio upis više godine studija
              "patterns": ["What is required if the registration for a higher year of study was not completed within the registration period", "I forgot to register for a higher year, what now", "I did not have time to register for a higher year"],
              "responses": ["U Službu za studente i ISVU može se podnijeti molba čelniku sastavnice za naknadni upis u kojoj treba navesti razloge zbog kojih se nije na vrijeme upisalo i priložiti dokumentaciju koja podupire te razloge."]
             },
            {"tag": "enrollment-Q11",
             # 11. Postoji li testiranje semestra?
              "patterns": ["Does semester testing exist?", "semester testing does it exist"],
              "responses": ["Ne."]
             },
            {"tag": "enrollment-Q12",
             # 12. Što je ubrzani studij?
              "patterns": ["What is accelerated study?", "I would study accelerated", "accelerated study"],
              "responses": ["Sukladno odredbama Pravilnika o studiju: Članak 47. Studenti koji u tekućoj godini ostvare 60 ECTS bodova mogu u sljedećoj godini upisati 30% ECTS bodova više od uobičajenoga godišnjeg opterećenja, uz uvjet da su ostvarili prosjek ocjena 4,5 ili više, odnosno 89% i više uspješnosti (ubrzani studij)."]
             },
            {"tag": "enrollment-Q13",
             # 13. Koji su uvjeti odabira izbornih predmeta? Do kada ih moram odabrati?
              "patterns": ["What are the conditions for choosing electives? By when do I have to choose them?", "conditions for choosing electives", "when electives are chosen."],
              "responses": ["Osim ako u silabu ne postoji naveden preduvjet upisa, uvjeta nema. Izborni predmeti odabiru se pri upisu u narednu akademsku godinu (od 1. do 30. rujna)."]
             },
            {"tag": "enrollment-Q14",
             # 14. Mogu li među izbornim predmetima odabrati neki s bilo kojeg drugog studija?
              "patterns": ["Can I choose one from any other study among the optional subjects?", "an optional subject from other faculties, is it possible"],
              "responses": ["Mogućnost odabira izbornih predmeta i popis predmeta koji se mogu odabrati definiraju se studijskim programom."]
             },
            {"tag": "studentStatus-Q1",
             # 1. Koja je razlika između redovitih i izvanrednih studenata? 
              "patterns": ["What is the difference between full-time and part-time students?", "difference between full-time and part-time students", "part-time or full-time enrollment"],
              "responses": ["Redoviti su oni studenti koji studiraju prema programu koji se temelji na punoj nastavnoj satnici (puno radno vrijeme). Troškovi studija (studijskog programa) mogu redovitim studentima biti dijelom ili u cijelosti financirani iz državnog proračuna, sukladno s općim aktom sveučilišta, veleučilišta ili visoke škole. Redoviti studenti imaju određena studentska prava i povlastice kao npr. zdravstveno osiguranje, oslobođenje od participacije pod uvjetima koje propisuje HZZO, mogućnost rada preko student servisa, pravo na dječji doplatak, pravo na subvencioniranu prehranu, pravo na popuste na usluge prijevoza itd. Izvanredni studenti su oni koji obrazovni program pohađaju uz rad ili drugu aktivnost koja traži posebno prilagođene termine i načine izvođenja studija u skladu s izvedbenim planom nastave. Troškove takvog studija u cijelosti ili dijelom snosi sam student, sukladno općem aktu sveučilišta, veleučilišta ili visoke škole.  "]
             },
            {"tag": "studentStatus-Q2",
             # 2. Koliko traje status studenta? Može li se izgubiti?
              "patterns": ["How long does student status last? Can it be lost?", "student status", "student status duration"],
              "responses": ["Status studenta traje do kraja akademske godine koju je student posljednju upisao (do 30. rujna). Prema Pravilniku o studiju: Članak 25. Student gubi status studenta: kada završi studij (danom polaganja posljednjega ispita, odnosno polaganjem završnoga ispita i diplomskoga ispita) kada se ispiše sa studija kada se ne upiše u sljedeću akademsku godinu (istekom roka za upis) kada je isključen sa studija po postupku i uz uvjete utvrđene općim aktom Sveučilišta kada ne završi studij u roku iz članka 13. stavka 3. ovoga Pravilnika (istekom akademske godine)."]
             },
            {"tag": "studentStatus-Q3",
             # 3. Što je mirovanje u studiju? Što je potrebno za reguliranje? 
              "patterns": ["What is studio hibernation? What is required to regulate?", "studio hibernation", "studio freezing", "freeze studio"],
              "responses": ["Sukladno odredbama Pravilnika o studiju: Članak 20. Mirovanje obveza može se odobriti za vrijeme trudnoće i do godine dana starosti djeteta, za vrijeme dulje bolesti i u drugim opravdanim slučajevima privremenoga prekida studija. Postojanje opravdanoga razloga iz stavka 1. ovoga članka student dokazuje odgovarajućom liječničkom potvrdom ili drugom vjerodostojnom dokumentacijom. Članak 21. Odluka o mirovanju studentskih obveza donosi se na temelju pisane molbe koju student podnosi Studentskoj službi, zajedno s indeksom i vjerodostojnom dokumentacijom koju je izdala ili ovjerila nadležna institucija. Potrebno je podnijeti molbu za mirovanje studentskih prava čelniku sastavnice/voditelju studija. Molba se predaje u Službi za studente i ISVU."]
             },
            {"tag": "studentStatus-Q4",
             # 4. Pod kojim uvjetima student može postati redoviti student ako je upisan kao izvanredni student? 
              "patterns": ["Under what conditions can a student become a full-time student if he is enrolled as a part-time student?", "part-time student to full-time", "conditions of part-time student to full-time", "transition from part-time to full-time"],
              "responses": ["Po trenutačnoj regulaciji ne može."]
             },
            {"tag": "studentStatus-Q5",
             # 5.Kolika je najveća dozvoljena dužina studiranja za redovite studente?
             "patterns": ["What is the maximum permitted length of study for full-time students?", "length of study for full-time students", "how long can I study", "length of study"],
              "responses": ["Sukladno odredbama Pravilnika o studiranju: Trajanje statusa studenta Članak 34. (1) Status studenta traje najviše dvostruko dulje od propisanog vremena trajanja studija. (2) U vrijeme trajanja studija ne uračunava se vrijeme mirovanja studija. (3) U iznimnim slučajevima, rektor može odobriti pojedinim studentima duži rok za završetak studija. Prestanak statusa studenta Članak 35. Osoba gubi status studenta: 1. kad završi studij 2. kad se ispiše sa Sveučilišta (danom ispisa) 3. kad ne završi studij u roku iz stavka 1. članka 34. ovog Pravilnika 4. kad u dvije akademske godine uzastopno ne ostvari uvjet za upis u višu godinu studija 5. kad u dvije uzastopne akademske godine ne položi isti kolegij 6. kad ne upiše sljedeću akademsku godinu u propisanom roku sukladno članku 7. ovog Pravilnika ili 7. kad je isključen sa studija iz razloga utvrđenih drugim općim aktima Sveučilišta."]
             },
            {"tag": "studentStatus-Q6",
             # 6. Kolika je najveća dozvoljena dužina studiranja za izvanredne studente?
              "patterns": ["What is the maximum permitted length of study for part-time students?", "how long can I study part-time?", "length of part-time study"],
              "responses": ["Ista je kao i kod redovitih studenata. Sukladno odredbama Pravilnika o studiranju: Trajanje statusa studenta Članak 34. (1) Status studenta traje najviše dvostruko dulje od propisanog vremena trajanja studija. (2) U vrijeme trajanja studija ne uračunava se vrijeme mirovanja studija. (3) U iznimnim slučajevima, rektor može odobriti pojedinim studentima duži rok za završetak studija. Prestanak statusa studenta Članak 35. Osoba gubi status studenta: 1. kad završi studij 2. kad se ispiše sa Sveučilišta (danom ispisa) 3. kad ne završi studij u roku iz stavka 1. članka 34. ovog Pravilnika 4. kad u dvije akademske godine uzastopno ne ostvari uvjet za upis u višu godinu studija 5. kad u dvije uzastopne akademske godine ne položi isti kolegij 6. kad ne upiše sljedeću akademsku godinu u propisanom roku sukladno članku 7. ovog Pravilnika ili 7. kad je isključen sa studija iz razloga utvrđenih drugim općim aktima Sveučilišta."]
             },
            {"tag": "studentStatus-Q7",
             # 7. Koliko puta smijem ponavljati godinu? Mogu li i kako upisati međugodinu?
              "patterns": ["How many times can I repeat the year? Can I and how do I enter the gap year?", "repeat the year", "entry of the gap year", "entry of the year if I failed"],
              "responses": ["Sukladno odredbama Statuta: Prestanak statusa studenta Članak 86. (1) Status redovitog studenta prestaje kad student u dvije uzastopne akademske godine ne ostvari barem 36 ECTS-a ili u dvije uzastopne akademske godine ne položi isti predmet ili protekom roka iz stavka 1. članka 81. ovog Statuta. (2) Status studenta prestaje: završetkom studija, ispisom sa Sveučilišta, kad student ne upiše sljedeću akademsku godinu i ako se isključi sa studija iz razloga utvrđenih drugim općim aktima Sveučilišta. Dakle, godina se može ponavljati jednom. Međugodina ne postoji. Postoji ponovni upis godine s dopisivanjem nepoloženih predmeta."]
             },
            {"tag": "studentStatus-Q8",
             # 8. Kako se upisuje apsolventska godina studija?  
              "patterns": ["How to enroll in the senior year of study?", "how to enroll in the senior year", "enrollment in the senior year", "graduate year"],
              "responses": ["Studenti po bolonjskom sustavu nemaju apsolventsku godinu. Upis sljedeće akademske godine nakon one u kojoj su odslušana sva predavanja smatra se ponovnim upisom."]
             },
            {"tag": "studentStatus-Q9",
             # 9. Je li moguće promijeniti studijski program/odjel? Kakva je procedura? Je li moguća promjena u tijeku akademske godine?
              "patterns": ["Is it possible to change the study program/department? What is the procedure? Is it possible to change during the academic year?", "change of study course", "can I change study course", "change of course in progress academic years"],
              "responses": ["Sukladno odredbama Pravilnika o studiju: Članak  51. Studentu se može dopustiti promjena studija unutar visokoga učilišta, s jednopredmetnoga na dvopredmetni studij ili s dvopredmetnoga na jednopredmetni studij, odnosno s jednoga na drugi studijski program. Promjena studija moguća je samo jednom tijekom studiranja. Student promjenu studija unutar visokog učilišta ne može zatražiti na početku prve godine studija. Zamolbe za promjenu studija predaju se najkasnije do kraja akademske godine, rješavaju se u roku od 7 dana te se najkasnije do 15. listopada omogućava studentu upis. Članak 52. Promjena studija iz članka 51. dopustit će se ako na studiju koji bi student želio upisati ima slobodnih mjesta u odnosu na kvotu predviđenu za studij. Prijelaz odobrava nadležno tijelo sveučilišnoga odjela ili samostalnoga sveučilišnoga studija. Student mora u roku od jedne akademske godine odslušati sve predmete i položiti razlikovne ispite studija na koji je prešao."]
             },
            {"tag": "studentStatus-Q10",
             # 10. Kakva je procedura kod prijelaza s nekog drugog sveučilišta ili veleučilišta?
              "patterns": ["What is the procedure for transferring from another university or polytechnic?", "transfer to another study", "transfer to another university"],
              "responses": ["Sukladno odredbama Pravilnika o studiju Članak 48. Student koji je na nekom drugom studiju u Hrvatskoj u redovitom roku stekao uvjete za upis u višu godinu studija, propisane na ovome Sveučilištu, može nastaviti istovrsni studij na Sveučilištu na toj studijskoj godini. Student uz zahtjev za prijelaz prilaže izvorne dokumente koji se zahtijevaju natječajem za upis, indeks i privremeni supplement diplomi, studijski program prethodnoga studija, uvjete za upis u višu godinu studija te potvrdnicu da je ispisan s prethodnoga studija. Studentu kojemu se dopusti prijelaz na Sveučilište, prema stavku 1. ovoga članka, priznat će se odgovarajuće godine provedene na studiju. Od položenih ispita priznat će mu se ispiti iz predmeta čiji nastavni programi odgovaraju nastavnim programima odnosnih predmeta na ovome Sveučilištu. Članak 49. Prijelaz iz stavka 1. članka 51. može se izvršiti samo u redovitom upisnom roku u akademsku godinu, od 1. do 30. rujna. O molbi studenta da mu se dopusti prijelaz odlučuje Odbor za nastavu, odnosno drugo nadležno tijelo sveučilišnoga odjela ili sveučilišnoga studija. U odluci kojom se dopušta prijelaz odlučuje se o sljedećem: u koju se studijsku godinu upisuje student koji je status studenta koji se ispiti, položeni na drugome visokom učilištu, priznaju studentu na ovome Sveučilištu, na temelju mišljenja predmetnoga nastavnika o polaganju razlikovnih ispita o odobravanju upisa sukladno odredbama ovoga Pravilnika. Student koji je na drugome visokom učilištu izgubio pravo studiranja ne može nastaviti istovrsni studij na ovome Sveučilištu. Članak 50. Student koji je studirao na nekom visokom učilištu u inozemstvu može tražiti prelazak na Sveučilište na način i uz uvjete utvrđene člankom 51. i 52."]
             },
            {"tag": "evaulationExams-Q1",
             # 1. Gdje se mogu vidjeti rasporedi predavanja za studente?
              "patterns": ["Where can I see class schedules for students?", "class schedule", "class schedule", "when is the class", "class time"],
              "responses": ["Rasporedi predavanja dostupni su na mrežnim stranicama studija, a na nekim sastavnicama i na vratima predavaonica."]
             },
            {"tag": "evaulationExams-Q2",
             # 2. Gdje se mogu naći termini ispita i konzultacija?
              "patterns": ["Where can I find exam and consultation dates?", "exam dates", "consultation dates", "when is the exam", "exam time", "I want a consultation with the professor"],
              "responses": ["Termini ispita dostupni su na Studomatu. Raspored konzultacija dostupan je na vratima nastavničkih kabineta. Neke sastavnice navede informacije oglašavaju i na mrežnim stranicama."]
             },
            {"tag": "evaulationExams-Q3",
             # 3. Gdje se može naći literatura za pojedine predmete studija?
              "patterns": ["Where can you find literature for certain study subjects?", "study literature", "which literature to use", "literature", "how to get literature"],
              "responses": ["Popis literature dostupan je u silabima (izvedbenim planovima nastave) predmeta koji su ili objavljeni na mrežnim stranicama studija ili dostupni putem e-učenja. Literatura se može posuditi u knjižnici sastavnice ili Sveučilišnoj knjižnici."]
             },
            {"tag": "evaulationExams-Q4",
             # 4. Od kada do kada traju predavanja i ispitni rokovi u akademskoj godini?
              "patterns": ["From when until when do lectures and exam periods last in the academic year?", "from when until when do lectures last", "duration of lectures and exam periods", "duration of periods"],
              "responses": ["Trajanje predavanja uređuje se kalendarom nastave koji donosi Senat i objavljuje se na mrežnim stranicama Sveučilišta. Ispitni rokovi objavljuju se zasebno za svaku akademsku godinu i imaju jednako trajanje kao i akademska godina (od 1. listopada do 30. rujna sljedeće godine)."]
             },
            {"tag": "evaulationExams-Q5",
             # 5. Zašto postoji razlika u načinima vrednovanja studentskog rada među predmetima?
              "patterns": ["Why is there a difference in the ways of evaluating student work between courses?", "difference in ways of evaluating student work", "difference in project evaluation"],
              "responses": ["Pravilnikom o ocjenjivanju određuju se okviri načina vrednovanja studentskog rada i elementi koji se mogu vrednovati. Sukladno svojoj autonomiji, nastavnik sam razrađuje načine vrednovanja studentskog postignuća, vodeći računa o Pravilniku i ECTS sustavu. Različiti ishodi učenja zahtjevaju različite nastavne metode i različite načine vrednovanja. Vrednovanje i ocjenjivanje regulirano je Pravilnikom o ocjenjivanju. Silabe predmeta definiraju nastavnici i sva pitanja o vrednovanju u konkretnom predmetu treba postaviti nastavniku."]
             },
            {"tag": "evaulationExams-Q6",
             # 6. Koja je procedura prijave ispita?
              "patterns": ["What is the exam registration procedure?", "how to register an exam", "I want an exam registration", "exam registration"],
              "responses": ["Sukladno odredbama Pravilnika o studiju: Članak 64. Student je dužan ispit prijaviti najkasnije pet radnih dana prije održavanja ispita. Student koji je evidentiran sustavom ISVU ispit prijavljuje lokalnim računalom ili internetom koristeći se programskim modulom Studomat. O rasporedu ispita kod velikoga broja prijava predmetni nastavnik izvješćuje studente posebnim oglasom na službenim mrežnim stranicama i na oglasnoj ploči Odjela, najkasnije dva dana prije ispitnoga termina. Studenti koji nisu evidentirani sustavom ISVU prijavljuju ispite prijavnicama predanim u Službu za studente i ISVU."]
             },
            {"tag": "evaulationExams-Q7",
             # 7. Gdje i kako se odjavljuje prijavljeni ispit?
              "patterns": ["Where and how to deregister a registered exam?", "how to deregister an exam", "deregistering an exam", "where to deregister an exam"],
              "responses": ["Sukladno Pravilniku o studiju: Članak 65. Student koji je evidentiran sustavom ISVU ispit odjavljuje lokalnim računalom ili internetom koristeći se programskim modulom Studomat. Studentu koji je evidentiran sustavom ISVU, a nije pristupio prijavljenom ispitu niti ga je na vrijeme odjavio, nastavnik će u ispitnu listu upisati '0'. U tom slučaju smatrat će se da ispit nije položio. Članak 66. Iznimno, ispit će se smatrati pravodobno odjavljenim ako student ili osoba koju on ovlasti, na dan ispita, a najkasnije u roku od 24 sata nakon dana i sata održavanja ispita, predoči dokaz kojim dokazuje opravdane okolnosti zbog kojih student nije mogao pravodobno odjaviti ispit. Dokaz se predaje Studentskoj službi ili predmetnomu nastavniku koji donosi odluku."]
            },
            {"tag": "evaulationExams-Q8",
             # 8. Koliko puta imam pravo izaći na jedan ispit?
              "patterns": ["How many times do I have the right to sit for one exam?", "how many times can I sit for the exam", "how many times can I repeat the exam", "number of sittings for the exam", "turnout for the exam"],
              "responses": ["Sukladno odredbama Pravilnika o studiju: Članak 69. Ispit iz istoga predmeta može se polagati najviše četiri puta. Ako student četvrti put ispit ne položi, mora u sljedećoj akademskoj godini ponovno upisati taj predmet. Ako student ni nakon ponovno odslušanoga predmeta ne položi ispit četvrti put (ukupno osmi put), peti (deveti) put ispit polaže pred nastavničkim povjerenstvom koje čini predsjednik i dva člana. Ako student nakon ponovo odslušanoga predmeta ne položi ispit utvrđenim načinom u članku 69. ovoga Pravilnika, gubi pravo studiranja na upisanome studijskom programu."]
             },
            {"tag": "evaulationExams-Q9",
             # 9. Ukoliko smatram da mi je na ispitu učinjena nepravda, kome se mogu obratiti?
              "patterns": ["If I believe that an injustice was done to me during the exam, who can I contact?", "I consider that the grade is not fair and unfair", "who to contact for unfairness during the exam", "who to contact for wrongly graded exam", "my exam was not graded well", "unfair grading"],
              "responses": ["Sukladno odredbama Pravilnika o studiju: Članak 67. Nastavnik mora studentu obrazložiti konačnu ocjenu. Student koji nije zadovoljan ocjenom na ispitu ima pravo podnijeti prigovor na ocjenu. Prigovor se podnosi pročelniku odjela u roku od 24 sata nakon priopćenja ocjene. Prigovor mora biti obrazložen. Ako prigovor ocijeni utemeljenim, pročelnik će donijeti odluku kojom dopušta ponavljanje ispita, imenuje nastavničko povjerenstvo i određuje vrijeme ponovnoga polaganja ispita. Nastavničko povjerenstvo čine predsjednik i dva člana. Predmetni nastavnik ne može biti predsjednikom povjerenstva. Članak 68. Ponovni ispit organizira se najkasnije u roku od tri dana od dana podnošenja prigovora. Pismeni ispit ili pismeni dio ispita ne ponavlja se pred povjerenstvom, već ga ono ponovno pregledava i ocjenjuje. Na temelju predloženih ocjena svih članova povjerenstva predsjednik povjerenstva zaključuje konačnu ocjenu i ako je ta ocjena pozitivna, upisuje ju u indeks. Zaključna ocjena ne može biti pozitivna ako su dva člana povjerenstva predložila negativnu ocjenu. Povjerenstvo vodi zapisnik o tijeku ispita. Na odluku o ocjeni nastavničkoga povjerenstva ne može se podnijeti prigovor."]
             },
            {"tag": "evaulationExams-Q10",
             # 10. Može li se ispit polagati prije no što završe predavanja? U kojem slučaju student može prijevremeno polagati ispite?
              "patterns": ["Can the exam be taken before the end of the lectures? In which case can the student take the exams early?", "taking the exam before the end of the lecture", "taking the exam early"],
              "responses": ["Ispiti se polažu nakon što student odsluša predavanja i zadovolji obveze koje mu omogućavaju izlazak na ispit."]
             },
            {"tag": "finishing-Q1",
             # 1. Koji je rok za prijavu završnog/diplomskog rada? 
              "patterns": ["What is the deadline for submitting the final/graduate thesis?", "deadline for submitting the final thesis", "deadline for submitting the graduate thesis", "deadline for submitting the final thesis"],
              "responses": ["Sukladno odredbama Pravilnika o završnome radu i Pravilnika o diplomskome radu: Student prijavljuje završni rad/završni koncert i diplomski rad/diplomski koncert u studentsku službu, na za to predviđenom obrascu (prijavi), najkasnije do 15. travnja  posljednje akademske godine studija."]
             },
            {"tag": "finishing-Q2",
             # 2. Jesu li su teme zadane ili slobodne? 
              "patterns": ["Are the topics set or free?", "set and free topics of the final paper", "topics of the final paper", "topics of the diploma", "are the topics already given or free"],
              "responses": ["Sukladno odredbama Pravilnika o završnome radu i Pravilnika o diplomskome radu: Način utvrđivanja i broj tema po kolegiju, predmetu, području ili mentoru utvrđuje se posebnom odlukom stručnog vijeća odjela, odnosno samostalnog studija."]
             },
            {"tag": "finishing-Q3",
             # 3. Tko može biti mentor/sumentor?
              "patterns": ["Who can be a mentor/sumentor?", "mentor for the final thesis", "who can be a mentor for the final thesis"],
              "responses": ["Sukladno odredbama Pravilnika o završnome radu i Pravilnika o diplomskome radu: Mentor pri izradi i obrani završnog rada/završnog koncerta može biti nastavnik u znanstveno-nastavnom, umjetničko-nastavnom i nastavnom ili višem suradničkom zvanju. Sumentor pri izradi i obrani završnog rada/završnog koncerta može biti nastavnik u znanstveno-nastavnom, umjetničko-nastavnom i nastavnom zvanju ili suradničkom zvanju (asistent i viši asistent). Mentor i sumentor pri izradi i obrani diplomskoga rada/diplomskog koncerta može biti nastavnik u znanstveno-nastavnom, umjetničko-nastavnom i nastavnom ili višem suradničkom zvanju."]
             },
            {"tag": "finishing-Q4",
             # 4. Koja je procedura obrane?
              "patterns": ["What is the defense procedure?", "final thesis defense", "how to defend the final thesis"],
              "responses": ["Sukladno odredbama Pravilnika o završnome radu: Članak 9. (1) Obrana je završnog rada/izvedba završnog koncerta javna. (2) Obrana završnog  rada/izvedba završnog koncerta sastoji se od usmenog/praktičnog prikaza rezultata završnog rada, odnosno završni koncert čini javna izvedba završnog programa. (3) Studentska referada prilaže obrazac zapisnika o obrani završnog rada/završnog koncerta, a popunjava ga predsjednik povjerenstva. (4) Predsjednik povjerenstva otvara postupak obrane završnog rada/izvedbe završnog koncerta. (5) Pristupnik izlaže osnovnu problematiku rada, metode kojima se služio i najvažnije rezultate do kojih je došao u radu. Izlaganje završnog rada traje do 15 minuta, a izvedba završnog koncerta 45 minuta. (6) Na obrani završnog rada na svim studijskim smjerovima, osim na instrumentalno umjetničkim studijima, članovi povjerenstva postavljaju pitanja pristupniku. Svaki član može postaviti najviše tri pitanja. (7) Nakon što je student odgovorio na sva pitanja, odnosno nakon izvedenoga završnog koncerta, povjerenstvo razmatra kvalitetu završnog rada/završnog koncerta i usmene obrane te donosi konačnu ocjenu prema Pravilniku o ocjenjivanju. (8) Ocjena se upisuje u indeks i zapisnik o obrani završnog rada/izvedbi završnog koncerta, te svi članovi povjerenstva potpisuju i indeks  i zapisnik. --- Sukladno odredbama Pravilnika o diplomskome radu: (1) Obrana diplomskog rada/izvedba diplomskog koncerta je javna. (2) Obrana diplomskog rada/izvedba diplomskog koncerta sastoji se od usmenog/praktičnog prikaza rezultata diplomskog rada, odnosno diplomski koncert čini javna izvedba diplomskog programa. (4) Studentska referada prilaže obrazac o obrani diplomskog rada/izvedbi diplomskog koncerta. (4) Predsjednik povjerenstva otvara postupak obrane diplomskoga rada/izvedbe diplomskoga koncerta. (5) Pristupnik izlaže osnovnu problematiku rada, metode kojima se služio i najvažnije rezultate do kojih je došao u radu. Izlaganje diplomskog rada traje do 15 minuta, a izvedba diplomskog koncerta 60 minuta. (6) Na obrani diplomskoga rada na svim studijskim smjerovima, osim na instrumentalno-umjetničkim studijima, članovi povjerenstva postavljaju pitanja pristupniku. Svaki član može postaviti najviše tri pitanja. (7) Nakon što je student odgovorio na sva  pitanja, odnosno nakon izvedenoga diplomskog koncerta, povjerenstvo razmatra kvalitetu diplomskoga rada/diplomskog koncerta i obrane/izvedbe te na temelju toga donosi konačnu ocjenu prema Pravilniku o ocjenjivanju. (8) Ocjena se upisuje u indeks i zapisnik o obrani diplomskog rada/izvedbi diplomskog koncerta, te svi članovi povjerenstva potpisuju i indeks i zapisnik."]
             },
            {"tag": "finishing-Q5",
             # 5. Ako nisam zadovoljan završnom ocjenom obrane, mogu li je odbiti?  
              "patterns": ["If I am not satisfied with the final grade of the defense, can I reject it?", "rejection of the final grade", "dissatisfaction with the final grade"],
              "responses": ["Navedena mogućnost nije predviđena."]
             },
            {"tag": "finishing-Q6",
             # 6. Postoji li propisan izgled i forma završnog/diplomskog rada?
              "patterns": ["Is there a prescribed layout and form of the final/graduation thesis?", "prescribed layout and format of the final", "how to write a final thesis", "how to write a graduation thesis"],
              "responses": ["Da. Navedeno je propisano Pravilnikom o završnome radu (članak 5.) i Pravilnikom o diplomskome radu (članak 5.)."]
             },
            {"tag": "finishing-Q7",
             # 7. Na koji način se izdaje diploma i što je potrebno za taj postupak? 
              "patterns": ["How is a diploma issued and what is required for that procedure?", "how is a diploma issued", "how to get a diploma"],
              "responses": ["Nakon obrane završnog/diplomskog rada u Službi se ispunjavaju potrebni obrasci, vrši uplata troškova tiskanja diplome i donosi uvezani i elektronički primjerak rada. Diploma se izdaje po ispunjenju svih studijskih obveza, a uručuje na svečanoj promociji."]
             },
            {"tag": "diploma-Q1",
             #  Utvrđivanje diplome navažećom i izdavanje nove diplome („duplikat diplome“)
              "patterns": ["Determining a diploma invalid and issuing a new diploma (duplicate diploma)", "duplicate diploma", "I lost my diploma, what now"],
              "responses": ["Osobe kojima je Sveučilište Jurja Dobrile u Puli ili neki od njegovih pravnih prednika izdalo diplomu/svjedodžbu, mogu u slučaju gubitka, uništenja ili drugog sličnog razloga zatražiti izdavanje nove diplome samo na način kako je predviđeno općim aktom Sveučilišta Jurja Dobrile u Puli. Prije izdavanja nove diplome, ovlaštena osoba je dužna pokrenuti postupak utvrđivanja diplome/svjedodžbe nevažećom. "]
             },
            {"tag": "diploma-Q2",
             # Postupak utvrđenja diplome/svjedodžba nevažećom:
              "patterns": ["Procedure to determine diploma/certificate invalid:", "invalid diploma"],
              "responses": ["1. osoba na čije je ima diploma/svjedodžba izdana može pokrenuti postupak u kojem će se diplom/svjedodžba proglasiti nevažećom zbog gubitka, uništenja ili drugog sličnog razloga 2. postupak se pokreće podnošenjem popunjenog zahtjeva (OBRAZAC 1) i preslike osobne iskaznice 3. temeljem urednog zahtjeva rektor u roku od 15 dana izdaje rješenje kojim se diploma/ svjedodžba proglašava nevažećom i dostavlja podnositelju zahtjeva 4. podnositelj zahtjeva je dužan rješenje o proglašenju diplome/svjedodžba nevažećom objaviti kao oglas u Narodnim novima Tek nakon što se temelje rješenja izdanog od strane Sveučilišta diploma/svjedodžba objavi nevažećom u Narodnim novinama moguće je zatražiti izdavanje nove diplome."]
             },
            {"tag": "diploma-Q3",
             # Postupak izdavanja nove diplome jer je ranija diploma/svjedodžba proglašena nevažećom: 
              "patterns": ["Procedure for issuing a new diploma because the previous diploma/certificate is declared invalid:", "new diploma if the old one is invalid", "I have an invalid diploma and want another one"],
              "responses": ["1. postupak se pokreće podnošenjem popunjenog zahtjeva (OBRAZAC 2). 2. uz popunjeni obrazac zahtjeva potrebno je dostaviti dokaz da je rješenje o proglašenju diplome/svjedodžbe nevažećom objavljeno u Narodnim novinama te dokaz o uplati naknade za izdavanje nove diplome (duplikata). 3.Sveučilište temeljem urednog zahtjeva izrađuje novu diplomu sukladno propisima koji su na snazi."]
             },
            {"tag": "enrollment",
             # upis fakulteta
              "patterns": ["Faculty enrollment procedure", "how to enroll in faculty", "how to enroll in FIPU", "enrollment in FIPU", "I want to enroll", "enrollment in faculty", "how to enroll in FIPU faculty?"],
              "responses": ["Ja ti ne mogu dati previše informacija o upisu, ali možeš to potražiti na stranicama sveučilišta. :D"]
             },
            {"tag": "professors",
             # nastavnici FIPU
              "patterns": ["list of professors", "who are all professors at the faculty?", "all professors", "professors", "email address from professor", "list of email addresses from professor"],
              "responses": ["Izvanredni profesor: \nizv.profesor.dr.sc. Valter Boljunčić (valter.boljuncic@unipu.hr), izv. prof. dr. sc. Darko Etinger (darko.etinger@unipu.hr), izv. prof. dr. sc. Tihomir Orehovački (tihomir.orehovacki@unipu.hr), izv. prof. dr. sc. Giorgio Sinković (giorgio.sinkovic@unipu.hr). \nDocent: \ndoc. dr. sc. Siniša Miličić (sinisa.milicic@unipu.hr), doc. dr. sc. Goran Oreški (goran.oreski@unipu.hr), doc. dr. sc. Siniša Sovilj (sinisa.sovilj@unipu.hr), doc. dr. sc. Nikola Tanković (nikola.tankovic@unipu.hr). \nAsistent: \nIngrid Hrga, mag.oec (ingrid.hrga@unipu.hr), Robert Šajina, mag.inf (robert.sajina@unipu.hr), Romeo Šajina, mag.inf (romeo.sajina@unipu.hr). \nStručni suradnik: \nSrđan Daniel Simić (srdjan.daniel.simic@unipu.hr)"]
             },
]}