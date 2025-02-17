import random

def capitalize_lists(continentex):
    capitalix = []
    for elements in continentex:
        capiz = [elements.capitalize() for elements in continentex]
        capitalix.extend((capiz))
    return capitalix
        
def accentsfree (lista):
    newwords = []
    for word in lista:
        palabra = word
        
        if "Á" in word or "á" in word:
            palabra = palabra.replace("á", "a").replace("Á", "A")
        if "Í" in word or "í" in word:
            palabra = palabra.replace("í", "i").replace("Í", "I")
        if "Ú" in word or "ú" in word:
            palabra = palabra.replace("ú", "u").replace("Ú", "U")
        if "É" in word or "é" in word:
            palabra = palabra.replace("é", "e").replace("É", "E")
        if "Ó" in word or "ó" in word:
            palabra = palabra.replace("ó", "o").replace("Ó", "O")
        newwords.append(palabra)
    return newwords

def get_key(diccionario, word):
        for key, listita in diccionario.items():
            for elements in listita:
                if elements == word:
                    result = key
                    return result
                
def lista_random(palabras, result):
    yatusabe = []
    for nose in range(0, 5):
        chacha = random.choice(palabras)
        yatusabe.append(chacha)
        
    jijiji =  [1, 2, 3, 4, 5, 6]
    jojojo = random.choice(jijiji)
    yatusabe.insert(jojojo, result)
    yatusabe = [word.capitalize() for word in yatusabe]
    list(set(yatusabe))
    return yatusabe
    
paises = [
    "Afganistán",
    "Albania",
    "Alemania",
    "Andorra",
    "Angola",
    "Antigua y Barbuda",
    "Arabia Saudí",
    "Argelia",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaiyán",
    "Bahamas",
    "Bahréin",
    "Bangladés",
    "Barbados",
    "Bélgica",
    "Belice",
    "Benín",
    "Bielorrusia",
    "Birmania",
    "Bolivia",
    "Bosnia y Herzegovina",
    "Botsuana",
    "Brasil",
    "Bulgaria",
    "Brunéi",
    "Burkina Faso",
    "Burundi",
    "Bután",
    "Cabo Verde",
    "Camboya",
    "Camerún",
    "Canadá",
    "Sri Lanka",
    "Chad",
    "Chile",
    "China",
    "Chipre",
    "Ciudad del Vaticano",
    "Colombia",
    "Comoras",
    "Corea del Norte",
    "Corea del Sur",
    "Costa de Marfil",
    "Costa Rica",
    "Croacia",
    "Cuba",
    "Dinamarca",
    "Dominica",
    "Ecuador",
    "Egipto",
    "El Salvador",
    "Emiratos Árabes Unidos",
    "Eritrea",
    "Eslovaquia",
    "Eslovenia",
    "España",
    "Estados Unidos",
    "Estonia",
    "Etiopía",
    "Filipinas",
    "Finlandia",
    "Fiyi",
    "Francia",
    "Gabón",
    "Gambia",
    "Georgia",
    "Ghana",
    "Granada",
    "Grecia",
    "Guatemala",
    "Guayana",
    "Guinea",
    "Guinea Ecuatorial",
    "Guinea-Bissáu",
    "Haití",
    "Honduras",
    "Hungría",
    "India",
    "Indonesia",
    "Irak",
    "Irán",
    "Irlanda",
    "Islandia",
    "Israel",
	"Italia",
    "Jamaica",
    "Japón",
    "Jordania",
    "Kazajistán",
    "Kenia",
    "Kirguizistán",
    "Kiribati",
    "Kuwait",
    "Laos",
    "Lesoto",
    "Letonia",
    "Líbano",
    "Liberia",
    "Libia",
    "Liechtenstein",
    "Lituania",
    "Luxemburgo",
    "Macedonia",
    "Madagascar",
    "Malasia",
    "Malaui",
    "Maldivas",
    "Malí",
    "Malta",
    "Marruecos",
    "Marshall",
    "Mauricio",
    "Mauritania",
    "México",
    "Micronesia",
    "Moldavia",
    "Mónaco",
    "Mongolia",
    "Montenegro",
    "Mozambique",
    "Namibia",
    "Nauru",
    "Nepal",
    "Nicaragua",
    "Níger",
    "Nigeria",
    "Noruega",
    "Nueva Zelanda",
    "Omán",
    "Países Bajos",
    "Pakistán",
    "Palaos",
    "Panamá",
    "Papúa-Nueva Guinea",
    "Paraguay",
    "Perú",
    "Polonia",
    "Portugal",
    "Puerto Rico",
    "Qatar",
    "Reino Unido",
    "República Centroafricana",
    "República Checa",
    "República del Congo",
    "República Democrática del Congo",
    "República Dominicana",
    "Ruanda",
    "Rumanía",
    "Rusia",
    "Salomón",
    "Samoa",
    "San Cristóbal y Nieves",
    "San Marino",
    "San Vicente y las Granadinas",
    "Santa Lucía",
    "Santo Tomé y Príncipe",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leona",
    "Singapur",
    "Siria",
    "Somalia",
    "Suazilandia",
    "Sudáfrica",
    "Sudán",
    "Suecia",
    "Suiza",
    "Surinam",
    "Tailandia",
    "Tanzania",
    "Tayikistán",
    "Timor Oriental",
    "Togo",
    "Tonga",
    "Trinidad y Tobago",
    "Túnez",
    "Turkmenistán",
    "Turquía",
    "Tuvalu",
    "Ucrania",
    "Uganda",
    "Uruguay",
    "Uzbekistán",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Yibuti",
    "Zambia",
    "Zimbabue"
    
]

