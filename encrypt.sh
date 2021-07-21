#!/bin/bash
echo ""
msg=$(cat text_to_encrypt.txt)
key=$(cat private.key)
echo -n $(python3 -c "from baseQ import encrypt; print(encrypt('${msg}', '${key}'))") > number_to_decrypt.txt
cat number_to_decrypt.txt
echo ""