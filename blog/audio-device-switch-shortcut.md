---
title: Atalho para trocar dispositivo de áudio no Linux
tags: [linux,audio,automation]
---

Entre reuniões virtuais usando headset, escutar música ou mesmo só assistir uma aula, eu prefiro que o headset seja usado só quando é necessário um isolamento.

Para as outras opções, as caixas de som ambiente são bem mais confortáveis.

No Ubuntu, é meio chatinho ficar chaveando entre os dispositivos de saída de áudio. Aqui na minha máquina, são uma meia dúzia de cliques de mouse.

Então este script aqui em baixo deixou as coisas bem mais interessantes. Fiz algumas alterações, mas a ideia eu peguei desse [link](https://askubuntu.com/questions/156895/how-to-switch-sound-output-with-key-shortcut).


## audio-device-switch.sh

```bash
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
```

Salve o arquivo em uma pasta segura, por exemplo /usr/local/bin/audio-device-switch.sh e dê as permissões de execução:

```bash
sudo chmod 755 /usr/local/bin/audio-device-switch.sh
```

## Configurações de atalho de teclado

Acesse o menu de setup da sua distribuição, e informe o nome do atalho (Audio Device Switch, no meu caso), o local onde o script está salvo, e o atalho que você deseja usar (Eu escolhi Win+F12).

Prontinho, agora é só aproveitar.