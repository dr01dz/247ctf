#!/bin/bash

for file in keys/*
do
    openssl rsa -in "$file" -text -noout -text -modulus >> $file
done
