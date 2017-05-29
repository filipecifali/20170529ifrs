#!/bin/bash
if [ "$1" == "" ]; then
    playerpiano --color ifrs_presentation.presentation
    for i in $(seq 0 9); do
        playerpiano --color ifrs_presentation.exemplo_$i
    done
    playerpiano --color ifrs_presentation.exemplo_final
else
    playerpiano --color ifrs_presentation.exemplo_$1
fi
