#!/bin/bash

################################################################################
# Generates a pdf file from the input lecture slides pdf that
# can be added to my binder and has space for taking extra notes.
################################################################################

PDF="$1"

NAME="${1%.pdf}"

echo "Name  "${NAME}

PAGES=$(pdftk "${PDF}" dump_data | grep NumberOfPages | sed 's/NumberOfPages: \([0-9]*\)/\1/')
SIZEX=$(pdftk "${PDF}" dump_data | grep PageMediaDimensions | head -n 1 | sed 's/PageMediaDimensions: \([0-9]*\) \([0-9]*\)/\1/')
SIZEY=$(pdftk "${PDF}" dump_data | grep PageMediaDimensions | head -n 1 | sed 's/PageMediaDimensions: \([0-9]*\) \([0-9]*\)/\2/')

echo "Pages: "${PAGES}
echo "SizeX: "${SIZEX}
echo "SizeY: "${SIZEY}

convert xc:white -page ${SIZEX}x${SIZEY} blank.pdf

PLUS=$((2*(4-(PAGES % 4))))

if [ "$PLUS" -eq "8" ]; then
   PLUS=0;
fi

COMMAND=$((seq ${PAGES} | xargs -i echo "A{} B1"); (seq $PLUS  | xargs -i echo "B1") | tr '\n' ' ')

echo $COMMAND

pdftk A="${PDF}" B=blank.pdf cat ${COMMAND} output combined.pdf

# convert combined.pdf -bordercolor black -border 10 with_border.pdf

pdfjam combined.pdf --nup 2x4 --clip true --frame true --outfile fixed.pdf

pdfcrop fixed.pdf nowhite.pdf

pdfcrop --margin '40 20 40 20' fixed.pdf very_fixed.pdf

pdfjam very_fixed.pdf --twoside --offset '40px 0px' --a4paper --no-landscape --outfile "${NAME}"_handout.pdf

rm blank.pdf
rm combined.pdf
rm nowhite.pdf
rm fixed.pdf
rm very_fixed.pdf
