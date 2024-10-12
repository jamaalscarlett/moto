# -*- coding: utf-8 -*-

# This data is a verbatim copy of that produced using the AWS CLI (requires AWS
# account) and jq utility to pull out the right part and reformat:
#
# aws polly describe-voices | jq .Voices --indent 4
VOICE_DATA = [
    {
        "Gender": "Female",
        "Id": "Isabelle",
        "LanguageCode": "fr-BE",
        "LanguageName": "Belgian French",
        "Name": "Isabelle",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Danielle",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Danielle",
        "SupportedEngines": ["long-form", "neural"],
    },
    {
        "Gender": "Male",
        "Id": "Gregory",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Gregory",
        "SupportedEngines": ["long-form", "neural"],
    },
    {
        "Gender": "Female",
        "Id": "Burcu",
        "LanguageCode": "tr-TR",
        "LanguageName": "Turkish",
        "Name": "Burcu",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Jitka",
        "LanguageCode": "cs-CZ",
        "LanguageName": "Czech",
        "Name": "Jitka",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Sabrina",
        "LanguageCode": "de-CH",
        "LanguageName": "Swiss Standard German",
        "Name": "Sabrina",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Kevin",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Kevin",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Filiz",
        "LanguageCode": "tr-TR",
        "LanguageName": "Turkish",
        "Name": "Filiz",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Elin",
        "LanguageCode": "sv-SE",
        "LanguageName": "Swedish",
        "Name": "Elin",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Astrid",
        "LanguageCode": "sv-SE",
        "LanguageName": "Swedish",
        "Name": "Astrid",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Tatyana",
        "LanguageCode": "ru-RU",
        "LanguageName": "Russian",
        "Name": "Tatyana",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Maxim",
        "LanguageCode": "ru-RU",
        "LanguageName": "Russian",
        "Name": "Maxim",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Carmen",
        "LanguageCode": "ro-RO",
        "LanguageName": "Romanian",
        "Name": "Carmen",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Ines",
        "LanguageCode": "pt-PT",
        "LanguageName": "Portuguese",
        "Name": "Inês",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Cristiano",
        "LanguageCode": "pt-PT",
        "LanguageName": "Portuguese",
        "Name": "Cristiano",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Vitoria",
        "LanguageCode": "pt-BR",
        "LanguageName": "Brazilian Portuguese",
        "Name": "Vitória",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Ricardo",
        "LanguageCode": "pt-BR",
        "LanguageName": "Brazilian Portuguese",
        "Name": "Ricardo",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Camila",
        "LanguageCode": "pt-BR",
        "LanguageName": "Brazilian Portuguese",
        "Name": "Camila",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Maja",
        "LanguageCode": "pl-PL",
        "LanguageName": "Polish",
        "Name": "Maja",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Jan",
        "LanguageCode": "pl-PL",
        "LanguageName": "Polish",
        "Name": "Jan",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Jacek",
        "LanguageCode": "pl-PL",
        "LanguageName": "Polish",
        "Name": "Jacek",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Ewa",
        "LanguageCode": "pl-PL",
        "LanguageName": "Polish",
        "Name": "Ewa",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Ola",
        "LanguageCode": "pl-PL",
        "LanguageName": "Polish",
        "Name": "Ola",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Lisa",
        "LanguageCode": "nl-BE",
        "LanguageName": "Belgian Dutch",
        "Name": "Lisa",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Ruben",
        "LanguageCode": "nl-NL",
        "LanguageName": "Dutch",
        "Name": "Ruben",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Lotte",
        "LanguageCode": "nl-NL",
        "LanguageName": "Dutch",
        "Name": "Lotte",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Laura",
        "LanguageCode": "nl-NL",
        "LanguageName": "Dutch",
        "Name": "Laura",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Ida",
        "LanguageCode": "nb-NO",
        "LanguageName": "Norwegian",
        "Name": "Ida",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Liv",
        "LanguageCode": "nb-NO",
        "LanguageName": "Norwegian",
        "Name": "Liv",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Seoyeon",
        "LanguageCode": "ko-KR",
        "LanguageName": "Korean",
        "Name": "Seoyeon",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Kazuha",
        "LanguageCode": "ja-JP",
        "LanguageName": "Japanese",
        "Name": "Kazuha",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Tomoko",
        "LanguageCode": "ja-JP",
        "LanguageName": "Japanese",
        "Name": "Tomoko",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Takumi",
        "LanguageCode": "ja-JP",
        "LanguageName": "Japanese",
        "Name": "Takumi",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Mizuki",
        "LanguageCode": "ja-JP",
        "LanguageName": "Japanese",
        "Name": "Mizuki",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Bianca",
        "LanguageCode": "it-IT",
        "LanguageName": "Italian",
        "Name": "Bianca",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Giorgio",
        "LanguageCode": "it-IT",
        "LanguageName": "Italian",
        "Name": "Giorgio",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Carla",
        "LanguageCode": "it-IT",
        "LanguageName": "Italian",
        "Name": "Carla",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Karl",
        "LanguageCode": "is-IS",
        "LanguageName": "Icelandic",
        "Name": "Karl",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Dora",
        "LanguageCode": "is-IS",
        "LanguageName": "Icelandic",
        "Name": "Dóra",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Mathieu",
        "LanguageCode": "fr-FR",
        "LanguageName": "French",
        "Name": "Mathieu",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Lea",
        "LanguageCode": "fr-FR",
        "LanguageName": "French",
        "Name": "Léa",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Celine",
        "LanguageCode": "fr-FR",
        "LanguageName": "French",
        "Name": "Céline",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Chantal",
        "LanguageCode": "fr-CA",
        "LanguageName": "Canadian French",
        "Name": "Chantal",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Gabrielle",
        "LanguageCode": "fr-CA",
        "LanguageName": "Canadian French",
        "Name": "Gabrielle",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Penelope",
        "LanguageCode": "es-US",
        "LanguageName": "US Spanish",
        "Name": "Penélope",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Miguel",
        "LanguageCode": "es-US",
        "LanguageName": "US Spanish",
        "Name": "Miguel",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Lupe",
        "LanguageCode": "es-US",
        "LanguageName": "US Spanish",
        "Name": "Lupe",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Mia",
        "LanguageCode": "es-MX",
        "LanguageName": "Mexican Spanish",
        "Name": "Mia",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Lucia",
        "LanguageCode": "es-ES",
        "LanguageName": "Castilian Spanish",
        "Name": "Lucia",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Enrique",
        "LanguageCode": "es-ES",
        "LanguageName": "Castilian Spanish",
        "Name": "Enrique",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Conchita",
        "LanguageCode": "es-ES",
        "LanguageName": "Castilian Spanish",
        "Name": "Conchita",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Geraint",
        "LanguageCode": "en-GB-WLS",
        "LanguageName": "Welsh English",
        "Name": "Geraint",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Salli",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Salli",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Matthew",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Matthew",
        "SupportedEngines": ["generative", "neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Kimberly",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Kimberly",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Kendra",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Kendra",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Justin",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Justin",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Joey",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Joey",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Joanna",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Joanna",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Ivy",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Ivy",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Aria",
        "LanguageCode": "en-NZ",
        "LanguageName": "New Zealand English",
        "Name": "Aria",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Ayanda",
        "LanguageCode": "en-ZA",
        "LanguageName": "South African English",
        "Name": "Ayanda",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Raveena",
        "LanguageCode": "en-IN",
        "LanguageName": "Indian English",
        "Name": "Raveena",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Aditi",
        "LanguageCode": "en-IN",
        "LanguageName": "Indian English",
        "Name": "Aditi",
        "AdditionalLanguageCodes": ["hi-IN"],
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Emma",
        "LanguageCode": "en-GB",
        "LanguageName": "British English",
        "Name": "Emma",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Brian",
        "LanguageCode": "en-GB",
        "LanguageName": "British English",
        "Name": "Brian",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Amy",
        "LanguageCode": "en-GB",
        "LanguageName": "British English",
        "Name": "Amy",
        "SupportedEngines": ["generative", "neural", "standard"],
    },
    {
        "Gender": "Male",
        "Id": "Russell",
        "LanguageCode": "en-AU",
        "LanguageName": "Australian English",
        "Name": "Russell",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Nicole",
        "LanguageCode": "en-AU",
        "LanguageName": "Australian English",
        "Name": "Nicole",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Olivia",
        "LanguageCode": "en-AU",
        "LanguageName": "Australian English",
        "Name": "Olivia",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Vicki",
        "LanguageCode": "de-DE",
        "LanguageName": "German",
        "Name": "Vicki",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Marlene",
        "LanguageCode": "de-DE",
        "LanguageName": "German",
        "Name": "Marlene",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Hans",
        "LanguageCode": "de-DE",
        "LanguageName": "German",
        "Name": "Hans",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Naja",
        "LanguageCode": "da-DK",
        "LanguageName": "Danish",
        "Name": "Naja",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Male",
        "Id": "Mads",
        "LanguageCode": "da-DK",
        "LanguageName": "Danish",
        "Name": "Mads",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Sofie",
        "LanguageCode": "da-DK",
        "LanguageName": "Danish",
        "Name": "Sofie",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Gwyneth",
        "LanguageCode": "cy-GB",
        "LanguageName": "Welsh",
        "Name": "Gwyneth",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Zhiyu",
        "LanguageCode": "cmn-CN",
        "LanguageName": "Chinese Mandarin",
        "Name": "Zhiyu",
        "SupportedEngines": ["neural", "standard"],
    },
    {
        "Gender": "Female",
        "Id": "Zeina",
        "LanguageCode": "arb",
        "LanguageName": "Arabic",
        "Name": "Zeina",
        "SupportedEngines": ["standard"],
    },
    {
        "Gender": "Female",
        "Id": "Hala",
        "LanguageCode": "ar-AE",
        "LanguageName": "Gulf Arabic",
        "Name": "Hala",
        "AdditionalLanguageCodes": ["arb"],
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Arlet",
        "LanguageCode": "ca-ES",
        "LanguageName": "Catalan",
        "Name": "Arlet",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Hannah",
        "LanguageCode": "de-AT",
        "LanguageName": "Austrian German",
        "Name": "Hannah",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Ruth",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Ruth",
        "SupportedEngines": ["generative", "long-form", "neural"],
    },
    {
        "Gender": "Male",
        "Id": "Stephen",
        "LanguageCode": "en-US",
        "LanguageName": "US English",
        "Name": "Stephen",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Kajal",
        "LanguageCode": "en-IN",
        "LanguageName": "Indian English",
        "Name": "Kajal",
        "AdditionalLanguageCodes": ["hi-IN"],
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Hiujin",
        "LanguageCode": "yue-CN",
        "LanguageName": "Cantonese",
        "Name": "Hiujin",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Suvi",
        "LanguageCode": "fi-FI",
        "LanguageName": "Finnish",
        "Name": "Suvi",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Female",
        "Id": "Niamh",
        "LanguageCode": "en-IE",
        "LanguageName": "Irish English",
        "Name": "Niamh",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Arthur",
        "LanguageCode": "en-GB",
        "LanguageName": "British English",
        "Name": "Arthur",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Daniel",
        "LanguageCode": "de-DE",
        "LanguageName": "German",
        "Name": "Daniel",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Liam",
        "LanguageCode": "fr-CA",
        "LanguageName": "Canadian French",
        "Name": "Liam",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Pedro",
        "LanguageCode": "es-US",
        "LanguageName": "US Spanish",
        "Name": "Pedro",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Sergio",
        "LanguageCode": "es-ES",
        "LanguageName": "Castilian Spanish",
        "Name": "Sergio",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Andres",
        "LanguageCode": "es-MX",
        "LanguageName": "Mexican Spanish",
        "Name": "Andrés",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Remi",
        "LanguageCode": "fr-FR",
        "LanguageName": "French",
        "Name": "Rémi",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Adriano",
        "LanguageCode": "it-IT",
        "LanguageName": "Italian",
        "Name": "Adriano",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Thiago",
        "LanguageCode": "pt-BR",
        "LanguageName": "Brazilian Portuguese",
        "Name": "Thiago",
        "SupportedEngines": ["neural"],
    },
    {
        "Gender": "Male",
        "Id": "Zayd",
        "LanguageCode": "ar-AE",
        "LanguageName": "Gulf Arabic",
        "Name": "Zayd",
        "AdditionalLanguageCodes": ["arb"],
        "SupportedEngines": ["neural"],
    },
]

LANGUAGE_CODES = {voice["LanguageCode"] for voice in VOICE_DATA}

VOICE_IDS = {voice["Name"] for voice in VOICE_DATA}