idiomas = [

"albanés",
"alemán",
"catalán",
"portugués",
"inglés",
"árabe",
"castellano",
"armenio",
"azerí",
"bengalí",
"neerlandés",
"francés",
"bielorruso",
"ruso",
"birmano",
"serbo-croata",
"malayo",
"búlgaro",
"mandarin",
"griego",
"turco",
"italiano",
"coreano",
"croata",
"danés",
"eslovaco",
"esloveno",
"estonio",
"amárico",
"filipino",
"finés",
"georgiano",
"húngaro",
"hindi",
"indonesio",
"persa",
"irlandes",
"islandes",
"hebreo",
"japonés",
"kazajo",
"kirguís",
"pastún",
"birmano",
"serbio",
"rundi",
"dzongka",
"cingalés",
"comorense",
"tigriña",
"arabe chadiano",
"sueco",
"haitiano",
"suahili",
"kiribatiano",
"lao",
"soto meridional",
"letón",
"lituano",
"luxemburgués",
"macedonio",
"malgache",
"malayo",
"chicheua",
"maldivo",
"maltés",
"marshalés",
"rumano",
"mongol",
"nauruano",
"nepalí",
"noruego",
"urdu",
"palauano",
"hiri motu",
"tok pisin",
"polaco",
"checo",
"ruanda",
"rumano",
"samoano",
"criollo seychellense",
"somalí",
"mina",
"suazi",
"zulú",
"tailandés",
"tayiko",
"tongano",
"turcomano",
"tuvaluano",
"ucraniano",
"uzbeko",
"bislama",
"vietnamita",
"bosnio"

]

