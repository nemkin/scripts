egrep -v ^I | cut -d ':' -f 2 | sed -e 's/ \(.*\)/\1\t/g' | tr '\n' ' ' | sed 's/FEASIBLE/\nFEASIBLE/g' | sed 's/\t $//g'
echo ""

