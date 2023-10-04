#STRINGS = LIST OF CHARACTERS
mijn_string = "waterijsje"
for whatever in mijn_string:
    print(whatever)
#Hierboven zie je een string dat gekoppeld is aan een variabele.
#In string kan je in principe hetzelfde zien als een list met verschillende elementen dat gekoppeld is aan 1 variabele.
#Bij een string zijn de verschillende letters of karakters de elementen die gekoppeld zijn aan een variabele.
#Dit wordt duidelijk wanneer je een for-loop combineert met een string. Alle karakters worden dan één voor één geprint, net als bij een list.

#SPLITSEN EN SUB-STRINGS
print()
print(mijn_string[4])
#Je kunt een betaald element/ karakter uit de string printen door de index aan te geven. (Net als bij een list)

print()
mijn_string = "ham, eieren, koffie en thee"
print(mijn_string[5:11])
print(mijn_string[13:19])
print(mijn_string[23:])
print(mijn_string[:3])
#Je kunt een betaald element/ karakter uit de string printen door de index aan te geven. (Net als bij een list)

#STRINGS BEWERKEN/ SAMENVOEGEN
print()
str1 = "zon"
str2 = "licht"
totaal_str = str1 + str2
print(totaal_str)
#Je kunt strings op verschillende manieren bewerken
#door de manier hierboven, voeg je meerdere strings samen d.m.v. een plus teken.

print()
voornaam = "Jan"
achternaam = "de Vries"
naam = voornaam + " " + achternaam
print(naam)
#door de manier hierboven, voeg je meerdere strings samen met een spatie ertussen.

print()
print(10 * naam)
#Je kunt een bepaalde string meerdere malen printen d.m.v. de hierboven getoonde manier

#FORMATTED STRINGS
print()
a = "Maandag"
b = "Dinsdag"
c = "Woensdag"
print(f"Eerst komt {a}, dan komt {b} en dan komt {c}.")
#Dit is een andere en betere manier om meerdere strings samen te voegen.
#Deze manier gebruik je als je variabelen en tekst wilt combineren.

#STRING METHODS
print()
text = "Mijn Voorbeeld"

lowercase_text = text.lower()
print(lowercase_text)
#De .lower() method, zorgt ervoor dat de hele string in kleine letters geprint wordt.

uppercase_text = text.upper()
print(uppercase_text)
#De .upper() method, zorgt ervoor dat de hele string in hoofdletters geprint wordt.

split_text = text.split(" ")
print(split_text)
#De .split() method, zorgt ervoor dat de string opgesplitst wordt in een list.
#Dat wat achter .split tussen haakjes staat, wordt gebruikt als breekpunt.

index_text = text.index("Voorbeeld")
print(index_text)
#De .index() method, print de eerste index die gevonden wordt van de opgegeven substring.

replace_text = text.replace("Voorbeeld", "Voorbeelden")
print(replace_text)
#De .replace() method, vervangt de gekozen string met het opgegeven element