famIdiomas = {
        "armenio" : ["armenio"],
        "albanes" : ["albanés"],
        "lenguas helenicas" : ["griego"],
        "lenguas romances" : ["castellano", "francés", "Portugues", "italiano","rumano", "Criollo haitiano","criollo seychellense"],
        "lenguas indoiranias" : ["maldivo","hindi", "Urdu", "bengalí", "cingalés", "nepalí","persa", "pastún","tayiko"],
        "lenguas celticas" : "irlandes",
        "lenguas germanicas" : ["inglés", "escoces", "alemán", "sueco", "islandes", "danés", "neerlandés", "afrikaans", "noruego", "luxemburgués", "tok pisin", "fiyiano", "tongano"],
        "lenguas balticas" : ["lituano", "letón"],
        "lenguas eslavas" : ["ruso", "polaco", "ucraniano", "checo", "serbio", "Bulgaro", "croata","bielorruso", "Eslovaco", "bosnio", "Esloveno", "Macedonio", "esloveno"],
        "Lenguas uralicas" : ["hungaro", "fines", "estonio"],
        "lenguas turquicas" : ["turco", "azeri", "turcomano", "kazajo", "Kirguis", "uzbeko"],
        "lenguas semiticas" : ["arabe", "hebreo", "tigriña"],
        "lenguas cusitas" : ["somali"],
        "lenguas chadicas" : ["arabe chadiano"],
        "lenguas nigerocongolesas" : ["suazi", "suahili", "zulú", "comorense", "mina", "soto meridional", "chicheua"],
        "lenguas sino-tibetanas" : ["Mandarín", "birmano"],
        "lenguas austroasiáticas" : ["Jemer", "Vietnamita", "lao", "Tailandés"],
        "lenguas austronesias" : ["palauano", "nauruano","Malayo", "Indonesio", "filipino", "Malgache", "Samoano", "Bislama", "Tetum"],
        "lenguas coreanicas" : ["coreano"],
        "lenguas japónicas" : ["japones"],
        "lenguas mongolicas" : ["mongol"]}

