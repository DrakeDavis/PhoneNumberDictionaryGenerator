# PhoneNumberDictionaryGenerator
This generates a dictionary file of every United States phone number.

Assumed use is for a https://en.wikipedia.org/wiki/Dictionary_attack where a list of all possible phone numbers are needed.

To minimize size of the file only exact Area Codes are used, and NA Phone Number rules are observed: 
(NXX) NXX-XXXX, where N is 2–9 and X is 0–9

Full runtime is <1 hour (system specific) and full generated list is 21GB
To alleviate time or memory concerns - you can generate only specific states by deleting/commenting uneeded lines from AreaCodes.txt
