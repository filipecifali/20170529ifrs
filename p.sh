#!/bin/bash
if [ "$1" == "" ]; then
    /home/cifali/.local/bin/playerpiano --color ifrs_presentation.presentation
    for i in $(seq 0 9); do
        /home/cifali/.local/bin/playerpiano --color ifrs_presentation.exemplo_$i
    done
    /home/cifali/.local/bin/playerpiano --color ifrs_presentation.exemplo_final
else
    /home/cifali/.local/bin/playerpiano --color ifrs_presentation.exemplo_$1
fi