def langPaisesGam():
    
    paises_idiomas = {
    "Afganistán" : "persa",
    "Albania" : "albanés",
    "Alemania" : "alemán",
    "Andorra" : "catalán",
    "Angola" : "portugués",
    "Antigua y Barbuda" : "inglés",
    "Arabia Saudí" : "árabe",
    "Argelia" : "	árabe",
    "Argentina" : "castellano",
    "Armenia" : "armenio",
    "Australia" : "inglés",
    "Austria" : "alemán",
    "Azerbaiyán" : "azerí",
    "Bahamas" : "inglés",
    "Bahréin" : "árabe",
    "Bangladés" : "bengalí",
    "Barbados" : "	inglés",
    "Bélgica" : "neerlandés",
    "Belice" : "inglés",
    "Benín" : "	francés",
    "Bielorrusia" : "bielorruso",
    "Birmania" : "birmano",
    "Bolivia" : "castellano",
    "Bosnia y Herzegovina" : "bosnio",
    "Botsuana" : "inglés",
    "Brasil" : "portugués",
    "Brunéi" : "malayo",
    "Bulgaria" : "búlgaro",
    "Burkina Faso" : "francés",
    "Burundi" : "rundi",
    "Bután" : "dzongka",
    "Cabo Verde" : "portugués",
    "Camboya" : "jemer",
    "Camerún" : "francés",
    "Canadá" : "francés",
    "Sri Lanka" : "cingalés",
    "Chad" : "arabe chadiano",
    "Chile" : "	castellano",
    "China" : "mandarin",
    "Chipre" : "griego",
    "Ciudad del Vaticano" : "italiano",
    "Colombia" : "castellano",
    "Comoras" : "comorense",
    "Corea del Norte" : "coreano",
    "Corea del Sur" : "coreano",
    "Costa de Marfil" : "francés",
    "Costa Rica" : "castellano",
    "Croacia" : "croata",
    "Cuba" : "castellano",
    "Dinamarca" : "	danés",
    "Dominica" : "inglés",
    "Ecuador" : "castellano",
    "Egipto" : "árabe",
    "El Salvador" : "castellano",
    "Emiratos Árabes Unidos" : "árabe",
    "Eritrea" : "tigriña",
    "Eslovaquia" : "eslovaco",
    "Eslovenia" : "esloveno",
    "España" : "castellano",
    "Estados Unidos" : "ingles",
    "Estonia" : "estonio",
    "Etiopía" : "amárico",
    "Filipinas" : "filipino",
    "Finlandia" : "finés",
    "Fiyi" : "inglés",
    "Francia" : "francés",
    "Gabón" : "francés",
    "Gambia" : "ingles",
    "Georgia" : "georgiano",
    "Ghana" : "inglés",
    "Granada" : "inglés",
    "Grecia" : "griego",
    "Guatemala" : "castellano",
    "Guayana" : "inglés",
    "Guinea" : "francés",
    "Guinea Ecuatorial" : "castellano",
    "Guinea-Bissáu" : "portugués",
    "Haití" : "criollo haitiano",
    "Honduras" : "castellano",
    "Hungría" : "húngaro",
    "India" : "hindi",
    "Indonesia" : "indonesio",
    "Irak" : "árabe",
    "Irán" : "persa",
    "Irlanda" : "irlandes",
    "Islandia" : "islandes",
    "Israel" : "hebreo",
	"Italia" : "italiano",
    "Jamaica" : "inglés",
    "Japón" : "japonés",
    "Jordania" : "árabe",
    "Kazajistán" : "kazajo",
    "Kenia" : "suahili",
    "Kirguizistán" : "kirguis",
    "Kiribati" : "kiribatiano",
    "Kuwait" : "árabe",
    "Laos" : "lao",
    "Lesoto" : "soto meridional",
    "Letonia" : "letón",
    "Líbano" : "árabe",
    "Liberia" : "inglés",
    "Libia" : "	árabe",
    "Liechtenstein" : "alemán",
    "Lituania" : "lituano",
    "Luxemburgo" : "luxemburgués",
    "Macedonia" : "macedonio",
    "Madagascar" : "malgache",
    "Malasia" : "malayo",
    "Malaui" : "chicheua",
    "Maldivas" : "maldivo",
    "Malí" : "francés",
    "Malta" : "maltés",
    "Marruecos" : "árabe",
    "Marshall" : "marshalés",
    "Mauricio" : "inglés",
    "Mauritania" : "árabe",
    "México" : "castellano",
    "Micronesia" : "inglés",
    "Moldavia" : "rumano",
    "Mónaco" : "francés",
    "Mongolia" : "mongol",
    "Montenegro" : "serbio",
    "Mozambique" : "portugués",
    "Namibia" : "inglés",
    "Nauru" : "nauruano",
    "Nepal" : "nepalí",
    "Nicaragua" : "castellano",
    "Níger" : "francés",
    "Nigeria" : "inglés",
    "Noruega" : "noruego",
    "Nueva Zelanda" : "inglés",
    "Omán" : "árabe",
    "Países Bajos" : "neerlandés",
    "Pakistán" : "urdu",
    "Palaos" : "palauano",
    "Panamá" : "castellano",
    "Papúa-Nueva Guinea" : "tok pisin",
    "Paraguay" : "castellano",
    "Perú" : "castellano",
    "Polonia" : "polaco",
    "Portugal" : "portugués",
    "Puerto Rico" : "castellano",
    "Qatar" : "árabe",
    "Reino Unido" : "inglés",
    "República Centroafricana" : "francés",
    "República Checa" : "checo",
    "República del Congo" : "",
    "República Democrática del Congo" : "francés",
    "República Dominicana" : "castellano",
    "Ruanda" : "ruanda",
    "Rumanía" : "rumano",
    "Rusia" : "ruso",
    "Salomón" : "inglés",
    "Samoa" : "samoano",
    "San Cristóbal y Nieves" : "inglés",
    "San Marino" : "italiano",
    "San Vicente y las Granadinas" : "inglés",
    "Santa Lucía" : "inglés",
    "Santo Tomé y Príncipe" : "portugués",
    "Senegal" : "francés",
    "Serbia" : "serbio",
    "Seychelles" : "criollo seychellense",
    "Sierra Leona" : "inglés",
    "Singapur" : "malayo",
    "Siria" : "árabe",
    "Somalia" : "somalí",
    "Suazilandia" : "suazi",
    "Sudáfrica" : "zulú",
    "Sudán" : "árabe",
    "Suecia" : "sueco ",
    "Suiza" : "alemán",
    "Surinam" : "neerlandés",
    "Tailandia" : "tailandés",
    "Tanzania" : "suahili",
    "Tayikistán" : "tayiko",
    "Timor Oriental" : "tetum",
    "Togo" : "mina",
    "Tonga" : "tongano",
    "Trinidad y Tobago" : "inglés",
    "Túnez" : "árabe",
    "Turkmenistán" : "turcomano",
    "Turquía" : "turco",
    "Tuvalu" : "tuvaluano",
    "Ucrania" : "ucraniano",
    "Uganda" : "inglés",
    "Uruguay" : "castellano",
    "Uzbekistán" : "uzbeko",
    "Vanuatu" : "bislama",
    "Venezuela" : "castellano",
    "Vietnam" : "vietnamita",
    "Yemen" : "árabe",
    "Yibuti" : "somali",
    "Zambia" : "inglés",
    "Zimbabue" : "inglés"
}
    
    country = random.choice(paises)
    language = paises_idiomas.get(country)
    
    country = accentsfree(country)
    country = "". join(country)
    country = country.capitalize()
    
    language = accentsfree(language)
    language = "".join(language)
    language = language.capitalize()
    
    return country, language

