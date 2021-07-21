#!/bin/bash
echo ""
num=$(cat number_to_decrypt.txt)
key=$(cat private.key)
python3 -c "from baseQ import decrypt; print(decrypt('${num}', '${key}'))"