
---
title: "C# Case insensitive Contains -merkkijonon tarkistus"
description: "Tässä opetusohjelmassa opimme eri tapoja tehdä case insensitive string contains check in C#"

lead: ""
date: 2022-09-21T14:41:21+01:00
lastmod: 2022-09-21T14:41:21+01:00
draft: false
images: []
type: docs

---


Tässä opetusohjelmassa opimme eri tapoja tehdä case insensitive string contains check C#:ssa 

Se näyttää yksinkertaiselta ongelmalta, mutta C#:n `string.Contains()` -menetelmä on oletusarvoisesti isojen ja pienten kirjainten suhteen herkkä 

Ja jos merkkijono ei ole englanninkielinen eli muilla kielillä, emme voi verrata tekstiä tapauskohtaisesti suoraan 

Molempien merkkijonojen pitäisi olla samassa kulttuurissa ja meidän pitäisi tietää kielikulttuuri.

Useimmiten vertaamme vain englanninkielisiä merkkijonoja.

## Menetelmä 1: Käyttämällä C# `string.IndexOf()` -menetelmää.

Voimme käyttää C# `string.IndexOf()` -menetelmää tehdäksemme isojen ja pienten kirjainten erottelemattoman merkkijonon sisällön tarkistuksen.

`IndexOf()` metodi hyväksyy parametrin `StringComparison.OrdinalIgnoreCase`, jolla määritetään merkkien hakutyyppi.

```csharp

string textToCheck = "STRING Contains";
bool contains = textToCheck.IndexOf("string", StringComparison.OrdinalIgnoreCase) >= 0;

```

## Menetelmä 2: `string.Contains()` -menetelmän käyttäminen .Net 5+ ja .NET Core 2.0+ -ohjelmissa

Uusimmissa dot net -versioissa eli .Net Core 2.0+:ssa ja .Net 5+:ssa. `string.Contains()` -metodilla on ylikuormitettu metodi, joka hyväksyy parametrin `StringComparison`.

```csharp

string textToCheck = "STRING Contains";
bool checkContains = textToCheck.Contains("string",StringComparison.OrdinalIgnoreCase);

```

## Menetelmä 3: `Regex.IsMatch()` -metodin käyttäminen

Voimme käyttää säännöllisiä lausekkeita tehdäksemme isoja ja pieniä kirjaimia erittelemättömän contains-merkkijonon tarkistuksen.

Jos tunnet `Regex`, käytä `Regex.IsMatch()` -menetelmää ja tarkistaaksesi, ettei isoja ja pieniä kirjaimia huomioida, anna `RegexOptions.IgnoreCase` -parametri 

```csharp
var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = Regex.IsMatch(stringToCheck, Regex.Escape(substring), RegexOptions.IgnoreCase);

//true

```

## Menetelmä 4: Käyttämällä `.ToUpper()` &amp `.ToLower()`

Jos merkkijonot ovat englanninkielisiä ja suorituskyky ei ole ongelma, voimme muuntaa molemmat merkkijonot samaan tapaukseen ja tehdä sitten merkkijonon sisältötarkistuksen.

```csharp

var stringToSearch = "hI hEllo";
var substring = "hello";
bool contains = stringToSearch.ToLower().Contains(substring.ToLower());
or 
bool contains = stringToSearch.ToUpper().Contains(substring.ToUpper());

//true

```
## C# Case insensitive Contains -tarkistus muille kielille

Isojen ja pienten kirjainten tunnistamattomuus on kieliriippuvainen 

Esimerkiksi englannin kielessä `I` on `i` isolla alkukirjaimella kirjoitettu versio.

Turkkilaisessa kielessä taas `i`:n suuraakkosellinen versio on tuntematon merkki `İ`.

Jos haluamme tarkistaa merkkijonon ilman isoja ja pieniä kirjaimia, meidän on käytettävä `CultureInfo` -objektia.


```csharp

var text = "İ";

var check = "i";
            
CultureInfo trCulture = new CultureInfo("tr-TR",false);

bool englishContains = text.IndexOf(check, StringComparison.OrdinalIgnoreCase) >= 0;
//false

var turkishContains = trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
//true
```

Olen luonut `CultureInfo` -objektin turkkilaista kieltä varten. Ja verrannut molempia merkkijonoja käyttäen `CompareInfo` alla olevan kuvan mukaisesti.

```
trCulture.CompareInfo.IndexOf(check, text, CompareOptions.IgnoreCase) >= 0;
```

## Paras tapa tehdä Case-erottelematon Contains merkkijonon tarkistus

Jos käytät `.Net`:n uusinta versiota, käytä `string.Contains()` -menetelmää.

Muussa tapauksessa käytä `string.IndexOf()` -menetelmää.

Älä suosi `.ToUpper()` tai `To.Lower()` -menetelmää, koska ne voivat aiheuttaa suorituskykyongelmia.

Käytä `CultureInfo` -objektia muiden kielten merkkijonoille.