def paisesContinents():
    
    paises_continentes = {
"Afganistán" : "Asia del Sur",
"Albania" : "Europa del Sur",
"Alemania" : "Europa del Oeste",
"Andorra" : "Europa del Sur",
"Angola" : "África Central",
"Antigua y Barbuda" : "Antillas",
"Arabia Saudita" : "Asia del Oeste",
"Argelia" : "África del Norte",
"Argentina" : "América del Sur",
"Armenia" : "Asia del Oeste",
"Australia" : "Australasia",
"Austria" : "Europa del Oeste",
"Azerbaiyán" : "Asia del Oeste",
"Bahamas" : "Antillas ",
"Baréin" : "Asia del Oeste",
"Banglades" : "Asia del Sur",
"Barbados" : "Antillas",
"Bélgica" : "Europa del Oeste",
"Belice" : "América Central",
"Benín" : "África del Oeste",
"Bielorrusia" : "Europa del Este",
"Birmania" : "Sudeste Asiático",
"Bolivia" : "América del Sur",
"Bosnia y Herzegovina" : "Europa del Sur",
"Botsuana" : "África del Sur",
"Brasil" : "América del Sur",
"Bulgaria": "Europa del Este",
"Brunéi" : "Sudeste Asiático",
"Burkina Faso" : "África del Oeste",
"Burundi" : "África del Este",
"Bután" : "Asia del Sur",
"Cabo Verde" : "África del Oeste",
"Camboya" : "Sudeste Asiático",
"Camerún" : "África Central",
"Canadá" : "América del Norte",
"Sri Lanka" : "Asia del Sur",
"Chad" : "África Central",
"Chile" : "América del Sur",
"China" : "Asia del Este",
"Chipre" : "Europa del Sur",
"Ciudad del Vaticano" : "Europa del Sur",
"Colombia" : "América del Sur",
"Comoras" : "África del Este",
"Corea del Norte" : "Asia del Este",
"Corea del Sur" : "Asia del Este",
"Costa de Marfil" : "África del Oeste",
"Costa Rica" : "América Central",
"Croacia" : "Europa del Sur",
"Cuba" : "Antillas",
"Dinamarca" : "Europa del Norte",
"Dominica" : "Antillas",
"Ecuador" : "América del Sur",
"Egipto" : "África del Norte",
"El Salvador" : "América Central",
"Emiratos Árabes Unidos" : "Asia del Oeste",
"Eritrea" : "África del Este",
"Eslovaquia" : "Europa del Este",
"Eslovenia" : "Europa del Sur",
"España" : "Europa del Sur",
"Estados Unidos" : "América del Norte",
"Estonia" : "Europa del Norte",
"Etiopía" : "África del Este",
"Filipinas" : "Sudeste Asiático",
"Finlandia" : "Europa del Norte",
"Fiyi" : "Melanesia",
"Francia" : "Europa del Oeste",
"Gabón" : "África Central",
"Gambia" : "África del Oeste",
"Georgia" : "Asia del Oeste",
"Ghana" : "África del Oeste",
"Granada" : "Antillas",
"Grecia" : "Europa del Sur",
"Guatemala" : "América Central",
"Guayana" : "América del Sur",
"Guinea" : "África del Oeste",
"Guinea Ecuatorial" : "África Central",
"Guinea-Bissau" : "África del Oeste",
"Haití" : "Antillas",
"Honduras" : "América Central",
"Hungría" : "Europa del Este",
"India" : "Asia del Sur",
"Indonesia" : "Sudeste Asiático",
"Irak" : "Asia del Oeste",
"Irán" : "Asia del Sur",
"Irlanda" : "Europa del Norte",
"Islandia" : "Europa del Norte",
"Israel" : "Asia del Oeste",
"Italia" : "Europa del Sur",
"Jamaica" : "Antillas",
"Japón" : "Asia del Este",
"Jordania" : "Asia del Oeste",
"Kazajistán" : "Asia Central",
"Kenia" : "África del Este",
"Kirguistán" : "Asia Central",
"Kiribati" : "Micronesia",
"Kuwait" : "Asia del Oeste",
"Laos" : "Sudeste Asiático",
"Lesoto" : "África del Sur",
"Letonia" : "Europa del Norte",
"Líbano" : "Asia del Oeste",
"Liberia" : "África del Oeste",
"Libia" : "África del Norte",
"Liechtenstein" : "Europa del Oeste",
"Lituania" : "Europa del Norte",
"Luxemburgo" : "Europa del Oeste",
"Macedonia del Norte" : "Europa del Sur",
"Madagascar" : "África del Este",
"Malasia" : "Sudeste Asiático",
"Malaui" : "África del Este",
"Maldivas" : "Asia del Sur",
"Malí" : "África del Oeste",
"Malta" : "Europa del Sur",
"Marruecos" : "África del Norte",
"Islas Marshall" : "Micronesia",
"Mauricio" : "África del Este",
"Mauritania" : "África del Oeste",
"México" : "América del Norte",
"Micronesia" : "Micronesia",
"Moldavia" : "Europa del Este",
"Mónaco" : "Europa del Oeste",
"Mongolia" : "Asia del Este",
"Montenegro" : "Europa del Sur",
"Mozambique" : "África del Este",
"Namibia" : "África del Sur",
"Nauru" : "Micronesia",
"Nepal" : "Asia del Sur",
"Nicaragua" : "América Central",
"Níger" : "África del Oeste",
"Nigeria" : "África del Oeste",
"Noruega" : "Europa del Norte",
"Nueva Zelanda" : "Australasia",
"Omán" : "Asia del Oeste",
"Países Bajos" : "Europa del Oeste",
"Pakistán" : "Asia del Sur",
"Palaos" : "Micronesia",
"Panamá" : "América Central",
"Papúa Nueva Guinea" : "Melanesia",
"Paraguay" : "América del Sur",
"Perú" : "América del Sur",
"Polonia" : "Europa del Este",
"Portugal" : "Europa del Sur",
"Puerto Rico" : "Antillas",
"Qatar" : "Asia del Oeste",
"Reino Unido" : "Europa del Norte",
"República Centroafricana" : "África Central",
"República Checa" : "Europa del Este",
"República del Congo" : "África Central",
"República Democrática del Congo" : "África Central",
"República Dominicana" : "Antillas",
"Ruanda" : "África del Este",
"Rumanía" : "Europa del Este",
"Rusia" : "Europa del Este",
"Salomón" : "Melanesia",
"Samoa" : "Polinesia",
"San Cristóbal y Nieves" : "Antillas",
"San Marino" : "Europa del Sur",
"San Vicente y las Granadinas" : "Antillas",
"Santa Lucía" : "Antillas",
"Santo Tomé y Príncipe" : "África Central",
"Senegal" : "África del Oeste",
"Serbia" : "Europa del Sur",
"Seychelles" : "África del Este",
"Sierra Leona" : "África del Oeste",
"Singapur" : "Sudeste Asiático",
"Siria" : "Asia del Oeste",
"Somalia" : "África del Este",
"Suazilandia" : "África del Sur",
"Sudáfrica" : "África del Sur",
"Sudán" : "África del Este",
"Suecia" : "Europa del Norte",
"Suiza" : "Europa del Oeste",
"Surinam" : "América del Sur",
"Tailandia" : "Sudeste Asiático",
"Tanzania" : "África del Este",
"Tayikistán" : "Asia Central",
"Timor Oriental" : "Sudeste Asiático",
"Togo" : "África del Oeste",
"Tonga" : "Polinesia",
"Trinidad y Tobago" : "América del Sur",
"Túnez" : "África del Norte",
"Turkmenistán" : "Asia Central",
"Turquía" : "Asia del Oeste",
"Tuvalu" : "Polinesia",
"Ucrania" : "Europa del Este",
"Uganda" : "África del Este",
"Uruguay" : "América del Sur",
"Uzbekistán" : "Asia Central",
"Vanuatu" : "Melanesia",
"Venezuela" : "América del Sur",
"Vietnam" : "Sudeste Asiático",
"Yemen" : "Asia del Oeste",
"Yibuti" : "África del Este",
"Zambia" : "África del Este",
"Zimbabue" : "África del Sur",
    
}
    
    continentes = list(paises_continentes.values())
    counContinent = random.choice(paises)
    kontinenti = paises_continentes.get(counContinent)
    
    try:
        counContinent = accentsfree(counContinent)
        counContinent = "". join(counContinent)
        counContinent = counContinent.capitalize()
        kontinenti = accentsfree(kontinenti)
        kontinenti = "".join(kontinenti)
        kontinenti = kontinenti.capitalize()
        continentes = accentsfree(continentes)
        continentes = capitalize_lists(continentes)
    except:
        print("continentes y paises", counContinent, kontinenti, continentes)
        
    return counContinent, kontinenti, continentes

