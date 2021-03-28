#!/bin/bash
# Upload hex to teensy. Must provide HEX environment var

set -Eeox pipefail

if [ -z $HEX ]; then
	echo "HEX environment variable not set"; exit 1
fi

set -u

REMOTE="${REMOTE:-debian@bb}"
REMOTEDIR="${REMOTEDIR:-/tmp}"
RSYNC_OPT="${RSYNC_OPT:--av}"
RSYNC_SRC="${RSYNC_SRC:-$(dirname $HEX)}"

RSYNC_RSH="ssh -q" rsync $RSYNC_OPT $RSYNC_SRC $REMOTE:$REMOTEDIR
ssh -vq $REMOTE teensy_loader_cli --mcu=imxrt1062 -w $REMOTEDIR/$(basename $RSYNC_SRC)/$(basename $HEX)
