#!/bin/bash

FILES=$(find "$1" -type f -iname '*.png')

FIXED=0
for f in $FILES; do
    WARN=$(pngcrush -n -warn "$f" 2>&1)
    if [[ "$WARN" == *"PCS illuminant is not D50"* ]] || [[ "$WARN" == *"known incorrect sRGB profile"* ]]; then
        pngcrush -s -ow -rem allb -reduce "$f"
        FIXED=$((FIXED + 1))
    fi
done

echo "$FIXED errors fixed"

PAUSE