def famLang():
    
    ezitsi = random.choice(idiomas)
    famDEidiomas = get_key(famIdiomas, ezitsi)
    fami__diomas = list(famIdiomas.keys())
    

    try:
        ezitsi = accentsfree(ezitsi)
        ezitsi = "".join(ezitsi)
        ezitsi = ezitsi.capitalize()
        famDEidiomas = accentsfree(famDEidiomas)
        famDEidiomas = "".join(famDEidiomas)
        famDEidiomas = famDEidiomas.capitalize()
        fami__diomas = accentsfree(fami__diomas)
        fami__diomas = capitalize_lists(fami__diomas)
    except:
        print("familias de idiomas e idiomas", ezitsi, famDEidiomas, fami__diomas)
            
    return ezitsi, famDEidiomas, fami__diomas

def famlinglang():
    
    famlinguistica = {
    "lenguas indoeuropeas" : ["armenio","albanes", "griego", "lenguas romances", "lenguas indoiranias", "lenguas celticas", "lenguas germanicas", "lenguas balticas", "lenguas eslavas", "Lenguas uralicas", "lenguas turquicas"],  
    "lenguas afroasiaticas" : ["lenguas semiticas", "lenguas cusitas", "lenguas chadicas"],
    "lenguas del africa subsahariana" : ["lenguas nigerocongolesas"],
    "lenguas del sudeste asiatico" : ["lenguas sino-tibetanas","lenguas austroasiáticas"],
    "lenguas de oceania": ["lenguas austronesias"],
    "lenguas del este de asia"  : ["lenguas japónicas", "lenguas mongolicas", "lenguas coreanicas"]}
    
    #una familia de idiomas random
    LangSemeistvo = random.choice(list(famIdiomas.keys()))
    #lista de familias linguisticas
    linguistics = list(famlinguistica.keys())
    #familia linguistica y la familia de idiomas correspondiente
    Lingfam = get_key(famlinguistica, LangSemeistvo)
    
    try:
        LangSemeistvo = accentsfree(LangSemeistvo)
        LangSemeistvo = "".join(LangSemeistvo)
        LangSemeistvo = LangSemeistvo.capitalize()
        Lingfam = accentsfree(Lingfam)
        Lingfam = "".join(Lingfam)
        Lingfam = Lingfam.capitalize()
        linguistics = accentsfree(linguistics)
        linguistics = capitalize_lists(linguistics)
        
    except:
        print("familia linguistica y familia de idiomas", LangSemeistvo, Lingfam, linguistics)
        
    return LangSemeistvo, Lingfam, linguistics

