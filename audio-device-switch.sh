#!/bin/bash

declare -i sinks_count=`pacmd list-sinks | grep -c index:[[:space:]][[:digit:]]`
declare -i active_sink_index=`pacmd list-sinks | sed -n -e 's/\*[[:space:]]index:[[:space:]]\([[:digit:]]\)/\1/p'`
declare -i major_sink_index=$sinks_count
declare -i next_sink_index=1

if [ $active_sink_index -ne $major_sink_index ] ; then
    next_sink_index=active_sink_index+1
fi

declare -i new_sink_index=$next_sink_index

#change the default sink
pacmd "set-default-sink ${new_sink_index}"


# move all inputs to the new sink: $new_sink_index"

for app in $(pacmd list-sink-inputs | sed -n -e 's/index:[[:space:]]\([[:digit:]]\)/\1/p');
do
    pacmd "move-sink-input $app $new_sink_index"
done

# echo 'display notification'
declare -i ndx=1
pacmd list-sinks | sed -n -e 's/device.description[[:space:]]=[[:space:]]"\(.*\)"/\1/p' | while read line;
do
    if [ $new_sink_index -eq $ndx ] ; then
        notify-send -i audio-volume-high "Sound output switched to" "$line"
        exit
    fi
    ndx=ndx+1
done
