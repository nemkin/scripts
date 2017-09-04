#!/bin/bash

################################################################################
# Generates a pdf file from the input lecture slides pdf that
# can be added to my binder and has space for taking extra notes.
################################################################################

PDF="$1"

PAGES=$(pdftk "${PDF}" dump_data | grep NumberOfPages | sed 's/NumberOfPages: \([0-9]*\)/\1/')
SIZEX=$(pdftk "${PDF}" dump_data | grep PageMediaDimensions | head -n 1 | sed 's/PageMediaDimensions: \([0-9]*\) \([0-9]*\)/\1/')
SIZEY=$(pdftk "${PDF}" dump_data | grep PageMediaDimensions | head -n 1 | sed 's/PageMediaDimensions: \([0-9]*\) \([0-9]*\)/\2/')

echo "Pages: "${PAGES}
echo "SizeX: "${SIZEX}
echo "SizeY: "${SIZEY}

convert xc:white -page ${SIZEX}x${SIZEY} blank.pdf

COMMAND=$(seq ${PAGES} | xargs -i echo "A{} B1" | tr '\n' ' ')

pdftk A="${PDF}" B=blank.pdf cat ${COMMAND} output combined.pdf

# convert combined.pdf -bordercolor black -border 10 with_border.pdf

pdfjam combined.pdf --offset '2cm 0cm' --nup 2x3 --a4paper --no-landscape --frame true --outfile result.pdf

rm blank.pdf