country, language = langPaisesGam()
counContinent, kontinenti, continentes  = paisesContinents()
ezitsi, famDEidiomas, fami__diomas = famLang()
LangSemeistvo, Lingfam, linguistics = famlinglang()

game = print("¿Qué tipo de juego quieres jugar?")
print("A) Paises e idiomas")
print("B) Paises y continentes")
print("C) Idiomas y familias de idiomas")
print("D) Familias de idiomas y familias linguisticas")
answer = input()

if answer == "A":
    yatusabe = lista_random(idiomas, language)
    option1, option2, option3, option4, option5, option6 = yatusabe
    lang = yatusabe.index(language)
    lang = lang + 1
        
    print(f"¿Cuál es el idioma mas hablado de {country}?")
    print(f"1) {option1}")
    print(f"2) {option2}")
    print(f"3) {option3}")
    print(f"4) {option4}")
    print(f"5) {option5}")
    print(f"6) {option6}")
    respuesta = int(input())
    if respuesta == lang:
        print("NOJODA MAMAÑEMA Q ARRECHO Q ERE")
        
    else:
        print("Asi no era, pajuo. La respuesta correcta era la numero", lang)
        
    print("_____________.byee")    

if answer == "B":
        yatusabe = lista_random(continentes, kontinenti)
        option1, option2, option3, option4, option5, option6 = yatusabe
        kon = yatusabe.index(kontinenti)
        kon = kon + 1
        
        print(f"¿A qué continente pertenece {counContinent}?")
        print(f"1) {option1}")
        print(f"2) {option2}")
        print(f"3) {option3}")
        print(f"4) {option4}")
        print(f"5) {option5}")
        print(f"6) {option6}")
        respuesta = int(input())
        if respuesta == kon:
            print("NOJODA MAMAÑEMA Q ARRECHO Q ERE")
            
        else:
            print("Asi no era, pajuo. La respuesta correcta era la numero", kon)
            
        print("_____________.byee")

