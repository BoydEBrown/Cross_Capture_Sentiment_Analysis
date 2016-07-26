import requests
import os
import subprocess

export APIKEY = '<your API Key here>'
export PASSWORD = '<your password here>'

proc = subprocess.Popen(['curl "https://apis.voicebase.com/v2-beta/?apikey=${APIKEY}&password=${PASSWORD}" \
    | tee accept-invite-response.json | jq '.'', name],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE
                        )

    (out, err) = proc.communicate()
    print out

export TOKEN = $( jq --raw-output '.token' < accept-invite-response.json )
echo "Token:" ${TOKEN}a
