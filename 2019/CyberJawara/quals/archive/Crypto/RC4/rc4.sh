#!/bin/sh

KEY=`hexdump -n 16 -e '4/4 "%08X" 1 "\n"' /dev/random`
cat "CYBER JAWARA 2019 QUALS - RULES-OF-THE-GAME.pdf" | openssl rc4-40 -K $KEY -nosalt -e -nopad > "CYBER JAWARA 2019 QUALS - RULES-OF-THE-GAME.pdf.encrypted"
cat "flag.pdf" | openssl rc4-40 -K $KEY -nosalt -e -nopad > "flag.pdf.encrypted"