if answer == "C":
    try:
        yatusabe = lista_random(fami__diomas, famDEidiomas)
        option1, option2, option3, option4, option5, option6 = yatusabe
        famidim = yatusabe.index(famDEidiomas)
        famidim = famidim + 1
        
        print(f"¿A qué familia de idiomas pertenece el {ezitsi}?")
        print(f"1) {option1}")
        print(f"2) {option2}")
        print(f"3) {option3}")
        print(f"4) {option4}")
        print(f"5) {option5}")
        print(f"6) {option6}")
        respuesta = int(input())
        if respuesta == famidim:
            print("NOJODA MAMAÑEMA Q ARRECHO Q ERE")
            
        else:
            print("Asi no era, pajuo. La respuesta correcta era la numero", famidim)
        
        print("_____________.byee")
        
    except:
        print(ezitsi, fami__diomas, famDEidiomas)

if answer == "D":
    try:
        yatusabe = lista_random(linguistics, Lingfam)
        option1, option2, option3, option4, option5, option6 = yatusabe
        falimg = yatusabe.index(Lingfam)
        falimg = falimg + 1
        
        print(f"¿A qué familia linguistica pertenecen el/las {LangSemeistvo}?")
        print(f"1) {option1}")
        print(f"2) {option2}")
        print(f"3) {option3}")
        print(f"4) {option4}")
        print(f"5) {option5}")
        print(f"6) {option6}")
        
        respuesta = int(input())
        
        if respuesta == falimg:
            print("NOJODA MAMAÑEMA Q ARRECHO Q ERE")
            
        else:
            print("Asi no era, pajuo. La respuesta correcta era la numero", falimg)
            
        print("_____________.byee")
        
    except:
        print(LangSemeistvo, linguistics, Lingfam)
