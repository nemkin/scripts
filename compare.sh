#!/bin/bash
diff <(find $1 -type f -exec md5sum {} + | sort -k 2 | sed 's/ .*\// /') <(find $2 -type f -exec md5sum {} + | sort -k 2 | sed 's/ .*\// /')

