#!/bin/bash
if [ "$1" == "" ]; then
    /home/cifali/.local/bin/playerpiano --color ifrs_presentation.presentation
    for i in $(seq 0 10); do
        /home/cifali/.local/bin/playerpiano --color ifrs_presentation.exemplo_$i
    done
    /home/cifali/.local/bin/playerpiano --color ifrs_presentation.exemplo_final 
    python3.6 -m webbrowser 'https://www.facebook.com/media/set/?set=a.303043140123523.1073741830.179285999165905&type=1&l=c03b3bc5ea'
    python3.6 -m webbrowser 'https://photos.google.com/share/AF1QipOkgv1ekbTN-QoZUwpCJIXHfMcFBeyRd2DpIBVFHU841n00VZEk6Cudijz1TtY-2w?key=M29oNEU4d2FkZGV2LXN3YTVfQ2JsMHkwd3lyS2ln'
else
    /home/cifali/.local/bin/playerpiano --color ifrs_presentation.exemplo_$1
fi
